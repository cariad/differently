from pytest import mark

from differently.change_type import ChangeType
from differently.line import Line


@mark.parametrize(
    "diff, expect",
    [
        ("  foo", ChangeType.none),
        ("+ foo", ChangeType.insert),
        ("- foo", ChangeType.delete),
        ("? ^", ChangeType.modify),
    ],
)
def test_change(diff: str, expect: ChangeType) -> None:
    assert Line(diff).change_type == expect
