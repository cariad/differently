from argparse import ArgumentParser
from typing import IO, List

from ansiscape.checks import should_emit_codes

from differently import (
    deserialize,
    get_deserializer_keys,
    get_renderer,
    get_renderer_keys,
)
from differently.version import get_version


def entry(cli_args: List[str], writer: IO[str]) -> int:
    parser = ArgumentParser(description="Compares files and data.")
    parser.add_argument("file0", help="Source file", nargs="?")
    parser.add_argument("file1", help="Comparing file", nargs="?")

    parser.add_argument("--color", help="force colour", action="store_true")

    parser.add_argument(
        "--in-format",
        default="text",
        help="input formats (comma-separate if files are different)",
        metavar=f"{{{','.join(get_deserializer_keys())}}}",
    )

    parser.add_argument(
        "--out-format",
        help="output format",
        metavar=f"{{{','.join(get_renderer_keys())}}}",
    )

    parser.add_argument("--version", help="show version and exit", action="store_true")

    args = parser.parse_args(cli_args)

    if args.version:
        writer.write(get_version() + "\n")
        return 0

    if args.out_format:
        renderer = get_renderer(args.out_format)
    elif "," in args.in_format:
        writer.write(
            'You must include "--out-format" when you specify multiple values for "--in-format".\n'
        )
        return 1
    else:
        renderer = get_renderer(args.in_format)

    diff = renderer(
        deserialize(args.in_format, 0, args.file0),
        deserialize(args.in_format, 1, args.file1),
        color=True if args.color else should_emit_codes(),
    )

    diff.render(writer)
    return 0
