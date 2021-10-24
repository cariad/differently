from typing import Any

from pytest import mark

from differently import ChangeType, StringDifferently


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
    assert repr(StringDifferently("foo", "bar")) == "foo > bar"


@mark.parametrize(
    "change, expect",
    [
        (StringDifferently("foo", "foo"), ChangeType.none),
        (StringDifferently("foo", None), ChangeType.delete),
        (StringDifferently(None, "foo"), ChangeType.insert),
        (StringDifferently("foo", "bar"), ChangeType.replace),
    ],
)
def test_change_type(change: StringDifferently, expect: ChangeType) -> None:
    assert change.change == expect
