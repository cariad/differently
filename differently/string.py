"""
Supports the description of changes to strings.
"""

from typing import IO, Any, Optional

from ansiscape import green, red, yellow

from differently.change_type import ChangeType


class StringDifferently:
    """
    Describes a change to a string.

    Args:
        before: Initial
        after: Updated
    """

    def __init__(
        self,
        before: Optional[str],
        after: Optional[str],
        color: bool = True,
    ) -> None:
        """Set the string's `before` and `after` values."""
        self._after = after
        self._before = before
        self.color = color

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StringDifferently):
            return False
        return self.before == other.before and self.after == other.after

    def __repr__(self) -> str:
        return f"{self.before or '<None>'} > {self.after or '<None>'}"

    @property
    def after(self) -> Optional[str]:
        """Gets the string's updated value."""
        return self._after

    @property
    def before(self) -> Optional[str]:
        """Gets the string's initial value."""
        return self._before

    def render_a(self, writer: IO[str]) -> None:
        if self.before is None:
            return

        if self.color:
            if self.change == ChangeType.delete:
                writer.write(red(self.before).encoded)
                return

            if self.change == ChangeType.replace:
                writer.write(yellow(self.before).encoded)
                return

            if self.change == ChangeType.none:
                writer.write(green(self.before).encoded)
                return

        writer.write(self.before)

    def render_b(self, writer: IO[str]) -> None:
        if self.after is None:
            return

        if self.color:
            if self.change in [ChangeType.insert, ChangeType.replace]:
                writer.write(yellow(self.after).encoded)
                return

            if self.change == ChangeType.none:
                writer.write(green(self.after).encoded)
                return

        writer.write(self.after)

    @property
    def arrow(self) -> str:
        if self.change == ChangeType.insert:
            return ">"
        if self.change == ChangeType.replace:
            return "~"
        if self.change == ChangeType.delete:
            return "x"
        return "="

    def render_arrow(self, writer: IO[str]) -> None:
        if self.color:
            if self.change == ChangeType.insert:
                writer.write(yellow(self.arrow).encoded)
                return

            if self.change == ChangeType.replace:
                writer.write(yellow(self.arrow).encoded)
                return

            if self.change == ChangeType.delete:
                writer.write(red(self.arrow).encoded)
                return

            if self.change == ChangeType.none:
                writer.write(green(self.arrow).encoded)
                return

        writer.write(self.arrow)

    def render(self, lhs_width: int, writer: IO[str]) -> None:
        self.render_a(writer)
        writer.write(" " * (lhs_width - len(self.before or "")))
        writer.write("  ")
        self.render_arrow(writer)
        writer.write("  ")
        self.render_b(writer)
        writer.write("\n")

    @property
    def change(self) -> ChangeType:
        """Gets the type of change."""
        if self.before == self.after:
            return ChangeType.none
        if self.before is None:
            return ChangeType.insert
        if self.after is None:
            return ChangeType.delete
        return ChangeType.replace
