import re
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
    raw_data = [int(c) for c in load_data(cmdl_args.debug).read()]
    question = "What is the solution to your captcha?"
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = "What is the solution to your new captcha?"
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:
    data = kwargs["raw_data"][:]
    data.append(data[0])
    return sum(n for i, n in enumerate(data[:-1]) if data[i + 1] == n)


def solution2(**kwargs) -> int:
    length = len(kwargs["raw_data"])
    data = kwargs["raw_data"]
    data = data + data[: int(length / 2)]
    return sum(n for i, n in enumerate(data[:length]) if data[i + int(length / 2)] == n)


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
