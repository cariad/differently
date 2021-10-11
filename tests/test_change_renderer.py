from typing import List

from pytest import mark, raises

from differently.change import Change
from differently.change_type import ChangeType
from differently.renderers.table import TableRenderer


@mark.parametrize(
    "change, expect",
    [
        (ChangeType.delete, "x"),
        (ChangeType.insert, ">"),
        (ChangeType.replace, "~"),
        (ChangeType.none, "="),
    ],
)
def test_arrow(change: ChangeType, expect: str) -> None:
    assert TableRenderer.arrow(change) == expect


@mark.parametrize(
    "change, expect",
    [
        (ChangeType.delete, "\x1b[38;5;9m.\x1b[39m"),
        (ChangeType.insert, "\x1b[38;5;11m.\x1b[39m"),
        (ChangeType.replace, "\x1b[38;5;11m.\x1b[39m"),
        (ChangeType.none, "\x1b[38;5;10m.\x1b[39m"),
    ],
)
def test_format_arrow(change: ChangeType, expect: str) -> None:
    assert TableRenderer.format_arrow(".", change) == expect


@mark.parametrize(
    "text, change, expect",
    [
        (None, ChangeType.insert, ""),
        ("", ChangeType.insert, ""),
        ("foo", ChangeType.insert, "\x1b[38;5;11mfoo\x1b[39m"),
        ("foo", ChangeType.replace, "\x1b[38;5;11mfoo\x1b[39m"),
        ("foo", ChangeType.none, "\x1b[38;5;10mfoo\x1b[39m"),
    ],
)
def test_format_after(text: str, change: ChangeType, expect: str) -> None:
    assert TableRenderer.format_after(text, change) == expect


def test_format_after__invalid() -> None:
    with raises(ValueError) as ex:
        TableRenderer.format_after("foo", ChangeType.delete)
    assert str(ex.value) == 'no format-after for change "ChangeType.delete" in "foo"'


@mark.parametrize(
    "text, change, expect",
    [
        (None, ChangeType.delete, ""),
        ("", ChangeType.delete, ""),
        ("foo", ChangeType.delete, "\x1b[38;5;9mfoo\x1b[39m"),
        ("foo", ChangeType.replace, "\x1b[38;5;11mfoo\x1b[39m"),
        ("foo", ChangeType.none, "\x1b[38;5;10mfoo\x1b[39m"),
    ],
)
def test_format_before(text: str, change: ChangeType, expect: str) -> None:
    assert TableRenderer.format_before(text, change) == expect


def test_format_before__invalid() -> None:
    with raises(ValueError) as ex:
        TableRenderer.format_before("foo", ChangeType.insert)
    assert str(ex.value) == 'no format-before for change "ChangeType.insert"'


@mark.parametrize(
    "changes, expect",
    [
        ([], ""),
        (
            [Change("foo", "foo")],
            "\x1b[38;5;10mfoo\x1b[39m  \x1b[38;5;10m=\x1b[39m  \x1b[38;5;10mfoo\x1b[39m",
        ),
    ],
)
def test_table(changes: List[Change], expect: str) -> None:
    assert TableRenderer(changes, color=True).table == expect
