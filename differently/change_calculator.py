from difflib import Differ
from functools import cached_property
from typing import List, Optional

from differently.change import Change
from differently.change_type import ChangeType


class ChangeCalculator:
    def __init__(self, a: List[str], b: List[str]) -> None:
        self.a = a
        self.b = b

    @cached_property
    def diff(self) -> List[str]:
        return list(Differ().compare(self.a, self.b))

    def diff_line(self, index: int) -> Optional[str]:
        try:
            return self.diff[index]
        except IndexError:
            # We do legitimately try to look-ahead beyond the end of the list,
            # so it's okay to fail silently.
            return None

    def change_type(self, index: int) -> Optional[ChangeType]:
        line = self.diff_line(index)
        if not line:
            return None
        if line[0] == " ":
            return ChangeType.none
        if line[0] == "+":
            return ChangeType.insert
        if line[0] == "-":
            return ChangeType.delete
        if line[0] == "?":
            return ChangeType.replace
        raise ValueError(f'unrecognised change type "{line[0]}" in "{line}"')

    def text(self, index: int) -> Optional[str]:
        line = self.diff_line(index)
        return line[2:] if line else None

    @cached_property
    def changes(self) -> List[Change]:
        changes: List[Change] = []
        skip = 0

        for index in range(len(self.diff)):
            if skip > 0:
                skip -= 1
                continue

            this_action = self.change_type(index)

            if this_action == ChangeType.replace:
                continue

            this_text = self.text(index)

            next_action = self.change_type(index + 1)
            next_text = self.text(index + 1)

            if this_action == ChangeType.delete:

                jump_action = self.change_type(index + 2)
                jump_text = self.text(index + 2)

                # If the next line is an addition then consider this a change:
                if next_action == ChangeType.insert:
                    changes.append(Change(this_text, next_text))
                    skip = 1
                elif (
                    next_action == ChangeType.replace
                    and jump_action == ChangeType.insert
                ):
                    changes.append(Change(this_text, jump_text))
                    skip = 3
                else:
                    changes.append(Change(this_text, None))

            elif this_action == ChangeType.insert:
                # If the next line is a deletion then consider this a change:
                if next_action == ChangeType.delete:
                    changes.append(Change(next_text, this_text))
                    skip = 1
                else:
                    changes.append(Change(None, this_text))

            else:
                changes.append(Change(this_text, this_text))

        return changes
