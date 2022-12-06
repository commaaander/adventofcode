import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from os.path import basename
from rich import print

""" https://adventofcode.com/2021/day/8 """


def main():

    # get command line args
    cmdl_parser = init_cmdl_parser()
    cmdl_args = cmdl_parser.parse_args()

    # load data
    raw_data = load_data(cmdl_args.debug).read().split("\n")

    question = "In the output values, how many times do digits 1, 4, 7, or 8 appear?"
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part one:[/yellow]\n{question} {solution}")

    question = "What do you get if you add up all of the output values?"
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"[yellow]Solution part two:[/yellow]\n{question} {solution}")


def solution1(**kwargs) -> int:
    sum = 0
    for output_value in [
        line.split("|")[1].strip().split(" ") for line in kwargs["raw_data"]
    ]:
        for v in output_value:
            if len(v) in [2, 3, 4, 7]:
                sum += 1
    return sum


def solution2(**kwargs) -> int:
    sum = 0
    for entry in kwargs["raw_data"]:
        signal_patterns = [set(e) for e in entry.split("|")[0].strip().split(" ")]
        output_values = [set(v) for v in entry.split("|")[1].strip().split(" ")]

        # recognize digits
        digits = {}
        digits["1"] = next(d for d in signal_patterns if len(d) == 2)
        digits["7"] = next(d for d in signal_patterns if len(d) == 3)
        digits["4"] = next(d for d in signal_patterns if len(d) == 4)
        digits["8"] = next(d for d in signal_patterns if len(d) == 7)
        digits["9"] = next(
            d for d in signal_patterns if len(d) == 6 and d.union(digits["4"]) == d
        )
        digits["0"] = next(
            d
            for d in signal_patterns
            if len(d) == 6 and d.union(digits["7"]) == d and d.union(digits["9"]) != d
        )
        digits["6"] = next(
            d
            for d in signal_patterns
            if len(d) == 6 and d.union(digits["0"]) != d and d.union(digits["9"]) != d
        )
        digits["3"] = next(
            d for d in signal_patterns if len(d) == 5 and d.union(digits["1"]) == d
        )
        digits["5"] = next(
            d
            for d in signal_patterns
            if len(d) == 5 and d.union(digits["4"].difference(digits["1"])) == d
        )
        digits["2"] = next(
            d
            for d in signal_patterns
            if len(d) == 5 and d.union(digits["5"]) != d and d.union(digits["3"]) != d
        )

        # sum up output values
        sum += int(
            "".join(
                next(n for n in digits.keys() if digits[n] == value)
                for value in output_values
            )
        )
    return sum


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
