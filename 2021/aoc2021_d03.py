import argparse
import pathlib
import re
import sys
from enum import Enum
from io import TextIOWrapper
from os.path import basename

""" https://adventofcode.com/2021/day/3 """


class RatingType(Enum):
    oxygen_generator = 1
    co2_scrubber = 0


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

    question = "What is the power consumption of the submarine? "
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"Solution part one:\n\t{question}: {solution}")

    question = "What is the life support rating of the submarine?"
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"Solution part one:\n\t{question}: {solution}")


def solution1(**kwargs) -> int:
    number_length = len(kwargs["raw_data"][0])
    number_count = len(kwargs["raw_data"])

    gamma = ""
    epsilon = ""
    for i in range(number_length):
        gamma += (
            "1"
            if sum(int(c[i]) for c in kwargs["raw_data"]) > number_count / 2
            else "0"
        )
    epsilon = "".join([str(1 - int(x)) for x in gamma])

    if kwargs["debug"]:
        print(f"{gamma=}->{int(gamma, 2)}, {epsilon=}->{int(epsilon, 2)}")
    return int(gamma, 2) * int(epsilon, 2)


def solution2(**kwargs) -> int:

    return get_rating(RatingType.oxygen_generator, kwargs["raw_data"]) * get_rating(
        RatingType.co2_scrubber, kwargs["raw_data"]
    )


def get_rating(rating_typ: RatingType, diagnostic_report: list) -> int:

    filtered_value = filter_report(rating_typ, diagnostic_report)
    return int(filtered_value[0], 2)


def filter_report(rating_typ: RatingType, diagnostic_report: list, index: int = 0):

    one_count = sum(int(number[index]) for number in diagnostic_report)

    if rating_typ == RatingType.oxygen_generator:
        filter_value = "1" if one_count >= len(diagnostic_report) - one_count else "0"
    else:
        filter_value = "1" if one_count < len(diagnostic_report) - one_count else "0"

    diagnostic_report = [
        number for number in diagnostic_report if number[index] == filter_value
    ]

    if len(diagnostic_report) > 1:
        return filter_report(rating_typ, diagnostic_report, index + 1)
    else:
        return diagnostic_report


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
