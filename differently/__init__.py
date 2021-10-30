from pathlib import Path
from typing import IO, Any, Callable, Dict, List, Optional, Type

from differently.deserialization import deserialize_value
from differently.difference_type import DifferenceType
from differently.json_differently import JsonDifferently
from differently.list_differently import ListDifferently
from differently.string_differently import StringDifferently
from differently.text_differently import TextDifferently
from differently.yaml_differently import YamlDifferently

TLoader = Callable[[Path], Any]

loaders: Dict[str, TLoader] = {
    "json": JsonDifferently.load,
    "text": TextDifferently.load,
    "yaml": YamlDifferently.load,
}

renderers: Dict[str, Type[ListDifferently]] = {
    "json": JsonDifferently,
    "text": TextDifferently,
    "yaml": YamlDifferently,
}


def deserialize(keys: str, index: int, path: Path) -> Any:
    """
    Deserialises the file at `path` using the deserialiser described at `index`
    of the comma-separated `keys`.
    """
    key = keys.split(",")[index] if "," in keys else keys
    return loaders[key](Path(path))


def get_deserializer_keys() -> List[str]:
    """Gets the keys of all available deserialisers."""
    return [key for key in loaders]


def get_renderer(key: str) -> Type[ListDifferently]:
    """Gets a renderer."""
    return renderers[key]


def get_renderer_keys() -> List[str]:
    """Gets the keys of all available renderers."""
    return [key for key in renderers]


def render(a: Optional[str], b: Optional[str], writer: IO[str]) -> None:
    """
    Renders the differences between `a` and `b` to `writer`.

    Treats the inputs as marked-up data if possible.
    """

    ta, da = deserialize_value(a)
    tb, db = deserialize_value(b)

    tv = ta or tb

    if not tv:
        # No changes to render:
        return

    writer.write(str(tv(da, db)))


__all__ = [
    "DifferenceType",
    "JsonDifferently",
    "ListDifferently",
    "render",
    "StringDifferently",
    "TextDifferently",
    "YamlDifferently",
]
