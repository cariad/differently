from typing import List

from colorama import Fore
from pytest import mark

from differently import ListDifferently
from differently.change import Change


@mark.parametrize(
    "a, b, expect",
    [
        (
            ["first"],
            ["first"],
            [Change("first", "first")],
        ),
        (
            ["first"],
            ["first (changed)"],
            [Change("first", "first (changed)")],
        ),
        (
            ["first"],
            ["first", "second"],
            [
                Change("first", "first"),
                Change(None, "second"),
            ],
        ),
        (
            ["first", "second"],
            ["first"],
            [
                Change("first", "first"),
                Change("second", None),
            ],
        ),
        (
            ["first", "third"],
            ["first", "second", "third"],
            [
                Change("first", "first"),
                Change(None, "second"),
                Change("third", "third"),
            ],
        ),
        (
            ["first", "second", "third"],
            ["first", "third"],
            [
                Change("first", "first"),
                Change("second", None),
                Change("third", "third"),
            ],
        ),
        (
            ["first", "fourth"],
            ["first", "second", "third", "fourth"],
            [
                Change("first", "first"),
                Change(None, "second"),
                Change(None, "third"),
                Change("fourth", "fourth"),
            ],
        ),
        (
            ["first", "second", "third", "fourth"],
            ["first", "fourth"],
            [
                Change("first", "first"),
                Change("second", None),
                Change("third", None),
                Change("fourth", "fourth"),
            ],
        ),
        (
            ["first", "second", "third"],
            ["first", "second (changed)"],
            [
                Change("first", "first"),
                Change("second", "second (changed)"),
                Change("third", None),
            ],
        ),
        (
            ["first 1"],
            ["first 2"],
            [Change("first 1", "first 2")],
        ),
    ],
)
def test_line_changes(a: List[str], b: List[str], expect: List[Change]) -> None:
    ld = ListDifferently(a, b)
    assert ld.line_changes == expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            ["first"],
            ["first"],
            f"{Fore.LIGHTGREEN_EX}first{Fore.RESET} > {Fore.LIGHTGREEN_EX}first{Fore.RESET}",
        ),
        (
            ["first"],
            ["first", "second"],
            (
                f"{Fore.LIGHTGREEN_EX}first{Fore.RESET} > {Fore.LIGHTGREEN_EX}first{Fore.RESET}\n"
                + f"      > {Fore.LIGHTYELLOW_EX}second{Fore.RESET}"
            ),
        ),
        (
            ["first", "second"],
            ["first"],
            (
                f"{Fore.LIGHTGREEN_EX}first{Fore.RESET}  > {Fore.LIGHTGREEN_EX}first{Fore.RESET}\n"
                + f"{Fore.LIGHTRED_EX}s\u0336e\u0336c\u0336o\u0336n\u0336d\u0336{Fore.RESET} {Fore.LIGHTRED_EX}x{Fore.RESET}"
            ),
        ),
    ],
)
def test_repr(a: List[str], b: List[str], expect: str) -> None:
    assert repr(ListDifferently(a, b)) == expect
