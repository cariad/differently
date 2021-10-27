"""
Supports the description of changes to strings.
"""

from io import StringIO
from typing import IO, Any, Optional

from ansiscape import green, red, yellow

from differently.change_type import DifferenceType


class StringDifferently:
    """
    Visualises the differences between two strings.

    Call `str(...)` or :meth:`.render` to render.

    Arguments:
        a:     First string
        b:     Second string
        color: Include or exclude colour formatting (default is `True`)

    Example:
        .. testcode::

            from differently import StringDifferently

            print(StringDifferently("worst of times", "worst of times", color=False))
            print(StringDifferently("borst of times", "worst of times", color=False))
            print(StringDifferently(None, "worst of times", color=False))
            print(StringDifferently("borst of times", None, color=False))

    .. testoutput::

        worst of times  =  worst of times
        borst of times  ~  worst of times
          >  worst of times
        borst of times  x
    """

    def __init__(
        self,
        a: Optional[str],
        b: Optional[str],
        color: bool = True,
    ) -> None:

        self._a = a
        self._b = b
        self.color = color

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StringDifferently):
            return False
        return self.a == other.a and self.b == other.b

    def __repr__(self) -> str:
        writer = StringIO()
        self.render(lhs_width=0, writer=writer)
        return writer.getvalue().rstrip()

    @property
    def a(self) -> Optional[str]:
        """
        Gets the first string.

        Example:
            .. testcode::

                from differently import StringDifferently

                diff = StringDifferently(
                    "It was the blorst of times.",
                    "It was the worst of times.",
                    color=False,
                )

                print(diff.a)

        .. testoutput::

            It was the blorst of times.
        """

        return self._a

    @property
    def arrow(self) -> str:
        """
        Gets the arrow character that describes the difference.

        Example:
            .. testcode::

                from differently import StringDifferently

                equal = StringDifferently("0", "0", color=False)
                print(equal.a, equal.b, equal.arrow)

                replace = StringDifferently("0", "1", color=False)
                print(replace.a, replace.b, replace.arrow)

                insert = StringDifferently(None, "1", color=False)
                print(insert.a, insert.b, insert.arrow)

                delete = StringDifferently("0", None, color=False)
                print(delete.a, delete.b, delete.arrow)

        .. testoutput::

            0 0 =
            0 1 ~
            None 1 >
            0 None x
        """

        if self.type == DifferenceType.INSERTION:
            return ">"
        if self.type == DifferenceType.REPLACEMENT:
            return "~"
        if self.type == DifferenceType.DELETION:
            return "x"
        return "="

    @property
    def b(self) -> Optional[str]:
        """
        Gets the second string.

        Example:
            .. testcode::

                from differently import StringDifferently

                diff = StringDifferently(
                    "It was the blorst of times.",
                    "It was the worst of times.",
                    color=False,
                )

                print(diff.b)

        .. testoutput::

            It was the worst of times.
        """

        return self._b

    def _render_a(self, writer: IO[str]) -> None:
        if self.a is None:
            return

        if self.color:
            if self.type == DifferenceType.DELETION:
                writer.write(red(self.a).encoded)
                return

            if self.type == DifferenceType.REPLACEMENT:
                writer.write(yellow(self.a).encoded)
                return

            if self.type == DifferenceType.NONE:
                writer.write(green(self.a).encoded)
                return

        writer.write(self.a)

    def _render_arrow(self, writer: IO[str]) -> None:
        if self.color:
            if self.type == DifferenceType.INSERTION:
                writer.write(yellow(self.arrow).encoded)
                return

            if self.type == DifferenceType.REPLACEMENT:
                writer.write(yellow(self.arrow).encoded)
                return

            if self.type == DifferenceType.DELETION:
                writer.write(red(self.arrow).encoded)
                return

            if self.type == DifferenceType.NONE:
                writer.write(green(self.arrow).encoded)
                return

        writer.write(self.arrow)

    def _render_b(self, writer: IO[str]) -> None:
        if self.b is None:
            return

        if self.color:
            if self.type in [DifferenceType.INSERTION, DifferenceType.REPLACEMENT]:
                writer.write(yellow(self.b).encoded)
                return

            if self.type == DifferenceType.NONE:
                writer.write(green(self.b).encoded)
                return

        writer.write(self.b)


    def render(self, lhs_width: int, writer: IO[str]) -> None:
        """
        Renders the visualisation to `writer`.

        Arguments:
            lhs_width: Width to pad the left-hand side
            writer:    Writer

        Example:
            .. testcode::

                from io import StringIO
                from differently import StringDifferently

                diff = StringDifferently(
                    "It was the blorst of times.",
                    "It was the worst of times.",
                    color=False,
                )

                writer = StringIO()
                diff.render(lhs_width=27, writer=writer)
                print(writer.getvalue())

        .. testoutput::

            It was the blorst of times.  ~  It was the worst of times.
        """

        self._render_a(writer)
        writer.write(" " * (lhs_width - len(self.a or "")))
        writer.write("  ")
        self._render_arrow(writer)
        writer.write("  ")
        self._render_b(writer)

    @property
    def type(self) -> DifferenceType:
        """
        Gets the type of the difference.

        Example:
            .. testcode::

                from differently import StringDifferently

                print(StringDifferently("worst of times", "worst of times", color=False).type)
                print(StringDifferently("borst of times", "worst of times", color=False).type)
                print(StringDifferently(None, "worst of times", color=False).type)
                print(StringDifferently("borst of times", None, color=False).type)

            .. testoutput::

                DifferenceType.NONE
                DifferenceType.REPLACEMENT
                DifferenceType.INSERTION
                DifferenceType.DELETION
        """


        if self.a == self.b:
            return DifferenceType.NONE
        if self.a is None:
            return DifferenceType.INSERTION
        if self.b is None:
            return DifferenceType.DELETION
        return DifferenceType.REPLACEMENT
