from pathlib import Path

from differently.handlers.list import ListDifferently


class TextDifferently(ListDifferently):
    """Visualises differences between strings."""

    def __init__(self, a: str, b: str) -> None:
        super().__init__(a.splitlines(), b.splitlines())

    @staticmethod
    def load(path: Path) -> str:
        with open(path, "r") as f:
            return f.read()
