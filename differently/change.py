from functools import cached_property
from typing import Any, Optional

from differently.change_type import ChangeType


class Change:
    def __init__(self, before: Optional[str], after: Optional[str]) -> None:
        self.before = before
        self.after = after

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Change):
            return False
        return self.before == other.before and self.after == other.after

    def __repr__(self) -> str:
        return f"{self.before or ''} > {self.after or ''}"

    @cached_property
    def change_type(self) -> ChangeType:
        if self.before == self.after:
            return ChangeType.none
        if self.before is None:
            return ChangeType.insert
        if self.after is None:
            return ChangeType.delete
        return ChangeType.replace
