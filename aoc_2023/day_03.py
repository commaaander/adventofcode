""" https://adventofcode.com/2022/day/3 """

import re
from typing import Any, Dict, List, Tuple, Set

from adventofcode import LOG
from rich import print

questions: List[str] = [
    "What is the sum of all of the part numbers in the engine schematic?",
    "What is the sum of all of the gear ratios in your engine schematic?",
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
        print(f"{row_number:03d}: [red][/red] {colorize_numbers(row, 'red', row_nonpart_numbers)}".replace(".", " "))
        part_numbers.extend(row_part_numbers)
        nonpart_numbers.extend(row_nonpart_numbers)
    LOG.debug(f"{len(part_numbers)} parts. {sorted(part_numbers)=}, {sorted(nonpart_numbers)=}")
    return questions[0], sum(part_numbers)


def part_two(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_two({kwargs=})")
    answer: int = 0
    engine_schematic: List[str] = kwargs["raw_data"].splitlines()
    parts_list: List[Dict[str, int]] = []
    for row_number, row in enumerate(engine_schematic):
        match = list(re.finditer(r"\d+", row))
        if match:
            for m in match:
                parts_list.append({"number": int(m.group(0)), "row": row_number, "start": m.start(), "end": m.end()})
    for row_number, row in enumerate(engine_schematic):
        for gear_position in [x for x, char in enumerate(row) if char == "*"]:
            parts_around: List[int] = get_parts_around(engine_schematic, row_number, gear_position, parts_list)
            if len(parts_around) == 2:
                answer += parts_around[0] * parts_around[1]

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


def get_parts_around(engine_schematic: List[str], row: int, column: int, parts_list: List[Dict[str, int]]) -> List[int]:
    parts: Set[int] = set()
    for row_number in [row - 1, row, row + 1]:
        for column_number in range(column - 1, column + 2):
            try:
                parts.update(
                    set(
                        part["number"]
                        for part in parts_list
                        if part["row"] == row_number and part["start"] <= column_number < part["end"]
                    )
                )

            except IndexError:
                pass
    LOG.debug(f"parts around gear at {row+1:03d}, {column+1:03d}: {list(parts)}")
    return list(parts)


def colorize_numbers(s: str, color: str, numbers: List[int]) -> str:
    for number in numbers:
        s = re.sub(r"\b" + str(number) + r"\b", f"[{color}]{number}[/{color}]", s)

    return s
