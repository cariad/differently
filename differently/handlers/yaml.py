from pathlib import Path
from typing import Generic, List, Union, cast

from yaml import safe_dump, safe_load

from differently.exceptions import DeserializationError
from differently.handlers.list import ListDifferently
from differently.types import TComparable


class YamlDifferently(ListDifferently, Generic[TComparable]):
    """
     `YamlDifferently` visualises the differences between dictionaries as YAML.

    ```python
    from differently import YamlDifferently
    from typing import List, TypedDict

    class PersonDict(TypedDict):
        name: str
        movies: List[str]

    a: PersonDict = {
    "name": "Danny Jam",
    "movies": ["Oh, What a Lovely Implosion!", "Touch It and Die", "Mice! Mice! Mice!"],
    }

    b: PersonDict = {
    "name": "Sandy Jelly",
    "movies": ["Oh, What a Lovely Explosion!", "Mice! Mice! Mice!"],
    }

    diff = YamlDifferently(a, b)

    print(diff)
    ```

    ```text
    movies:                         =  movies:
    - Oh, What a Lovely Implosion!  ~  - Oh, What a Lovely Explosion!
    - Touch It and Die              x
    - Mice! Mice! Mice!             =  - Mice! Mice! Mice!
    name: Danny Jam                 ~  name: Sandy Jelly
    ```

    Visualises differences as YAML."""

    def __init__(
        self,
        a: TComparable,
        b: TComparable,
        color: bool = True,
    ) -> None:
        super().__init__(
            self.to_strings(a),
            self.to_strings(b),
            color=color,
        )

    @staticmethod
    def load(i: Union[Path, str]) -> TComparable:
        """
        If `i` is a `Path` then deserialises the file at that location as YAML.

        If `i` is a `str` then deserialises `i` as YAML.

        Raises `DeserializationError` if deserialisation fails.
        """

        try:
            if isinstance(i, str):
                return cast(TComparable, safe_load(i))
            with open(i, "r") as f:
                return cast(TComparable, safe_load(f))
        except Exception as ex:
            raise DeserializationError(ex)

    @staticmethod
    def to_strings(d: TComparable) -> List[str]:
        return str(safe_dump(d, sort_keys=True)).splitlines()
