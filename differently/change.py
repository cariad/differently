from functools import cached_property
from typing import Any, Optional

from colorama import Fore

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
        return ChangeType.modify

    @cached_property
    def formatted_after(self) -> str:
        if not self.after:
            return ""

        if self.change_type == ChangeType.insert:
            return f"{Fore.LIGHTYELLOW_EX}{self.after}{Fore.RESET}"

        if self.change_type == ChangeType.modify:
            return f"{Fore.LIGHTYELLOW_EX}{self.after}{Fore.RESET}"

        return f"{Fore.LIGHTGREEN_EX}{self.after}{Fore.RESET}"

    @cached_property
    def formatted_before(self) -> str:
        if not self.before:
            return ""

        if self.change_type == ChangeType.delete:
            b = "".join([f"{c}\u0336" for c in self.before])
            return f"{Fore.LIGHTRED_EX}{b}{Fore.RESET}"

        if self.change_type == ChangeType.modify:
            return f"{Fore.LIGHTYELLOW_EX}{self.before}{Fore.RESET}"

        return f"{Fore.LIGHTGREEN_EX}{self.before}{Fore.RESET}"
