from typing import List, Optional

from colorama import Fore

from differently.change import Change
from differently.change_type import ChangeType


class TableRenderer:
    def __init__(self, changes: List[Change]) -> None:
        self.changes = changes

    @staticmethod
    def color(text: str, color: str) -> str:
        return f"{color}{text}{Fore.RESET}"

    @staticmethod
    def format_after(text: Optional[str], change: ChangeType) -> str:
        if not text:
            return ""
        if change in [ChangeType.insert, ChangeType.replace]:
            return TableRenderer.color(text, Fore.LIGHTYELLOW_EX)
        if change == ChangeType.none:
            return TableRenderer.color(text, Fore.LIGHTGREEN_EX)
        raise ValueError(f'no format-after for change "{change}" in "{text}"')

    @staticmethod
    def format_before(text: Optional[str], change: ChangeType) -> str:
        if not text:
            return ""
        if change == ChangeType.delete:
            b = "".join([f"{c}\u0336" for c in text])
            return TableRenderer.color(b, Fore.LIGHTRED_EX)
        if change == ChangeType.replace:
            return TableRenderer.color(text, Fore.LIGHTYELLOW_EX)
        if change == ChangeType.none:
            return TableRenderer.color(text, Fore.LIGHTGREEN_EX)
        raise ValueError(f'no format-before for change "{change}"')

    @staticmethod
    def arrow(change: ChangeType) -> str:
        if change == ChangeType.replace:
            return TableRenderer.color(">", Fore.LIGHTYELLOW_EX)
        if change == ChangeType.delete:
            return TableRenderer.color(">", Fore.LIGHTRED_EX)
        return ">"

    @property
    def table(self) -> str:
        if not self.changes:
            return ""

        longest_a = max([len(ch.before or "") for ch in self.changes])
        wip = ""

        for change in self.changes:
            pad = " " * (longest_a - len(change.before or ""))
            before = self.format_before(change.before, change.change_type)
            after = self.format_after(change.after, change.change_type)
            wip = f"{wip}{before}{pad} {self.arrow(change.change_type)} {after}"
            wip = f"{wip.strip()}\n"

        return wip.rstrip()
