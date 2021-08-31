from argparse import ArgumentParser

from colorama import deinit, init

from differently import TextDifferently


def cli_entry() -> None:
    parser = ArgumentParser(description="differently")
    parser.add_argument("file1", help="File 1")
    parser.add_argument("file2", help="File 2")
    args = parser.parse_args()

    init()
    with open(args.file1, "r") as file1:
        with open(args.file2, "r") as file2:
            print(TextDifferently(file1.read(), file2.read()))
    deinit()


if __name__ == "__main__":
    cli_entry()
