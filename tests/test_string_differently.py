from typing import Any

from pytest import mark

from differently import DifferenceType, StringDifferently


@mark.parametrize(
    "a, b, expect",
    [
        (StringDifferently("foo", "foo"), StringDifferently("foo", "foo"), True),
        (StringDifferently("foo", "foo"), StringDifferently("bar", "foo"), False),
        (StringDifferently("foo", "foo"), StringDifferently("foo", "bar"), False),
        (StringDifferently("foo", "foo"), "foo", False),
    ],
)
def test_eq(a: StringDifferently, b: Any, expect: bool) -> None:
    assert (a == b) == expect


def test_repr() -> None:
    assert repr(StringDifferently("foo", "bar")) == "\x1b[33mfoo\x1b[39m  \x1b[33m~\x1b[39m  \x1b[33mbar\x1b[39m"


@mark.parametrize(
    "change, expect",
    [
        (StringDifferently("foo", "foo"), DifferenceType.NONE),
        (StringDifferently("foo", None), DifferenceType.DELETION),
        (StringDifferently(None, "foo"), DifferenceType.INSERTION),
        (StringDifferently("foo", "bar"), DifferenceType.REPLACEMENT),
    ],
)
def test_change_type(change: StringDifferently, expect: DifferenceType) -> None:
    assert change.type == expect
