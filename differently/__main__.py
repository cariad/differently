import importlib.resources as pkg_resources
from argparse import ArgumentParser

from colorama import deinit, init
from yaml import load

from differently.handlers import (
    deserialize,
    get_deserializer_keys,
    get_renderer,
    get_renderer_keys,
)


def cli_entry() -> None:
    with pkg_resources.open_text(__package__, "local.yml") as t:
        local = load(t)

    parser = ArgumentParser(description="differently")
    parser.add_argument("file0", help="Source file")
    parser.add_argument("file1", help="Comparing file")

    parser.add_argument(
        "--in-format",
        default="text",
        help=local["in_format"],
        metavar=f"{{{','.join(get_deserializer_keys())}}}",
    )

    parser.add_argument(
        "--out-format",
        help=local["out_format"],
        metavar=f"{{{','.join(get_renderer_keys())}}}",
    )

    args = parser.parse_args()

    if args.out_format:
        renderer = get_renderer(args.out_format)
    elif "," in args.in_format:
        print(
            'You must include "--out-format" when you specify multiple values for "--in-format".'
        )
        exit(1)
    else:
        renderer = get_renderer(args.in_format)

    diff = renderer(
        deserialize(args.in_format, 0, args.file0),
        deserialize(args.in_format, 1, args.file1),
    )

    init()
    print(diff)
    deinit()


if __name__ == "__main__":
    cli_entry()
