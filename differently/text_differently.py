from pathlib import Path

from differently.list_differently import ListDifferently


class TextDifferently(ListDifferently):
    """
    Visualises the differences between two bodies of text.

    Use the string representation or inherited :meth:`ListDifferently.render` to
    render.

    Arguments:
        a:     First body
        b:     Second body
        color: Include or exclude colour formatting (default is `True`)

    Example:
        .. testcode::

            from differently import TextDifferently

            diff = TextDifferently(
                "It was the best of times,\\nIt was the burst of times.",
                "It was the best of times,\\nIt was the worst of times.",
                color=False,
            )

            print(diff)

    .. testoutput::
        :options: +NORMALIZE_WHITESPACE

        It was the best of times,   =  It was the best of times,
        It was the burst of times.  ~  It was the worst of times.
    """

    def __init__(
        self,
        a: str,
        b: str,
        color: bool = True,
    ) -> None:
        super().__init__(
            a.splitlines(),
            b.splitlines(),
            color=color,
        )

    @staticmethod
    def load(path: Path) -> str:
        """
        Gets the body of the text file at `path`.

        Arguments:
            path: Path to text file

        Returns:
            Body
        """

        with open(path, "r") as f:
            return f.read()
