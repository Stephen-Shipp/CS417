from __future__ import annotations

import sys

from module_placeholder.placeholder import demo_function


def __parse_cli_args(args) -> list[str]:
    program_name = args[0]

    names = args[1:]

    return program_name, names


def main():
    _, names = __parse_cli_args(sys.argv)

    for name in names:
        greeting = demo_function(name)

        print(f"{greeting}!")


if __name__ == "__main__":
    main()
