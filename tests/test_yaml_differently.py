from pathlib import Path
from typing import Any, Union

from pytest import mark, raises

from differently import YamlDifferently
from differently.exceptions import DeserializationError


@mark.parametrize(
    "a, b, expect",
    [
        (
            None,
            {"foo": "bar"},
            """  >  foo: bar\n""",
        ),
        (
            {"foo": "bar"},
            None,
            "foo: bar  x\n",
        ),
    ],
)
def test(a: Any, b: Any, expect: str) -> None:
    assert str(YamlDifferently(a, b, color=False)) == expect


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
