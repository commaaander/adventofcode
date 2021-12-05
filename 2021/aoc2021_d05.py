import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename

""" https://adventofcode.com/2021/day/5 """


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
    print(f"Solution part one:\n\t{question} {solution}")

    question = "At how many points do at least two lines overlap?"
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"Solution part two:\n\t{question} {solution}")


def solution1(**kwargs) -> int:
    commands = input_interpreter(kwargs["raw_data"])
    floor_map = execute_commands(commands)
    return sum(1 for p in floor_map.keys() if floor_map[p] > 1)


def solution2(**kwargs) -> int:
    commands = input_interpreter(kwargs["raw_data"])
    floor_map = execute_commands(commands, part2=True)
    return sum(1 for p in floor_map.keys() if floor_map[p] > 1)


def input_interpreter(input: list) -> dict:
    commands = {}
    for index, line in enumerate(input, start=1):
        match = re.search(
            r"(?P<x1>[0-9]+),(?P<y1>[0-9]+) -> (?P<x2>[0-9]+),(?P<y2>[0-9]+)", line
        )
        commands[index] = {}
        for coord in ["x1", "y1", "x2", "y2"]:
            commands[index][coord] = int(match.group(coord))
    return commands


def execute_commands(commands: dict, part2: bool = False) -> dict:
    floor_map = {}
    for cmd in commands.values():

        x1, x2, y1, y2 = cmd["x1"], cmd["x2"], cmd["y1"], cmd["y2"]
        if x1 == x2:
            line_length = abs(y2 - y1)
            start = min(y1, y2)
            for i in range(line_length + 1):
                increment_point_count(floor_map, x1, start + i)

        elif y1 == y2:
            line_length = abs(x2 - x1)
            start = min(x1, x2)
            for i in range(line_length + 1):
                increment_point_count(floor_map, start + i, y1)

        else:
            if part2:
                line_length = abs(x2 - x1)
                if x1 >= x2 and y1 >= y2:
                    dx, dy = -1, -1
                elif x1 <= x2 and y1 >= y2:
                    dx, dy = 1, -1
                elif x1 <= x2 and y1 <= y2:
                    dx, dy = 1, 1
                elif x1 >= x2 and y1 <= y2:
                    dx, dy = -1, 1
                for i in range(line_length + 1):
                    increment_point_count(floor_map, x1 + dx * i, y1 + dy * i)
    return floor_map


def increment_point_count(floor_map: dict, x: int, y: int):
    try:
        floor_map[(x, y)] += 1
    except Exception:
        floor_map[(x, y)] = 1


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
