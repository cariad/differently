from typing import Any

# from colorama import Fore
from pytest import mark

from differently.change import Change
from differently.change_type import ChangeType


@mark.parametrize(
    "a, b, expect",
    [
        (Change("foo", "foo"), Change("foo", "foo"), True),
        (Change("foo", "foo"), Change("bar", "foo"), False),
        (Change("foo", "foo"), Change("foo", "bar"), False),
        (Change("foo", "foo"), "foo", False),
    ],
)
def test_eq(a: Change, b: Any, expect: bool) -> None:
    assert (a == b) == expect


def test_repr() -> None:
    assert repr(Change("foo", "bar")) == "foo > bar"


@mark.parametrize(
    "change, expect",
    [
        (Change("foo", "foo"), ChangeType.none),
        (Change("foo", None), ChangeType.delete),
        (Change(None, "foo"), ChangeType.insert),
        (Change("foo", "bar"), ChangeType.replace),
    ],
)
def test_change_type(change: Change, expect: ChangeType) -> None:
    assert change.change_type == expect
