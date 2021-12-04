import argparse
import pathlib
import re
import sys
from io import TextIOWrapper
from itertools import islice
from os.path import basename

""" https://adventofcode.com/2021/day/4 """


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

    question = "What will your final score be if you choose that board?"
    solution = solution1(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"Solution part one:\n\t{question}: {solution}")

    question = ""
    solution = solution2(raw_data=raw_data, debug=cmdl_args.debug)
    print(f"Solution part one:\n\t{question}: {solution}")


def solution1(**kwargs) -> int:
    numbers, boards = create_boards(kwargs["raw_data"])
    drawn_numbers = set()
    for number in numbers:
        drawn_numbers.add(number)
        for board_index, board_sets in boards.items():
            for board_set in board_sets:
                if board_set.intersection(drawn_numbers) == board_set:
                    print(f"Bingo! {number} on board {board_index} {board_set}")
                    all_board_numbers = set()
                    for board_set in board_sets:
                        all_board_numbers = all_board_numbers.union(board_set)
                    return number * sum(all_board_numbers.difference(drawn_numbers))
    return 0


def solution2(**kwargs) -> int:
    numbers, boards = create_boards(kwargs["raw_data"])
    drawn_numbers = set()
    for number in numbers:
        drawn_numbers.add(number)
        for board_index, board_sets in boards.items():
            for board_set in board_sets:
                if board_set.intersection(drawn_numbers) == board_set:
                    print(f"Bingo! {number} on board {board_index} {board_set}")
                    all_board_numbers = set()
                    for board_set in board_sets:
                        all_board_numbers = all_board_numbers.union(board_set)
                    return number * sum(all_board_numbers.difference(drawn_numbers))
    return 0


def create_boards(board_data: list):
    boards = dict()
    draw_numbers = [int(i) for i in board_data[0].split(",")]
    for index, data in enumerate(chunk_list(board_data[1:], 6), start=1):
        boards[index] = []
        # rows
        rows = []
        for number_list in data[1:]:
            rows.append(
                tuple(int(i) for i in number_list.strip().replace("  ", " ").split(" "))
            )
        # columns
        columns = []
        for i in range(len(rows[0])):
            columns.append(tuple(j[i] for j in rows))

        boards[index] = [set(row) for row in rows] + [set(column) for column in columns]
    return draw_numbers, boards


def chunk_list(list, size):
    it = iter(list)
    return iter(lambda: tuple(islice(it, size)), ())


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
