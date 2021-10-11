from differently import TextDifferently


def test() -> None:
    a = """Hello world!
My name is Bobby Pringles!"""

    b = """Hello galaxy!
My name is Bobby Pringles!
I like turtles."""

    assert (
        str(TextDifferently(a, b))
        == """\x1b[38;5;11mHello world!\x1b[39m                \x1b[38;5;11m~\x1b[39m  \x1b[38;5;11mHello galaxy!\x1b[39m\n\x1b[38;5;10mMy name is Bobby Pringles!\x1b[39m  \x1b[38;5;10m=\x1b[39m  \x1b[38;5;10mMy name is Bobby Pringles!\x1b[39m\n                            \x1b[38;5;11m>\x1b[39m  \x1b[38;5;11mI like turtles.\x1b[39m"""
    )
