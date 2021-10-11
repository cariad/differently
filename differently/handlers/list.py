from typing import List

from differently.change_calculator import ChangeCalculator
from differently.renderers.table import TableRenderer


class ListDifferently:
    """Visualises differences between lists of strings."""

    def __init__(self, a: List[str], b: List[str]) -> None:
        self.calculator = ChangeCalculator(a, b)

    def __repr__(self) -> str:
        return TableRenderer(self.calculator.changes).table
