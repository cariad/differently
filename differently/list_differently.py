from difflib import Differ
from io import StringIO
from logging import getLogger
from typing import IO, List, Optional

from differently.difference_type import DifferenceType
from differently.exceptions import DifferentlyError
from differently.string_differently import StringDifferently


class ListDifferently:
    """
    Visualises the differences between two lists of strings.

    Use the string representation or :meth:`.render` to render.

    Arguments:
        a:     First list
        b:     Second list
        color: Include or exclude colour formatting (default is `True`)

    Example:
        .. testcode::

            from differently import ListDifferently

            diff = ListDifferently(
                [
                    "It was the best of times,",
                    "It was the burst of times.",
                ],
                [
                    "It was the best of times,",
                    "It was the worst of times.",
                    "It was the age of wisdom...",
                ],
                color=False,
            )

            print(diff)

    .. testoutput::
        :options: +NORMALIZE_WHITESPACE

        It was the best of times,   =  It was the best of times,
        It was the burst of times.  ~  It was the worst of times.
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
        self._changes: List[StringDifferently] = []
        self._diff: List[str] = []

    def __repr__(self) -> str:
        o = StringIO()
        self.render(o)
        return o.getvalue()

    def _append(self, a: Optional[str], b: Optional[str]) -> None:
        self._changes.append(StringDifferently(a, b, color=self.color))

    def _get_change_type_at(self, index: int) -> Optional[DifferenceType]:
        try:
            line = self._diff[index]
        except IndexError:
            # We do legitimately try to look-ahead beyond the end of the list,
            # so it's okay to fail silently.
            return None

        if line[0] == " ":
            return DifferenceType.NONE
        if line[0] == "+":
            return DifferenceType.INSERTION
        if line[0] == "-":
            return DifferenceType.DELETION
        if line[0] == "?":
            return DifferenceType.REPLACEMENT
        raise DifferentlyError(f'unrecognised change type "{line[0]}" in "{line}"')

    def _get_text_at(self, index: int) -> Optional[str]:
        try:
            return self._diff[index][2:]
        except IndexError:
            # We do legitimately try to look-ahead beyond the end of the list,
            # so it's okay to fail silently.
            return None

    @property
    def differences(self) -> List[StringDifferently]:
        """
        Gets the :class:`.StringDifferently` that make up the differences
        between the lists.
        """

        if not self._changes:
            log = getLogger("differently.ListDifferently")
            log.debug("Calculating differences")

            self._diff = list(Differ().compare(self.a, self.b))

            log.debug("Differ: %s", self._diff)

            skip = 0

            for index in range(len(self._diff)):
                if skip > 0:
                    log.debug("Skipping line %s", index)
                    skip -= 1
                    continue

                this_action = self._get_change_type_at(index)

                if this_action == DifferenceType.REPLACEMENT:
                    log.debug("Skipping instruction to replace")
                    continue

                this_text = self._get_text_at(index)

                next_action = self._get_change_type_at(index + 1)
                next_text = self._get_text_at(index + 1)

                if this_action == DifferenceType.DELETION:
                    log.debug("This is a deletion")

                    jump_action = self._get_change_type_at(index + 2)
                    jump_text = self._get_text_at(index + 2)

                    # If the next line is an addition then consider this a change:
                    if next_action == DifferenceType.INSERTION:
                        self._append(this_text, next_text)
                        skip = 1
                    elif (
                        next_action == DifferenceType.REPLACEMENT
                        and jump_action == DifferenceType.INSERTION
                    ):
                        self._append(this_text, jump_text)
                        skip = 2
                    else:
                        self._append(this_text, None)

                elif this_action == DifferenceType.INSERTION:
                    # If the next line is a deletion then consider this a change:
                    if next_action == DifferenceType.DELETION:
                        self._append(next_text, this_text)
                        skip = 1
                    else:
                        self._append(None, this_text)

                else:
                    self._append(this_text, this_text)

        return self._changes

    def render(self, writer: IO[str]) -> None:
        """
        Renders the visualisation to `writer`.

        Arguments:
            writer: Writer

        Example:
            .. testcode::

                from io import StringIO
                from differently import ListDifferently

                diff = ListDifferently(
                    ["first", "seccond"],
                    ["first", "second", "third"],
                    color=False,
                )

                writer = StringIO()
                diff.render(writer)
                print(writer.getvalue())

        .. testoutput::
            :options: +NORMALIZE_WHITESPACE

            first    =  first
            seccond  ~  second
                     >  third
        """

        longest_a = max([len(ch.a or "") for ch in self.differences])

        for change in self.differences:
            change.render(lhs_width=longest_a, writer=writer)
            writer.write("\n")
