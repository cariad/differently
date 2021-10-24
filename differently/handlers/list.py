from difflib import Differ
from io import StringIO
from typing import IO, List, Optional

from differently.change_type import ChangeType
from differently.string import StringDifferently


class ListDifferently:
    """
    Visualises the differences between two lists of strings.

    Arguments:
        a:     First list
        b:     Second list
        color: Include (`True`) or exclude (`False`) colour formatting
               (default is `True`)

    Example:
        .. testcode::

            from differently import ListDifferently

            diff = ListDifferently(
                a=[
                    "It was the best of times,",
                    "It was the blorst of times.",
                ],
                b=[
                    "It was the best of times,",
                    "It was the worst of times.",
                    "It was the age of wisdom...",
                ],
                color=False,
            )

            print(diff)

    .. testoutput::
        :options: +NORMALIZE_WHITESPACE

        It was the best of times,    =  It was the best of times,
        It was the blorst of times.  ~  It was the worst of times.
                                     >  It was the age of wisdom...
    """

    def __init__(
        self,
        a: List[str],
        b: List[str],
        color: bool = True,
    ) -> None:
        self.a = a
        self.b = b
        self.color = color
        self._diff: List[str] = []
        self._changes: List[StringDifferently] = []

    def __repr__(self) -> str:
        o = StringIO()
        self.render(o)
        return o.getvalue()

    def render(self, writer: IO[str]) -> None:
        if not self.changes:
            return

        longest_a = max([len(ch.before or "") for ch in self.changes])

        for change in self.changes:
            change.render(lhs_width=longest_a, writer=writer)

    def _get_change_type_at(self, index: int) -> Optional[ChangeType]:
        try:
            line = self._diff[index]
        except IndexError:
            # We do legitimately try to look-ahead beyond the end of the list,
            # so it's okay to fail silently.
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

    def _get_text_at(self, index: int) -> Optional[str]:
        try:
            return self._diff[index][2:]
        except IndexError:
            # We do legitimately try to look-ahead beyond the end of the list,
            # so it's okay to fail silently.
            return None

    def _append(self, a: Optional[str], b: Optional[str]) -> None:
        self._changes.append(StringDifferently(a, b, color=self.color))

    @property
    def changes(self) -> List[StringDifferently]:
        # """
        # Gets the changes.

        # For example:

        # from differently.calculation import Calculator

        # calc = Calculator(
        #     [
        #         "It was the best of times, it was the blorst of times.",
        #     ],
        #     [
        #         "It was the best of times, it was the worst of times.",
        #         "It was the age of wisdom, it was the age of foolishness",
        #     ],
        # )

        # for line, change in enumerate(calc.changes):
        #     print(f"line {line}: before={change.before or ''}")
        #     print(f"line {line}: after={change.after or ''}")
        #     print(f"line {line}: type={change.type}")

        # line 0: before=It was the best of times, it was the blorst of times.
        # line 0: after=It was the best of times, it was the worst of times.
        # line 0: type=ChangeType.replace
        # line 1: before=
        # line 1: after=It was the age of wisdom, it was the age of foolishness
        # line 1: type=ChangeType.insert
        # """

        if self._changes is None:
            self._diff = list(Differ().compare(self.a, self.b))
            skip = 0

            for index in range(len(self._diff)):
                if skip > 0:
                    skip -= 1
                    continue

                this_action = self._get_change_type_at(index)

                if this_action == ChangeType.replace:
                    continue

                this_text = self._get_text_at(index)

                next_action = self._get_change_type_at(index + 1)
                next_text = self._get_text_at(index + 1)

                if this_action == ChangeType.delete:

                    jump_action = self._get_change_type_at(index + 2)
                    jump_text = self._get_text_at(index + 2)

                    # If the next line is an addition then consider this a change:
                    if next_action == ChangeType.insert:
                        self._append(this_text, next_text)
                        skip = 1
                    elif (
                        next_action == ChangeType.replace
                        and jump_action == ChangeType.insert
                    ):
                        self._append(this_text, jump_text)
                        skip = 3
                    else:
                        self._append(this_text, None)

                elif this_action == ChangeType.insert:
                    # If the next line is a deletion then consider this a change:
                    if next_action == ChangeType.delete:
                        self._append(next_text, this_text)
                        skip = 1
                    else:
                        self._append(None, this_text)

                else:
                    self._append(this_text, this_text)

        return self._changes
