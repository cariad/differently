from json import dumps, load, loads
from pathlib import Path
from typing import Generic, List, Union, cast

from differently.exceptions import DeserializationError
from differently.handlers.list import ListDifferently
from differently.types import TComparable


class JsonDifferently(ListDifferently, Generic[TComparable]):
    """
     `JsonDifferently` visualises the differences between dictionaries as JSON.

    ```python
    from differently import JsonDifferently
    from typing import List, TypedDict

    class PersonDict(TypedDict):
        name: str
        movies: List[str]

    a: PersonDict = {
    "name": "Bobby Pringles",
    "movies": ["Fire Everywhere", "The World Is Exploding"],
    }

    b: PersonDict = {
    "name": "Susan Cheddar",
    "movies": ["The World Is Exploding", "Watch Out For The Moon"],
    }

    diff = JsonDifferently(a, b)

    print(diff)
    ```

    ```text
    {                             =  {
    "movies": [                 =    "movies": [
        "Fire Everywhere",        x
        "The World Is Exploding"  ~      "The World Is Exploding",
                                >      "Watch Out For The Moon"
    ],                          =    ],
    "name": "Bobby Pringles"    ~    "name": "Susan Cheddar"
    }                             =  }
    ```


    Visualises differences as JSON."""

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
        If `i` is a `Path` then deserialises the file at that location as JSON.

        If `i` is a `str` then deserialises `i` as JSON.

        Raises `DeserializationError` if deserialisation fails.
        """

        try:
            if isinstance(i, str):
                return cast(TComparable, loads(i))
            with open(i, "r") as f:
                return cast(TComparable, load(f))
        except Exception as ex:
            raise DeserializationError(ex)

    @staticmethod
    def to_strings(d: TComparable) -> List[str]:
        return str(dumps(d, indent=2, sort_keys=True)).splitlines()
