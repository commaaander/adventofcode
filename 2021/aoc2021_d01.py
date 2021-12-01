import argparse
import re
import sys
from os.path import basename
from itertools import pairwise, tee
from aoc2021_tools import load_data

""" https://adventofcode.com/2021/day/1 """


def init_cmdl_parser() -> argparse.ArgumentParser:
    cmdl_parser = argparse.ArgumentParser()
    cmdl_parser.add_argument("-d", "--debug", help="Debug", action="store_true")
    return cmdl_parser


def main():

    # get command line args
    cmdl_parser = init_cmdl_parser()
    cmdl_args = cmdl_parser.parse_args()

    # load data
    day = re.search(r"aoc.*_(?P<day>d[0-9]{2})", basename(__file__)).group("day")
    data_file_name = f"{day}{'_test' if cmdl_args.debug else ''}.data"
    raw_data = load_data(data_file_name, split_sep="\n")

    question = "How many measurements are larger than the previous measurement?"
    print(
        f"""Solution part one:
            {question}: {solution1(raw_data=raw_data)}
        """
    )
    question = "How many sums are larger than the previous sum?"
    print(
        f"""Solution part two:
            {question}: {solution2(raw_data=raw_data)}
        """
    )
    print()


def solution1(**kwargs) -> int:
    return sum(1 for i, j in pairwise(kwargs["raw_data"]) if int(i) < int(j))


def solution2(**kwargs) -> int:
    last_triplet_sum = 10000000
    increment_count = 0
    for triplet in triplewise(kwargs["raw_data"]):
        if sum(triplet) > last_triplet_sum:
            increment_count += 1
        last_triplet_sum = sum(triplet)

    return increment_count


def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield int(a), int(b), int(c)


if __name__ == "__main__":
    main()

"""
"""
