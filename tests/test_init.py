from io import StringIO

from differently import render


def test_render() -> None:
    writer = StringIO()
    render("", "foo: bar", writer)
    assert writer.getvalue() == "  \x1b[33m>\x1b[39m  \x1b[33mfoo: bar\x1b[39m\n"
