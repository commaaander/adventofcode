""" https://adventofcode.com/2023/day/8 """

import math
import re
from functools import reduce
from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "How many steps are required to reach ZZZ?",
    "How many steps does it take before you're only on nodes that end with Z",
]


def part_one(**kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({kwargs=})")
    desert_map = _parse_raw_data(kwargs["raw_data"])
    i = 0
    next_node: str = "AAA"
    while True:
        next_direction = desert_map["nav_instructions"][i % len(desert_map["nav_instructions"])]
        next_node = desert_map["nodes"][next_node][next_direction]
        i += 1
        LOG.debug(f"{i=} -> {next_node=}")
        if next_node == "ZZZ":
            break
    return questions[0], i


def part_two(**kwargs: Dict[str, Any]) -> Tuple[str, int]:
    return _part_two_v2(**kwargs)


def _part_two_v1(**kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({kwargs=})")
    desert_map = _parse_raw_data(kwargs["raw_data"])
    i = 0
    next_nodes = [node for node in desert_map["nodes"].keys() if node[-1] == "A"]
    while True:
        next_direction = desert_map["nav_instructions"][i % len(desert_map["nav_instructions"])]
        next_nodes = [desert_map["nodes"][next_node][next_direction] for next_node in next_nodes]
        i += 1
        x = [node for node in next_nodes if node[-1] == "Z"]
        if len(x) == len(next_nodes):
            break
    return questions[1], i


def _part_two_v2(**kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({kwargs=})")
    steps = []
    desert_map = _parse_raw_data(kwargs["raw_data"])
    next_nodes = [node for node in desert_map["nodes"].keys() if node[-1] == "A"]
    for node in next_nodes:
        i: int = 0
        while True:
            next_direction = desert_map["nav_instructions"][i % len(desert_map["nav_instructions"])]
            node = desert_map["nodes"][node][next_direction]
            i += 1
            if node[-1] == "Z":
                break
        LOG.debug(f"{node=}, {i=}")
        steps.append(i)
    return questions[1], _lcm_of_list(steps)


def _parse_raw_data(raw_data: str) -> Dict[str, str | List[str]]:
    parsed_raw_data = [row for row in raw_data.splitlines()]
    parsed_data = {}
    parsed_data["nav_instructions"] = parsed_raw_data[0]
    parsed_data["nodes"] = {}
    for row in parsed_raw_data[2:]:
        match = re.search(r"([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)", row)
        parsed_data["nodes"][match.group(1)] = {"L": match.group(2), "R": match.group(3)}
    return parsed_data


def _lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


def _lcm_of_list(numbers: List[int]) -> int:
    return reduce(_lcm, numbers)
