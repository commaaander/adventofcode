import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename
from rich import print

""" https://adventofcode.com/2021/day/12 """

DEBUG = False


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
    # create graph
    graph = {}
    for edge in kwargs["raw_data"]:
        k1, k2 = edge.split("-")
        add_edge(k1, k2, graph)
        add_edge(k2, k1, graph)

    return 0


def solution2(**kwargs) -> int:
    return 0


def add_edge(k1: str, k2: str, graph: dict) -> None:
    try:
        graph[k1].append(k2)
    except KeyError:
        graph[k1] = [k2]


#
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
