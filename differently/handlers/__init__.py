from pathlib import Path
from typing import Any, Callable, Dict, List, Type

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


def get_deserializer_keys() -> List[str]:
    """Gets the keys of all available deserialisers."""
    return [key for key in loaders]


def get_renderer(key: str) -> Type[ListDifferently]:
    """Gets a renderer."""
    return renderers[key]


def get_renderer_keys() -> List[str]:
    """Gets the keys of all available renderers."""
    return [key for key in renderers]


__all__ = [
    "JsonDifferently",
    "ListDifferently",
    "TextDifferently",
    "YamlDifferently",
]
