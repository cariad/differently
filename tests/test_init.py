from io import StringIO
from typing import Optional

from pytest import mark

from differently import render


@mark.parametrize(
    "a, b, expect",
    [
        (None, None, ""),
        ("", "", ""),
        ("", "foo: bar", "  \x1b[33m>\x1b[39m  \x1b[33mfoo: bar\x1b[39m\n"),
    ],
)
def test_render(a: Optional[str], b: Optional[str], expect: str) -> None:
    writer = StringIO()
    render(a, b, writer)
    assert writer.getvalue() == expect
