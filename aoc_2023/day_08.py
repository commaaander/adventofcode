""" https://adventofcode.com/2023/day/8 """

from typing import Any, Dict, List, Tuple
import re
from adventofcode import LOG

questions: List[str] = [
    "How many steps are required to reach ZZZ?",
    "",  # noqa: E501
]


def part_one(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_one({kwargs=})")
    desert_map = parse_raw_data(kwargs["raw_data"])
    i: int = 0
    next_node = "AAA"
    while True:
        next_direction = desert_map["nav_instructions"][i % len(desert_map["nav_instructions"])]
        next_node = desert_map["nodes"][next_node][next_direction]
        i += 1
        LOG.debug(f"{i=} -> {next_node=}")
        if next_node == "ZZZ":
            break
    return questions[0], i


# erster_schluessel = next(iter(mein_dict))
# erster_wert = mein_dict[erster_schluessel]


def part_two(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_two({kwargs=})")
    answer: int = 0
    return questions[1], answer


def parse_raw_data(raw_data: str) -> Dict[str, str | List[str]]:
    parsed_raw_data = [row for row in raw_data.splitlines()]
    parsed_data: Dict[str, str | List[str]] = {}
    parsed_data["nav_instructions"] = parsed_raw_data[0]
    parsed_data["nodes"] = {}
    for row in parsed_raw_data[2:]:
        match = re.search(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", row)
        parsed_data["nodes"][match.group(1)] = {"L": match.group(2), "R": match.group(3)}
    return parsed_data
