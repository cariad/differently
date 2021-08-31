from typing import Any

from colorama import Fore
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
        (Change("foo", "bar"), ChangeType.modify),
    ],
)
def test_change_type(change: Change, expect: ChangeType) -> None:
    assert change.change_type == expect


@mark.parametrize(
    "change, expect",
    [
        (Change("foo", None), ""),
        (Change("foo", ""), ""),
        (Change(None, "bar"), f"{Fore.LIGHTYELLOW_EX}bar{Fore.RESET}"),
        (Change("foo", "bar"), f"{Fore.LIGHTYELLOW_EX}bar{Fore.RESET}"),
        (Change("foo", "foo"), f"{Fore.LIGHTGREEN_EX}foo{Fore.RESET}"),
    ],
)
def test_formatted_after(change: Change, expect: str) -> None:
    assert change.formatted_after == expect


@mark.parametrize(
    "change, expect",
    [
        (Change(None, "bar"), ""),
        (Change("", "bar"), ""),
        (Change("foo", None), f"{Fore.LIGHTRED_EX}f\u0336o\u0336o\u0336{Fore.RESET}"),
        (Change("foo", "bar"), f"{Fore.LIGHTYELLOW_EX}foo{Fore.RESET}"),
        (Change("foo", "foo"), f"{Fore.LIGHTGREEN_EX}foo{Fore.RESET}"),
    ],
)
def test_formatted_before(change: Change, expect: str) -> None:
    assert change.formatted_before == expect
