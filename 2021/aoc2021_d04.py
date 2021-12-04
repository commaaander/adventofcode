import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename

""" https://adventofcode.com/2021/day/4 """



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

    question = ""
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"Solution part one:\n\t{question}: {solution}")

    question = ""
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"Solution part one:\n\t{question}: {solution}")


def solution1(**kwargs) -> int:
    draw_numbers,boards = create_boards(kwargs["raw_data"])
    print(draw_numbers, boards)
    return 0


def solution2(**kwargs) -> int:
    return 0

def create_boards(board_data: list):
    boards = dict()
    for board_number,
    return board_data[0].split(","), boards


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
