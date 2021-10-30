from logging import DEBUG, basicConfig
from typing import List

from pytest import mark

from differently import ListDifferently, StringDifferently


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
