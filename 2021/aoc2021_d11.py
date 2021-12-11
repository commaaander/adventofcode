import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename
from rich import print
from itertools import product

""" https://adventofcode.com/2021/day/11 """

DEBUG = False
FLASH_COUNTER = 0


def main():

    global DEBUG

    # get command line args
    cmdl_parser = init_cmdl_parser()
    cmdl_args = cmdl_parser.parse_args()

    # set globals
    DEBUG = cmdl_args.debug

    # load data
    raw_data = load_data(use_test_data=cmdl_args.test).read().split("\n")

    question = ""
    solution = solution1(raw_data=raw_data, steps=100)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = ""
    solution = solution2(raw_data=raw_data)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:
    global FLASH_COUNTER

    octopuses = create_octopus_map(kwargs["raw_data"])

    dprint("\n[underline]Start:[/underline]")
    dprint(print_octopuses(octopuses))

    for i in range(kwargs["steps"]):

        for x, y in octopuses:
            octopuses[(x, y)] += 1
        for x, y in octopuses:
            if octopuses[(x, y)] > 9:
                flash_octopus(x, y, octopuses)

        dprint(f"\n[underline]After Step {i+1}:[/underline]")
        dprint(print_octopuses(octopuses))

    return FLASH_COUNTER


def solution2(**kwargs) -> int:

    octopuses = create_octopus_map(kwargs["raw_data"])
    step = 0
    while sum(v for v in octopuses.values()) > 0:
        step += 1

        for x, y in octopuses:
            octopuses[(x, y)] += 1
        for x, y in octopuses:
            if octopuses[(x, y)] > 9:
                flash_octopus(x, y, octopuses)

        dprint(f"\n[underline]After Step {step}:[/underline]")
        dprint(print_octopuses(octopuses))

    return step


def create_octopus_map(input_data: list) -> dict:
    octopuses = {}
    for y, row in enumerate(input_data):
        for x, value in enumerate(row):
            octopuses[(x, y)] = int(value)
    return octopuses


def flash_octopus(x: int, y: int, octopuses: dict) -> None:

    global FLASH_COUNTER

    deltas = [-1, 0, 1]
    octopuses[(x, y)] = 0

    for dx, dy in [c for c in product(deltas, deltas) if c != (0, 0)]:
        try:
            if octopuses[(x + dx, y + dy)] > 0:
                octopuses[(x + dx, y + dy)] += 1
                if octopuses[(x + dx, y + dy)] > 9:
                    flash_octopus(x + dx, y + dy, octopuses)

        except KeyError:
            pass
    FLASH_COUNTER += 1
    return


def print_octopuses(octopuses: dict) -> str:
    xmax = max(x for x, _ in octopuses.keys()) + 1
    ymax = max(y for _, y in octopuses.keys()) + 1
    output = ""
    for y in range(ymax):
        output += f"{y:3d}\t"
        for x in range(xmax):
            color = "bright_yellow" if octopuses[(x, y)] == 0 else "white"
            output += f"[{color}]{octopuses[(x, y)]}[/{color}]"
        output += "\n"
    return output


# --------------------------------------------------------------------------------------
#
def init_cmdl_parser() -> argparse.ArgumentParser:
    cmdl_parser = argparse.ArgumentParser()
    cmdl_parser.add_argument("-d", "--debug", help="Debug", action="store_true")
    cmdl_parser.add_argument("-t", "--test", help="Use test data", action="store_true")
    return cmdl_parser


def load_data(use_test_data: bool) -> TextIOWrapper:
    day = re.search(r"aoc.*_(?P<day>d[0-9]{2})", basename(__file__)).group("day")
    input_file_name = (
        f"{pathlib.Path(__file__).parent.absolute()}"
        f"/data/{day}{'_test' if use_test_data else ''}.data"
    )

    try:
        input_file = open(input_file_name)
    except FileNotFoundError as e:
        print(f"While trying to read data file: {e}")
        sys.exit(e.errno)

    return input_file


def dprint(message: str) -> None:
    global DEBUG
    if DEBUG:
        print(message)
    return


if __name__ == "__main__":
    main()
