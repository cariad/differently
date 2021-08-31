from difflib import Differ
from functools import cached_property
from typing import List

from colorama import Fore

from differently.change import Change
from differently.change_type import ChangeType
from differently.line import Line


class ListDifferently:
    def __init__(self, a: List[str], b: List[str]) -> None:
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        longest_a = max([len(ch.before or "") for ch in self.line_changes])
        wip = ""
        for change in self.line_changes:
            pad = " " * (longest_a - len(change.before or ""))

            if change.change_type == ChangeType.modify:
                arrow = f"{Fore.LIGHTYELLOW_EX}>{Fore.RESET}"
            elif change.change_type == ChangeType.delete:
                arrow = f"{Fore.LIGHTRED_EX}x{Fore.RESET}"
            else:
                arrow = ">"

            after = change.formatted_after or ""
            wip = f"{wip}{change.formatted_before}{pad} {arrow} {after}\n"
        return wip.rstrip()

    @cached_property
    def line_changes(self) -> List[Change]:
        lines = list(Differ().compare(self.a, self.b))
        changes: List[Change] = []
        skip = 0

        for index, diff_line in enumerate(lines):
            if skip > 0:
                skip -= 1
                continue

            this = Line(diff_line)
            next = Line(lines[index + 1]) if index <= len(lines) - 2 else None
            jump = Line(lines[index + 2]) if index <= len(lines) - 3 else None

            if this.change_type == ChangeType.delete:
                # If the next line is an addition then consider this a change:
                if next and next.change_type == ChangeType.insert:
                    changes.append(Change(this.text, next.text))
                    skip = 1
                elif (
                    next
                    and next.change_type == ChangeType.modify
                    and jump
                    and jump.change_type == ChangeType.insert
                ):
                    changes.append(Change(this.text, jump.text))
                    skip = 3
                else:
                    changes.append(Change(this.text, None))

            elif this.change_type == ChangeType.insert:
                # If the next line is a deletion then consider this a change:
                if next and next.change_type == ChangeType.delete:
                    changes.append(Change(next.text, this.text))
                    skip = 1
                else:
                    changes.append(Change(None, this.text))

            else:
                changes.append(Change(this.text, this.text))

        return changes
