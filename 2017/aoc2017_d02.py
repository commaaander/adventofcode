import re
import argparse
from io import TextIOWrapper
from os.path import basename
import pathlib
import sys
from rich import print
from itertools import permutations


""" https://adventofcode.com/2020/day/2 """


def init_cmdl_parser() -> argparse.ArgumentParser:
    cmdl_parser = argparse.ArgumentParser()
    cmdl_parser.add_argument("-d", "--debug", help="Debug", action="store_true")
    return cmdl_parser


def main():

    # get command line args
    cmdl_parser = init_cmdl_parser()
    cmdl_args = cmdl_parser.parse_args()

    # load data
    raw_data = [
        re.split(r"\s", line) for line in load_data(cmdl_args.debug).read().split("\n")
    ]
    question = "What is the checksum for the spreadsheet in your puzzle input?"
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = "What is the sum of each row's result in your puzzle input?"
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:
    spreadsheet = kwargs["raw_data"]
    checksum = 0
    for row in spreadsheet:
        checksum += max(int(i) for i in row) - min(int(i) for i in row)
    return checksum


def solution2(**kwargs) -> int:
    spreadsheet = kwargs["raw_data"]
    checksum = 0
    for row in spreadsheet:
        row = [int(i) for i in row]
        x, y = [(x, y) for x, y in permutations(row, 2) if x / y == int(x / y)][0]
        checksum += int(x / y)
    return checksum


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
