import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename
from rich import print

""" https://adventofcode.com/2021/day/9 """


def main():

    # get command line args
    cmdl_parser = init_cmdl_parser()
    cmdl_args = cmdl_parser.parse_args()

    # load data
    raw_data = load_data(cmdl_args.debug).read().split("\n")

    question = ""
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = ""
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:
    area_map = [[int(x) for x in row] for row in kwargs["raw_data"]]
    sum = 0
    for y, row in enumerate(area_map):
        for x, value in enumerate(row):
            if is_low_point(x, y, area_map):
                print(f"Low Point {x=},{y=}: {value=}")
                sum += int(value) + 1
    draw_area_map(area_map)
    return sum


def solution2(**kwargs) -> int:
    return 0


def is_low_point(x: int, y: int, area_map: list) -> bool:
    ret_val = True
    if x == 0 and y == 73:
        pass
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        try:
            if y + dy < 0 or x + dx < 0:
                raise IndexError
            ret_val &= area_map[y + dy][x + dx] > area_map[y][x]
        except IndexError:
            pass
    return ret_val


def draw_area_map(area_map: list) -> None:
    output = ""
    for y, row in enumerate(area_map):
        output += f"{y:3d}\t"
        for x, value in enumerate(row):
            color = "bright_yellow" if is_low_point(x, y, area_map) else "white"
            output += f"[{color}]{value}[/{color}]"
        output += "\n"
    print(output)
    return


# ---------------------------------------------------------------------------------------
def init_cmdl_parser() -> argparse.ArgumentParser:
    cmdl_parser = argparse.ArgumentParser()
    cmdl_parser.add_argument("-d", "--debug", help="Debug", action="store_true")
    return cmdl_parser


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
