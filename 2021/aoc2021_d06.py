import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename
from rich import print

""" https://adventofcode.com/2021/day/6 """


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

    question = "How many lanternfish would there be after 80 days?"
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug, days=80)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = ""
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug, days=80)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:
    swarm = kwargs["raw_data"]
    for day in range(kwargs["days"]):
        new_fishes = sum(1 for f in swarm if f == 0)
        swarm = [f - 1 if f > 0 else 6 for f in swarm]
        swarm += new_fishes * [8]
        print(f"Day {day}: {len(swarm)}")
    return len(swarm)


def solution2(**kwargs) -> int:
    fish_types = {}
    for i in range(8):
        fish_types[i] = sum(1 for f in kwargs["raw_data"] if f == i)
    for day in range(kwargs["days"]):
        new_fishes = fish_types[0]
        for i in range(7):
            fish_types[i] = fish_types[i + 1]
        fish_types[6] += new_fishes
        fish_types[7] = new_fishes
        print(f"Day {day}: {sum(fish_types[i] for i in fish_types)}")
    return sum(fish_types[i] for i in fish_types)


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
