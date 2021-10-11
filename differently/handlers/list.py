from typing import List, Optional

from differently.change_calculator import ChangeCalculator
from differently.renderers.table import TableRenderer


class ListDifferently:
    """Visualises differences between lists of strings."""

    def __init__(
        self,
        a: List[str],
        b: List[str],
        color: Optional[bool] = None,
    ) -> None:
        self.calculator = ChangeCalculator(a, b)
        self.color = color

    def __repr__(self) -> str:
        renderer = TableRenderer(
            changes=self.calculator.changes,
            color=self.color,
        )
        return renderer.table
