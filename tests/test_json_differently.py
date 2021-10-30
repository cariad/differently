from pathlib import Path
from typing import Any, Union

from pytest import mark, raises

from differently import JsonDifferently
from differently.exceptions import DeserializationError


@mark.parametrize(
    "a, b, expect",
    [
        (
            None,
            {"foo": "bar"},
            """  >  {
  >    "foo": "bar"
  >  }
""",
        ),
        (
            {"foo": "bar"},
            None,
            """{               x
  "foo": "bar"  x
}               x
""",
        ),
    ],
)
def test(a: Any, b: Any, expect: str) -> None:
    assert str(JsonDifferently(a, b, color=False)) == expect


@mark.parametrize(
    "i, expect",
    [
        (Path() / "tests" / "foo.json", {"foo": "bar"}),
        ('{"foo": "bar"}', {"foo": "bar"}),
    ],
)
def test_load(i: Union[Path, str], expect: Any) -> None:
    assert JsonDifferently.load(i) == expect


def test_load__fail() -> None:
    with raises(DeserializationError):
        JsonDifferently.load("foo:\nfoo:")
