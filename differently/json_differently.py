from json import dumps, load, loads
from pathlib import Path
from typing import IO, Any, List, Union

from differently.exceptions import DeserializationError
from differently.list_differently import ListDifferently


class JsonDifferently(ListDifferently):
    """
    Visualises the differences between two objects as JSON.

    Use the string representation or :meth:`.render` to render.

    Arguments:
        a:     First object
        b:     Second object
        color: Include or exclude colour formatting (default is `True`)

    Example:
        .. testcode::

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

            diff = JsonDifferently(a, b, color=False)
            print(diff)

    .. testoutput::
        :options: +NORMALIZE_WHITESPACE

        {                                 =  {
            "movies": [                   =    "movies": [
                "Fire Everywhere",        x
                "The World Is Exploding"  ~      "The World Is Exploding",
                                          >      "Watch Out For The Moon"
            ],                            =    ],
            "name": "Bobby Pringles"      ~    "name": "Susan Cheddar"
        }                                 =  }
    """

    def __init__(
        self,
        a: Any,
        b: Any,
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
        Deserialises JSON.

        Arguments:
            i: If `i` is a `Path` then deserialises the file, If `i` is a `str`
               then deserialises `i`.

        Returns:
            Deserialised object

        Raises:
            :exc:`.DeserializationError`: raised if deserialisation fails
        """

        try:
            if isinstance(i, str):
                return loads(i)
            with open(i, "r") as f:
                return load(f)
        except Exception as ex:
            raise DeserializationError(ex)

    def render(self, writer: IO[str]) -> None:
        """
        Renders the visualisation to `writer`.

        Arguments:
            writer: Writer

        Example:
            .. testcode::

                from differently import JsonDifferently
                from io import StringIO
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

                diff = JsonDifferently(a, b, color=False)

                writer = StringIO()
                diff.render(writer)
                print(writer.getvalue())

            .. testoutput::
                :options: +NORMALIZE_WHITESPACE

                {                                 =  {
                    "movies": [                   =    "movies": [
                        "Fire Everywhere",        x
                        "The World Is Exploding"  ~      "The World Is Exploding",
                                                >      "Watch Out For The Moon"
                    ],                            =    ],
                    "name": "Bobby Pringles"      ~    "name": "Susan Cheddar"
                }                                 =  }
        """

        super().render(writer=writer)

    @staticmethod
    def to_strings(d: Any) -> List[str]:
        return str(dumps(d, indent=2, sort_keys=True)).splitlines()
