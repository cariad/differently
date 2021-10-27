from logging import DEBUG, basicConfig
from typing import List

from pytest import mark

from differently import ListDifferently, StringDifferently

# from typing import List

# from pytest import mark, raises

# from differently.change import Change
# from differently.change_type import ChangeType
# from differently.renderers.table import TableRenderer


# @mark.parametrize(
#     "change, expect",
#     [
#         (ChangeType.delete, "x"),
#         (ChangeType.insert, ">"),
#         (ChangeType.replace, "~"),
#         (ChangeType.none, "="),
#     ],
# )
# def test_arrow(change: ChangeType, expect: str) -> None:
#     assert TableRenderer.arrow(change) == expect


# @mark.parametrize(
#     "change, expect",
#     [
#         (ChangeType.delete, "\x1b[31m.\x1b[39m"),
#         (ChangeType.insert, "\x1b[33m.\x1b[39m"),
#         (ChangeType.replace, "\x1b[33m.\x1b[39m"),
#         (ChangeType.none, "\x1b[32m.\x1b[39m"),
#     ],
# )
# def test_format_arrow(change: ChangeType, expect: str) -> None:
#     assert TableRenderer.format_arrow(".", change) == expect


# @mark.parametrize(
#     "text, change, expect",
#     [
#         (None, ChangeType.insert, ""),
#         ("", ChangeType.insert, ""),
#         ("foo", ChangeType.insert, "\x1b[33mfoo\x1b[39m"),
#         ("foo", ChangeType.replace, "\x1b[33mfoo\x1b[39m"),
#         ("foo", ChangeType.none, "\x1b[32mfoo\x1b[39m"),
#     ],
# )
# def test_format_after(text: str, change: ChangeType, expect: str) -> None:
#     assert TableRenderer.format_after(text, change) == expect


# def test_format_after__invalid() -> None:
#     with raises(ValueError) as ex:
#         TableRenderer.format_after("foo", ChangeType.delete)
#     assert str(ex.value) == 'no format-after for change "ChangeType.delete" in "foo"'


# @mark.parametrize(
#     "text, change, expect",
#     [
#         (None, ChangeType.delete, ""),
#         ("", ChangeType.delete, ""),
#         ("foo", ChangeType.delete, "\x1b[31mfoo\x1b[39m"),
#         ("foo", ChangeType.replace, "\x1b[33mfoo\x1b[39m"),
#         ("foo", ChangeType.none, "\x1b[32mfoo\x1b[39m"),
#     ],
# )
# def test_format_before(text: str, change: ChangeType, expect: str) -> None:
#     assert TableRenderer.format_before(text, change) == expect


# def test_format_before__invalid() -> None:
#     with raises(ValueError) as ex:
#         TableRenderer.format_before("foo", ChangeType.insert)
#     assert str(ex.value) == 'no format-before for change "ChangeType.insert"'


# @mark.parametrize(
#     "changes, expect",
#     [
#         ([], ""),
#         (
#             [Change("foo", "foo")],
#             "\x1b[32mfoo\x1b[39m  \x1b[32m=\x1b[39m  \x1b[32mfoo\x1b[39m",
#         ),
#     ],
# )
# def test_table(changes: List[Change], expect: str) -> None:
#     assert TableRenderer(changes, color=True).table == expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            ["first"],
            ["first"],
            [StringDifferently("first", "first")],
        ),
        (
            ["first"],
            ["first (changed)"],
            [StringDifferently("first", "first (changed)")],
        ),
        (
            ["first"],
            ["first", "second"],
            [
                StringDifferently("first", "first"),
                StringDifferently(None, "second"),
            ],
        ),
        (
            ["first", "second"],
            ["first"],
            [
                StringDifferently("first", "first"),
                StringDifferently("second", None),
            ],
        ),
        (
            ["first", "third"],
            ["first", "second", "third"],
            [
                StringDifferently("first", "first"),
                StringDifferently(None, "second"),
                StringDifferently("third", "third"),
            ],
        ),
        (
            ["first", "second", "third"],
            ["first", "third"],
            [
                StringDifferently("first", "first"),
                StringDifferently("second", None),
                StringDifferently("third", "third"),
            ],
        ),
        (
            ["first", "fourth"],
            ["first", "second", "third", "fourth"],
            [
                StringDifferently("first", "first"),
                StringDifferently(None, "second"),
                StringDifferently(None, "third"),
                StringDifferently("fourth", "fourth"),
            ],
        ),
        (
            ["first", "second", "third", "fourth"],
            ["first", "fourth"],
            [
                StringDifferently("first", "first"),
                StringDifferently("second", None),
                StringDifferently("third", None),
                StringDifferently("fourth", "fourth"),
            ],
        ),
        (
            ["first", "second", "third"],
            ["first", "second (changed)"],
            [
                StringDifferently("first", "first"),
                StringDifferently("second", "second (changed)"),
                StringDifferently("third", None),
            ],
        ),
        (
            ["first 1"],
            ["first 2"],
            [StringDifferently("first 1", "first 2")],
        ),
        (
            [
                "first",
                "seccond",
            ],
            [
                "first",
                "second",
                "third",
            ],
            [
                StringDifferently("first", "first"),
                StringDifferently("seccond", "second"),
                StringDifferently(None, "third"),
            ],
        ),
    ],
)
def test_differences(
    a: List[str],
    b: List[str],
    expect: List[StringDifferently],
) -> None:
    basicConfig(level=DEBUG, force=True)
    assert ListDifferently(a, b).differences == expect


# def test_change_type__invalid() -> None:
#     c = ChangeCalculator([], [])
#     setattr(c, "diff", ["🤡 foo"])
#     with raises(ValueError) as ex:
#         c._get_change_type_at(0)
#     assert str(ex.value) == 'unrecognised change type "🤡" in "🤡 foo"'
