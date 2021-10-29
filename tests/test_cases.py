from os import scandir
from pathlib import Path

from differently import JsonDifferently


def test() -> None:
    for directory in scandir(Path() / "tests" / "cases"):
        a = JsonDifferently.load(Path(directory) / "a.json")
        b = JsonDifferently.load(Path(directory) / "b.json")

        actual_json = str(JsonDifferently(a, b, color=True))
        with open(Path(directory) / "actual-json.txt", "w") as f:
            f.write(actual_json)

        with open(Path(directory) / "expect-json.txt", "r") as f:
            expect = f.read().strip()
            if actual_json != expect:
                print("ACTUAL:")
                print(actual_json)
                print()
                print("EXPECTED:")
                print(expect)
                assert False
