from pathlib import Path
from typing import TypedDict

from differently.handlers import JsonDifferently


class FooDict(TypedDict):
    foo: str


def test() -> None:
    diff = JsonDifferently[FooDict]({"foo": "boo"}, {"foo": "woo"})
    assert (
        str(diff)
        == """\x1b[92m{\x1b[39m              > \x1b[92m{\x1b[39m
\x1b[93m  "foo": "boo"\x1b[39m \x1b[93m>\x1b[39m \x1b[93m  "foo": "woo"\x1b[39m
\x1b[92m}\x1b[39m              > \x1b[92m}\x1b[39m"""
    )


def test_load() -> None:
    path = Path() / "tests" / "foo.json"
    assert JsonDifferently[FooDict].load(path) == {"foo": "bar"}
