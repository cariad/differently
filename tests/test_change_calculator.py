from typing import List

from pytest import mark, raises

from differently.change import Change
from differently.change_calculator import ChangeCalculator


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
    assert ChangeCalculator(a, b).changes == expect


def test_change_type__invalid() -> None:
    c = ChangeCalculator([], [])
    setattr(c, "diff", ["🤡 foo"])
    with raises(ValueError) as ex:
        c._get_change_type_at(0)
    assert str(ex.value) == 'unrecognised change type "🤡" in "🤡 foo"'
