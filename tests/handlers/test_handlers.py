from pathlib import Path
from typing import Any, Type

from pytest import mark

from differently.handlers import (
    JsonDifferently,
    ListDifferently,
    TextDifferently,
    YamlDifferently,
    deserialize,
    get_deserializer_keys,
    get_renderer,
    get_renderer_keys,
)

tests = Path() / "tests"


@mark.parametrize(
    "arg, index, path, expect",
    [
        ("json", 0, tests / "foo.json", {"foo": "bar"}),
        ("text", 0, tests / "foo.txt", "foo\n"),
        ("yaml", 0, tests / "foo.yml", {"foo": "bar"}),
        ("json,yaml", 0, tests / "foo.json", {"foo": "bar"}),
        ("json,yaml", 1, tests / "foo.yml", {"foo": "bar"}),
    ],
)
def test_load_file(arg: str, index: int, path: Path, expect: Any) -> None:
    assert deserialize(keys=arg, index=index, path=path) == expect


def test_get_loader_keys() -> None:
    assert get_deserializer_keys() == ["json", "text", "yaml"]


@mark.parametrize(
    "key, expect",
    [
        ("json", JsonDifferently),
        ("text", TextDifferently),
        ("yaml", YamlDifferently),
    ],
)
def test_get_renderer(key: str, expect: Type[ListDifferently]) -> None:
    assert get_renderer(key) is expect


def test_get_renderer_keys() -> None:
    assert get_renderer_keys() == ["json", "text", "yaml"]
