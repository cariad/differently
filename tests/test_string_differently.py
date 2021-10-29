from io import StringIO
from typing import Any

from pytest import mark

from differently import DifferenceType, StringDifferently


@mark.parametrize(
    "diff, expect",
    [
        (StringDifferently("foo", "foo"), "="),
        (StringDifferently("foo", None), "x"),
        (StringDifferently(None, "foo"), ">"),
        (StringDifferently("foo", "bar"), "~"),
    ],
)
def test_arrow(diff: StringDifferently, expect: str) -> None:
    assert diff.arrow == expect


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


@mark.parametrize(
    "diff, expect",
    [
        (StringDifferently("foo", "foo"), "\x1b[32mfoo\x1b[39m"),
        (StringDifferently("foo", "bar"), "\x1b[33mfoo\x1b[39m"),
        (StringDifferently("foo", None), "\x1b[31mfoo\x1b[39m"),
        (StringDifferently(None, "bar"), ""),
        (StringDifferently("foo", "foo", color=False), "foo"),
        (StringDifferently("foo", "bar", color=False), "foo"),
        (StringDifferently("foo", None, color=False), "foo"),
        (StringDifferently(None, "bar", color=False), ""),
    ],
)
def test_render_a(diff: StringDifferently, expect: str) -> None:
    writer = StringIO()
    diff._render_a(writer)  # pyright: reportPrivateUsage=false
    assert writer.getvalue() == expect


@mark.parametrize(
    "diff, expect",
    [
        (StringDifferently("foo", "foo"), "\x1b[32m=\x1b[39m"),
        (StringDifferently("foo", "bar"), "\x1b[33m~\x1b[39m"),
        (StringDifferently("foo", None), "\x1b[31mx\x1b[39m"),
        (StringDifferently(None, "bar"), "\x1b[33m>\x1b[39m"),
        (StringDifferently("foo", "foo", color=False), "="),
        (StringDifferently("foo", "bar", color=False), "~"),
        (StringDifferently("foo", None, color=False), "x"),
        (StringDifferently(None, "bar", color=False), ">"),
    ],
)
def test_render_arrow(diff: StringDifferently, expect: str) -> None:
    writer = StringIO()
    diff._render_arrow(writer)  # pyright: reportPrivateUsage=false
    assert writer.getvalue() == expect


@mark.parametrize(
    "diff, expect",
    [
        (StringDifferently("foo", "foo"), "\x1b[32mfoo\x1b[39m"),
        (StringDifferently("foo", "bar"), "\x1b[33mbar\x1b[39m"),
        (StringDifferently("foo", None), ""),
        (StringDifferently(None, "bar"), "\x1b[33mbar\x1b[39m"),
        (StringDifferently("foo", "foo", color=False), "foo"),
        (StringDifferently("foo", "bar", color=False), "bar"),
        (StringDifferently("foo", None, color=False), ""),
        (StringDifferently(None, "bar", color=False), "bar"),
    ],
)
def test_render_b(diff: StringDifferently, expect: str) -> None:
    writer = StringIO()
    diff._render_b(writer)  # pyright: reportPrivateUsage=false
    assert writer.getvalue() == expect


def test_repr() -> None:
    assert (
        repr(StringDifferently("foo", "bar"))
        == "\x1b[33mfoo\x1b[39m  \x1b[33m~\x1b[39m  \x1b[33mbar\x1b[39m"
    )


@mark.parametrize(
    "diff, expect",
    [
        (StringDifferently("foo", "foo"), DifferenceType.NONE),
        (StringDifferently("foo", None), DifferenceType.DELETION),
        (StringDifferently(None, "foo"), DifferenceType.INSERTION),
        (StringDifferently("foo", "bar"), DifferenceType.REPLACEMENT),
    ],
)
def test_type(diff: StringDifferently, expect: DifferenceType) -> None:
    assert diff.type == expect
