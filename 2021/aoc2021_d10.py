import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename
from rich import print
from statistics import median

""" https://adventofcode.com/2021/day/10 """

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

    question = "What is the total syntax error score for those errors?"
    solution = solution1(raw_data=raw_data)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = "What is the middle score?"
    solution = solution2(raw_data=raw_data)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:

    open_signs = "([{<"
    close_signs = ")]}>"
    sign_scores = [3, 57, 1197, 25137]
    syntax_error_score = 0

    for line in kwargs["raw_data"]:
        simplified_line = remove_simple_chunks(line)
        for pos, sign in enumerate(simplified_line[1:], start=1):
            if sign in close_signs:
                prev_sign = simplified_line[pos - 1]
                if (
                    prev_sign in open_signs
                    and prev_sign != open_signs[close_signs.index(sign)]
                ):
                    dprint(
                        f"{line} - "
                        f"Expected {close_signs[open_signs.index(prev_sign)]}, "
                        f"but found {sign} instead."
                    )
                    syntax_error_score += sign_scores[close_signs.index(sign)]
                    break

    return syntax_error_score


def solution2(**kwargs) -> int:
    open_signs = "([{<"
    close_signs = ")]}>"
    lines = kwargs["raw_data"]
    dprint(f"Found {len(lines)} lines.")
    corrupted_lines = []
    for line_number, line in enumerate(kwargs["raw_data"]):
        simplified_line = remove_simple_chunks(line)
        for pos, sign in enumerate(simplified_line[1:], start=1):
            if sign in close_signs:
                prev_sign = simplified_line[pos - 1]
                if (
                    prev_sign in open_signs
                    and prev_sign != open_signs[close_signs.index(sign)]
                ):
                    corrupted_lines.append(line_number)
                    break
    dprint(f"Found {len(corrupted_lines)} corrupted lines.")

    line_scores = []
    for line in [
        remove_simple_chunks(l)
        for ln, l in enumerate(lines)
        if ln not in corrupted_lines
    ]:
        line_score = 0
        for sign in line[::-1]:
            line_score = 5 * line_score + (open_signs.index(sign) + 1)
        line_scores.append(line_score)
    dprint(line_scores)
    return median(line_scores)


def remove_simple_chunks(line: str) -> str:
    while True:
        new_line = re.sub(r"(\(\)|\[\]|\{\}|\<\>)", "", line)
        if new_line == line:
            break
        line = new_line
    return line


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
