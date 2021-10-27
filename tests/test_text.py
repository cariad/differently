from differently import TextDifferently


# def test() -> None:
#     a = """Hello world!
# My name is Bobby Pringles!"""

#     b = """Hello galaxy!
# My name is Bobby Pringles!
# I like turtles."""

#     assert (
#         str(TextDifferently(a, b, color=True))
#         == """\x1b[33mHello world!\x1b[39m                \x1b[33m~\x1b[39m  \x1b[33mHello galaxy!\x1b[39m\n\x1b[32mMy name is Bobby Pringles!\x1b[39m  \x1b[32m=\x1b[39m  \x1b[32mMy name is Bobby Pringles!\x1b[39m\n                            \x1b[33m>\x1b[39m  \x1b[33mI like turtles.\x1b[39m"""
#     )
