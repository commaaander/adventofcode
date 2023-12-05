#! /usr/bin/env python

import argparse
import importlib
import logging
import os
import re
import sys
from io import TextIOWrapper
from pathlib import Path

from rich import print
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table

logging.basicConfig(
    level=logging.ERROR,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)
LOG = logging.getLogger("rich")


def main():
    # get command line args
    cmdl_parser = init_cmdl_parser()
    cmdl_args = cmdl_parser.parse_args()

    # set globals
    if cmdl_args.verbose:
        LOG.setLevel(logging.DEBUG)

    LOG.debug(cmdl_args)

    if cmdl_args.list:
        list_solutions()
        sys.exit(0)

    # load data
    raw_data = load_data(use_test_data=cmdl_args.test, year=cmdl_args.year, day=cmdl_args.day).read()

    try:
        solution_module = f"aoc_{cmdl_args.year}.day_{cmdl_args.day:02d}"

        solution = importlib.import_module(solution_module)
    except ModuleNotFoundError as e:
        print(e)
        sys.exit(-1)

    if cmdl_args.solution in ("1", "all"):
        question, answer = solution.part_one(raw_data=raw_data)
        print(f"[yellow]Solution part one:[/yellow]\n{question} {answer}")

    if cmdl_args.solution in ("2", "all"):
        question, answer = solution.part_two(raw_data=raw_data)
        print(f"[yellow]Solution part two:[/yellow]\n{question} {answer}")

    return


def init_cmdl_parser() -> argparse.ArgumentParser:
    cmdl_parser = argparse.ArgumentParser()
    cmdl_parser.add_argument("-v", "--verbose", help="Set log level to 'Debug'", action="store_true")
    cmdl_parser.add_argument("-t", "--test", help="Use test data", action="store_true")
    cmdl_parser.add_argument("-l", "--list", help="List available solutions", action="store_true")
    cmdl_parser.add_argument("-y", "--year", metavar="YEAR", help="Year", type=int, required=True)
    cmdl_parser.add_argument("-d", "--day", metavar="DAY", help="Day", type=int, required=True)
    cmdl_parser.add_argument("-s", "--solution", metavar="SOLUTION", help="Solution", type=str, default="all")

    return cmdl_parser


def list_solutions():
    solutions = Table(title="Advent Of Code Solutions")
    solutions.add_column("Year")
    solutions.add_column("Day")

    for dir in os.listdir("."):
        if os.path.isdir(dir) and re.search(r"^aoc_\d{4}$", dir):
            for module in os.listdir(dir):
                if re.search(r"^day_\d{2}.py$", module):
                    solutions.add_row(dir, module)

    console = Console()
    console.print(solutions)


def load_data(use_test_data: bool, year: int, day: int) -> TextIOWrapper:
    input_file_name = f"{Path(__file__).parent.absolute()}" f"/aoc_{year}/data/d{day:02d}{'_test' if use_test_data else ''}.data"

    try:
        input_file = open(input_file_name)
    except FileNotFoundError as e:
        print(f"While trying to read data file: {e}")
        sys.exit(e.errno)

    return input_file


if __name__ == "__main__":
    main()
