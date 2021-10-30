from pathlib import Path
from typing import Any, List, Optional, Union

from yaml import safe_dump, safe_load

from differently.exceptions import DeserializationError
from differently.list_differently import ListDifferently


class YamlDifferently(ListDifferently):
    """
    Visualises the differences between two objects as YAML.

    Use the string representation or inherited :meth:`ListDifferently.render` to
    render.

    Arguments:
        a:     First object
        b:     Second object
        color: Include or exclude colour formatting (default is `True`)

    Example:
        .. testcode::

            from differently import YamlDifferently
            from typing import List, TypedDict

            class PersonDict(TypedDict):
                name: str
                movies: List[str]

            a: PersonDict = {
                "name": "Danny Jam",
                "movies": [
                    "Oh, What a Lovely Implosion!",
                    "Touch It and Die",
                    "Mice! Mice! Mice!",
                ],
            }

            b: PersonDict = {
                "name": "Sandy Jelly",
                "movies": [
                    "Oh, What a Lovely Explosion!",
                    "Mice! Mice! Mice!",
                ],
            }

            diff = YamlDifferently(a, b, color=False)
            print(diff)

    .. testoutput::
        :options: +NORMALIZE_WHITESPACE

        movies:                         =  movies:
        - Oh, What a Lovely Implosion!  ~  - Oh, What a Lovely Explosion!
        - Touch It and Die              x
        - Mice! Mice! Mice!             =  - Mice! Mice! Mice!
        name: Danny Jam                 ~  name: Sandy Jelly
    """

    def __init__(
        self,
        a: Optional[Any],
        b: Optional[Any],
        color: bool = True,
    ) -> None:
        super().__init__(
            self.to_strings(a),
            self.to_strings(b),
            color=color,
        )

    @staticmethod
    def load(i: Union[Path, str]) -> Any:
        """
        If `i` is a `Path` then deserialises the file at that location as YAML.

        If `i` is a `str` then deserialises `i` as YAML.

        Raises `DeserializationError` if deserialisation fails.
        """

        try:
            if isinstance(i, str):
                return safe_load(i)
            with open(i, "r") as f:
                return safe_load(f)
        except Exception as ex:
            raise DeserializationError(ex)

    @staticmethod
    def to_strings(d: Optional[Any]) -> Optional[List[str]]:
        if d is None:
            return None
        return str(safe_dump(d, sort_keys=True)).splitlines()
