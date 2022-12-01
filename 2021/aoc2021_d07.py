import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename
from rich import print

""" https://adventofcode.com/2021/day/7 """


def init_cmdl_parser() -> argparse.ArgumentParser:
    cmdl_parser = argparse.ArgumentParser()
    cmdl_parser.add_argument("-d", "--debug", help="Debug", action="store_true")
    return cmdl_parser


def main():

    # get command line args
    cmdl_parser = init_cmdl_parser()
    cmdl_args = cmdl_parser.parse_args()

    # load data
    raw_data = [int(i) for i in load_data(cmdl_args.debug).read().split(",")]

    question = ""
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = ""
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:
    levels = []
    for level in range(
        min(i for i in kwargs["raw_data"]),
        max(i for i in kwargs["raw_data"]) + 1,
    ):
        levels.append((level, sum(abs(i - level) for i in kwargs["raw_data"])))
    return min(levels, key=lambda k: k[1])[1]


def solution2(**kwargs) -> int:
    levels = []
    for level in range(
        min(i for i in kwargs["raw_data"]),
        max(i for i in kwargs["raw_data"]) + 1,
    ):
        levels.append(
            (
                level,
                int(sum((abs(i - level) * (abs(i - level) + 1)) / 2 for i in kwargs["raw_data"])),
            )
        )
    return min(levels, key=lambda l: l[1])[1]


def load_data(debug: bool) -> TextIOWrapper:
    day = re.search(r"aoc.*_(?P<day>d[0-9]{2})", basename(__file__)).group("day")
    input_file_name = f"{pathlib.Path(__file__).parent.absolute()}" f"/data/{day}{'_test' if debug else ''}.data"

    try:
        input_file = open(input_file_name)
    except FileNotFoundError as e:
        print(f"While trying to read data file: {e}")
        sys.exit(e.errno)

    return input_file


if __name__ == "__main__":
    main()
