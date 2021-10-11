from pathlib import Path

from differently.handlers import TextDifferently


def test() -> None:
    diff = TextDifferently("foo", "boo")
    expect = "\x1b[93mfoo\x1b[39m \x1b[93m>\x1b[39m \x1b[93mboo\x1b[39m"
    assert str(diff) == expect


def test_load() -> None:
    path = Path() / "tests" / "foo.txt"
    assert TextDifferently.load(path) == "foo\n"
