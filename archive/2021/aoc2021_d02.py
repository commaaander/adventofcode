import argparse
import re
from os.path import basename
from aoc2021_tools import load_data

""" https://adventofcode.com/2021/day/2 """


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

    question = (
        "What do you get if you multiply your final horizontal position by your "
        "final depth?"
    )
    print(f"Solution part one:\n\t{question}: {solution1(raw_data=raw_data)}")

    question = (
        "What do you get if you multiply your final horizontal position by your "
        "final depth?"
    )
    print(f"Solution part one:\n\t{question}: {solution1(raw_data=raw_data)}")
    print()


def solution1(**kwargs) -> int:
    course_data = [line.split(" ") for line in kwargs["raw_data"]]
    final_horizontal_pos = sum(
        int(line[1]) for line in course_data if line[0] == "forward"
    )
    final_depth = sum(int(line[1]) for line in course_data if line[0] == "down") - sum(
        int(line[1]) for line in course_data if line[0] == "up"
    )
    return final_horizontal_pos * final_depth


def solution2(**kwargs) -> int:
    horizontal_pos = 0
    depth = 0
    aim = 0
    for command in kwargs["raw_data"]:
        match command.split():
            case ["forward", value]:
                horizontal_pos += int(value)
                depth += aim * int(value)
            case ["down", value]:
                aim += int(value)
            case ["up", value]:
                aim -= int(value)
    return horizontal_pos * depth


if __name__ == "__main__":
    main()
