from pathlib import Path
from typing import Any, Union

from pytest import mark, raises

from differently import YamlDifferently
from differently.exceptions import DeserializationError


def test() -> None:
    diff = YamlDifferently(
        {"foo": "boo"},
        {"foo": "woo"},
        color=True,
    )
    expect = "\x1b[33mfoo: boo\x1b[39m  \x1b[33m~\x1b[39m  \x1b[33mfoo: woo\x1b[39m\n"
    assert str(diff) == expect


@mark.parametrize(
    "i, expect",
    [
        (Path() / "tests" / "foo.yml", {"foo": "bar"}),
        ('{"foo": "bar"}', {"foo": "bar"}),
    ],
)
def test_load(i: Union[Path, str], expect: Any) -> None:
    assert YamlDifferently.load(i) == expect


def test_load__fail() -> None:
    with raises(DeserializationError):
        YamlDifferently.load('{"foo')
