from pathlib import Path

from differently.handlers import TextDifferently


# def test() -> None:
#     diff = TextDifferently(
#         "foo",
#         "boo",
#         color=True,
#     )
#     expect = "\x1b[33mfoo\x1b[39m  \x1b[33m~\x1b[39m  \x1b[33mboo\x1b[39m"
#     assert str(diff) == expect


def test_load() -> None:
    path = Path() / "tests" / "foo.txt"
    assert TextDifferently.load(path) == "foo\n"
