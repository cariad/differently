from differently.list import ListDifferently


class TextDifferently:
    def __init__(self, a: str, b: str) -> None:
        self.ld = ListDifferently(a=a.splitlines(), b=b.splitlines())

    def __repr__(self) -> str:
        return repr(self.ld)
