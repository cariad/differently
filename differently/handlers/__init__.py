""" Handlers. """

from pathlib import Path
from typing import IO, Any, Callable, Dict, List, Tuple, Type

from differently.exceptions import DeserializationError
from differently.handlers.json import JsonDifferently
from differently.handlers.list import ListDifferently
from differently.handlers.text import TextDifferently
from differently.handlers.yaml import YamlDifferently

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
    return loaders[key](path)


def deserialize_value(v: str) -> Tuple[Type[ListDifferently], Any]:
    """
    Attempts to deserialise `v`.

    Returns the deserialiser and the deserialised value.
    """

    try:
        return YamlDifferently[Any], YamlDifferently.load(v)
    except DeserializationError:
        pass

    try:
        return JsonDifferently[Any], JsonDifferently.load(v)
    except DeserializationError:
        pass

    return TextDifferently, v


def get_deserializer_keys() -> List[str]:
    """Gets the keys of all available deserialisers."""
    return [key for key in loaders]


def get_renderer(key: str) -> Type[ListDifferently]:
    """Gets a renderer."""
    return renderers[key]


def get_renderer_keys() -> List[str]:
    """Gets the keys of all available renderers."""
    return [key for key in renderers]


def render(a: str, b: str, writer: IO[str]) -> None:
    """
    Renders the differences between `a` and `b` to `writer`.

    Treats the inputs as marked-up data if possible.
    """

    _, da = deserialize_value(a)
    t, db = deserialize_value(b)
    writer.write(str(t(da, db)))


__all__ = [
    "JsonDifferently",
    "ListDifferently",
    "TextDifferently",
    "YamlDifferently",
]
