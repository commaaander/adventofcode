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
    for index, command in commands.items():

        if command["x1"] == command["x2"]:
            line_length = abs(command["y2"] - command["y1"])
            start = min(command["y1"], command["y2"])
            for i in range(line_length + 1):
                increment_point_count(floor_map, command["x1"], start + i)

        elif command["y1"] == command["y2"]:
            line_length = abs(command["x2"] - command["x1"])
            start = min(command["x1"], command["x2"])
            for i in range(line_length + 1):
                increment_point_count(floor_map, start + i, command["y1"])

        else:
            if part2:
                line_length = abs(command["x2"] - command["x1"])
                if command["x1"] >= command["x2"] and command["y1"] >= command["y2"]:
                    for i in range(line_length + 1):
                        increment_point_count(
                            floor_map, command["x1"] - i, command["y1"] - i
                        )
                elif command["x1"] <= command["x2"] and command["y1"] >= command["y2"]:
                    for i in range(line_length + 1):
                        increment_point_count(
                            floor_map, command["x1"] + i, command["y1"] - i
                        )
                elif command["x1"] <= command["x2"] and command["y1"] <= command["y2"]:
                    for i in range(line_length + 1):
                        increment_point_count(
                            floor_map, command["x1"] + i, command["y1"] + i
                        )
                elif command["x1"] >= command["x2"] and command["y1"] <= command["y2"]:
                    for i in range(line_length + 1):
                        increment_point_count(
                            floor_map, command["x1"] - i, command["y1"] + i
                        )
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
