from typing import List, Optional

from ansiscape import green, red, yellow
from ansiscape.checks import should_emit_codes

from differently.change import Change
from differently.change_type import ChangeType


class TableRenderer:
    def __init__(self, changes: List[Change], color: Optional[bool] = None) -> None:
        self.changes = changes
        self.color = should_emit_codes() if color is None else color

    @staticmethod
    def format_after(text: Optional[str], change: ChangeType) -> str:
        if not text:
            return ""
        if change in [ChangeType.insert, ChangeType.replace]:
            return yellow(text).encoded
        if change == ChangeType.none:
            return green(text).encoded
        raise ValueError(f'no format-after for change "{change}" in "{text}"')

    @staticmethod
    def format_before(text: Optional[str], change: ChangeType) -> str:
        if not text:
            return ""
        if change == ChangeType.delete:
            return red(text).encoded
        if change == ChangeType.replace:
            return yellow(text).encoded
        if change == ChangeType.none:
            return green(text).encoded
        raise ValueError(f'no format-before for change "{change}"')

    @staticmethod
    def format_arrow(arrow: str, change: ChangeType) -> str:
        if change == ChangeType.insert:
            return yellow(arrow).encoded
        if change == ChangeType.replace:
            return yellow(arrow).encoded
        if change == ChangeType.delete:
            return red(arrow).encoded
        return green(arrow).encoded

    @staticmethod
    def arrow(change: ChangeType) -> str:
        if change == ChangeType.insert:
            return ">"
        if change == ChangeType.replace:
            return "~"
        if change == ChangeType.delete:
            return "x"
        return "="

    @property
    def table(self) -> str:
        if not self.changes:
            return ""

        longest_a = max([len(ch.before or "") for ch in self.changes])
        wip = ""

        for change in self.changes:
            pad = " " * (longest_a - len(change.before or ""))
            before = (
                self.format_before(change.before, change.change_type)
                if self.color
                else (change.before or "")
            )
            after = (
                self.format_after(change.after, change.change_type)
                if self.color
                else (change.after or "")
            )
            arrow = self.arrow(change.change_type)
            arrow_fmt = (
                self.format_arrow(arrow, change.change_type) if self.color else arrow
            )
            wip = f"{wip}{before}{pad}  {arrow_fmt}  {after}"
            wip = f"{wip.strip()}\n"

        return wip.rstrip()
