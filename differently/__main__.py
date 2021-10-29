from sys import argv, stdout

from differently.cli import entry


def cli_entry() -> None:
    exit(entry(cli_args=argv[1:], writer=stdout))


if __name__ == "__main__":
    cli_entry()
