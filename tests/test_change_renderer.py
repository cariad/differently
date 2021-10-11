from typing import List

from colorama import Fore
from pytest import mark, raises

from differently.change import Change
from differently.change_type import ChangeType
from differently.renderers.table import TableRenderer


@mark.parametrize(
    "change, expect",
    [
        (ChangeType.delete, f"{Fore.LIGHTRED_EX}>{Fore.RESET}"),
        (ChangeType.insert, ">"),
        (ChangeType.replace, f"{Fore.LIGHTYELLOW_EX}>{Fore.RESET}"),
        (ChangeType.none, ">"),
    ],
)
def test_arrow(change: ChangeType, expect: str) -> None:
    assert TableRenderer.arrow(change) == expect


@mark.parametrize(
    "text, change, expect",
    [
        (None, ChangeType.insert, ""),
        ("", ChangeType.insert, ""),
        ("foo", ChangeType.insert, f"{Fore.LIGHTYELLOW_EX}foo{Fore.RESET}"),
        ("foo", ChangeType.replace, f"{Fore.LIGHTYELLOW_EX}foo{Fore.RESET}"),
        ("foo", ChangeType.none, f"{Fore.LIGHTGREEN_EX}foo{Fore.RESET}"),
    ],
)
def test_format_after(text: str, change: ChangeType, expect: str) -> None:
    assert TableRenderer.format_after(text, change) == expect


def test_format_after__invalid() -> None:
    with raises(ValueError) as ex:  # pyright: reportUnknownVariableType=false
        TableRenderer.format_after("foo", ChangeType.delete)
    assert (
        str(ex.value) == 'no format-after for change "ChangeType.delete" in "foo"'
    )  # pyright: reportUnknownArgumentType=false, reportUnknownMemberType=false


@mark.parametrize(
    "text, change, expect",
    [
        (None, ChangeType.delete, ""),
        ("", ChangeType.delete, ""),
        (
            "foo",
            ChangeType.delete,
            f"{Fore.LIGHTRED_EX}f\u0336o\u0336o\u0336{Fore.RESET}",
        ),
        ("foo", ChangeType.replace, f"{Fore.LIGHTYELLOW_EX}foo{Fore.RESET}"),
        ("foo", ChangeType.none, f"{Fore.LIGHTGREEN_EX}foo{Fore.RESET}"),
    ],
)
def test_format_before(text: str, change: ChangeType, expect: str) -> None:
    assert TableRenderer.format_before(text, change) == expect


def test_format_before__invalid() -> None:
    with raises(ValueError) as ex:  # pyright: reportUnknownVariableType=false
        TableRenderer.format_before("foo", ChangeType.insert)
    assert (
        str(ex.value) == 'no format-before for change "ChangeType.insert"'
    )  # pyright: reportUnknownArgumentType=false, reportUnknownMemberType=false


@mark.parametrize(
    "changes, expect",
    [
        ([], ""),
        ([Change("foo", "foo")], "\x1b[92mfoo\x1b[39m > \x1b[92mfoo\x1b[39m"),
        # ([Change("foo", "bar")], "\x1b[92mfoo\x1b[39m > \x1b[92mfoo\x1b[39m"),
    ],
)
def test_table(changes: List[Change], expect: str) -> None:
    assert TableRenderer(changes).table == expect
