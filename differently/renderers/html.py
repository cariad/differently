from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional

from differently.change import Change
from differently.change_type import ChangeType


class Side(Enum):
    A = "a"
    B = "b"


class Renderer(ABC):
    def __init__(self, changes: List[Change]) -> None:
        self.changes = changes

    @abstractmethod
    def format_line(
        self,
        a: str,
        b: str,
        longest_a: int,
        original_a: Optional[str],
        change: ChangeType,
    ) -> str:
        ...

    @abstractmethod
    def format_diff(self, diff: str) -> str:
        ...


    @abstractmethod
    def format_line_side(
        self,
        text: Optional[str],
        change: ChangeType,
        side: Side,
    ) -> str:
        ...

    def render(self) -> str:
        if not self.changes:
            return ""

        longest_a = max([len(ch.before or "") for ch in self.changes])
        wip = ""

        for change in self.changes:
            a = self.format_line_side(change.before, change.change_type, Side.A)
            b = self.format_line_side(change.after, change.change_type, Side.B)
            line = self.format_line(a, b, longest_a, change.before, change.change_type)
            wip += line

        return self.format_diff(wip)


class HtmlRenderer(Renderer):
    def format_line(
        self,
        a: str,
        b: str,
        longest_a: int,
        original_a: Optional[str],
        change: ChangeType,
    ) -> str:
        pad = "&nbsp;" * (longest_a - len(original_a or ""))
        return f"<div>{a}{pad} &gt; {b}</div>"

    def format_line_side(
        self, text: Optional[str], change: ChangeType, side: Side,
    ) -> str:
        if not text:
            return ""
        return f'<span class="{side} {change}">{text}</span>'

    def format_diff(self, diff: str) -> str:
        return f'<div style="font-family: monospace;">{diff}</div>'
