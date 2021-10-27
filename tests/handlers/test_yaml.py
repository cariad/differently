from pathlib import Path
from typing import TypedDict

from differently.handlers import YamlDifferently


class FooDict(TypedDict):
    foo: str


# def test() -> None:
#     diff = YamlDifferently[FooDict](
#         {"foo": "boo"},
#         {"foo": "woo"},
#         color=True,
#     )
#     expect = "\x1b[33mfoo: boo\x1b[39m  \x1b[33m~\x1b[39m  \x1b[33mfoo: woo\x1b[39m"
#     assert str(diff) == expect


def test_load() -> None:
    path = Path() / "tests" / "foo.yml"
    assert YamlDifferently[FooDict].load(path) == {"foo": "bar"}
