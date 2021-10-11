from pathlib import Path
from typing import Generic, List, cast

from yaml import safe_dump, safe_load

from differently.handlers.list import ListDifferently
from differently.types import TComparable


class YamlDifferently(ListDifferently, Generic[TComparable]):
    """Visualises differences as YAML."""

    def __init__(self, a: TComparable, b: TComparable) -> None:
        super().__init__(self.to_strings(a), self.to_strings(b))

    @staticmethod
    def load(path: Path) -> TComparable:
        with open(path, "r") as f:
            return cast(TComparable, safe_load(f))

    @staticmethod
    def to_strings(d: TComparable) -> List[str]:
        return str(safe_dump(d, sort_keys=True)).splitlines()
