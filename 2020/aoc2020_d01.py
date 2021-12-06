import re
from itertools import permutations
import argparse
from io import TextIOWrapper
from os.path import basename
import pathlib
import sys
from rich import print


""" https://adventofcode.com/2020/day/1 """


def init_cmdl_parser() -> argparse.ArgumentParser:
    cmdl_parser = argparse.ArgumentParser()
    cmdl_parser.add_argument("-d", "--debug", help="Debug", action="store_true")
    return cmdl_parser


def main():

    # get command line args
    cmdl_parser = init_cmdl_parser()
    cmdl_args = cmdl_parser.parse_args()

    # load data
    raw_data = load_data(cmdl_args.debug).read().split("\n")

    question = "At how many points do at least two lines overlap?"
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = "At how many points do at least two lines overlap?"
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:
    int_data = list(int(i) for i in kwargs["raw_data"])
    return [i * j for i, j in permutations(int_data, 2) if i + j == 2020][0]


def solution2(**kwargs) -> int:
    int_data = list(int(i) for i in kwargs["raw_data"])
    return [i * j * k for i, j, k in permutations(int_data, 3) if i + j + k == 2020][0]


def load_data(debug: bool) -> TextIOWrapper:
    day = re.search(r"aoc.*_(?P<day>d[0-9]{2})", basename(__file__)).group("day")
    input_file_name = (
        f"{pathlib.Path(__file__).parent.absolute()}"
        f"/data/{day}{'_test' if debug else ''}.data"
    )

    try:
        input_file = open(input_file_name)
    except FileNotFoundError as e:
        print(f"While trying to read data file: {e}")
        sys.exit(e.errno)

    return input_file


if __name__ == "__main__":
    main()
