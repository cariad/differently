from functools import cached_property

from differently.change_type import ChangeType


class Line:
    def __init__(self, diff: str) -> None:
        self.diff = diff

    @cached_property
    def change_type(self) -> ChangeType:
        if self.diff[0] == " ":
            return ChangeType.none
        if self.diff[0] == "+":
            return ChangeType.insert
        if self.diff[0] == "-":
            return ChangeType.delete
        return ChangeType.modify

    @cached_property
    def text(self) -> str:
        return self.diff[2:]
