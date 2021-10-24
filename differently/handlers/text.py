from pathlib import Path

from differently.handlers.list import ListDifferently


class TextDifferently(ListDifferently):
    """
    Visualises differences between strings.


    `TextDifferently` visualises the differences between strings:

    ```python
    from differently import TextDifferently

    diff = TextDifferently("one\ntoo\nthree", "one\ntwo\nthree")

    print(diff)
    ```

    ```text
    one    =  one
    too    ~  two
    three  =  three
    ```


    """

    def __init__(
        self,
        a: str,
        b: str,
        color: bool = True,
    ) -> None:
        super().__init__(
            a.splitlines(),
            b.splitlines(),
            color=color,
        )

    @staticmethod
    def load(path: Path) -> str:
        with open(path, "r") as f:
            return f.read()
