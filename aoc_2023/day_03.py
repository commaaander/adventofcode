""" https://adventofcode.com/2022/day/3 """

import re
from typing import Any, Dict, List, Tuple

from adventofcode import LOG
from rich import print

questions: List[str] = [
    "What is the sum of all of the part numbers in the engine schematic?",
    "",  # noqa: E501
]


def part_one(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_one({kwargs=})")
    part_numbers: List[int] = []
    nonpart_numbers: List[int] = []

    engine_schematic: List[str] = kwargs["raw_data"].splitlines()
    for row_number, row in enumerate(engine_schematic):
        match = re.findall(r"\d+", row)
        row_part_numbers: List[int] = []
        row_nonpart_numbers: List[int] = []

        if match:
            for number in match:
                start, end = re.search(r"\b" + number + r"\b", row).span()
                if is_symbol_adjacent(engine_schematic, row_number, start, end):
                    row_part_numbers.append(int(number))
                else:
                    row_nonpart_numbers.append(int(number))
        print(f"{row_number:03d}: [red][/red] {colorize_numbers(row, 'red', row_nonpart_numbers)}".replace(".", "."))
        part_numbers.extend(row_part_numbers)
        nonpart_numbers.extend(row_nonpart_numbers)
    LOG.debug(f"{len(part_numbers)} parts. {sorted(part_numbers)=}, {sorted(nonpart_numbers)=}")
    return questions[0], sum(part_numbers)


def part_two(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_two({kwargs=})")
    answer: int = 0
    return questions[1], answer


def is_symbol_adjacent(engine_schematic: List[str], row: int, start: int, end: int) -> bool:
    for row_number in [row - 1, row, row + 1]:
        for column_number in range(start - 1, end + 1):
            try:
                char = engine_schematic[row_number][column_number]
                if not (char.isdigit() or char == "."):
                    return True
            except IndexError:
                pass
    return False


def colorize_numbers(s: str, color: str, numbers: List[int]) -> str:
    for number in numbers:
        s = re.sub(r"\b" + str(number) + r"\b", f"[{color}]{number}[/{color}]", s)

    return s
