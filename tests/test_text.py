from differently import TextDifferently


def test() -> None:
    a = """Hello world!
My name is Bobby Pringles!"""

    b = """Hello galaxy!
My name is Bobby Pringles!
I like turtles."""

    assert (
        str(TextDifferently(a, b))
        == """\x1b[93mHello world!\x1b[39m               \x1b[93m>\x1b[39m \x1b[93mHello galaxy!\x1b[39m
\x1b[92mMy name is Bobby Pringles!\x1b[39m > \x1b[92mMy name is Bobby Pringles!\x1b[39m
                           > \x1b[93mI like turtles.\x1b[39m"""
    )
