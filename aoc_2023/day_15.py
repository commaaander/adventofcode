""" https://adventofcode.com/2023/day/15 """

from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What is the sum of the results?",
    "",  # noqa: E501
]


def part_one(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_one({kwargs=})")
    answer: int = 0
    for step in kwargs["raw_data"].split(","):
        answer += int(get_hash(step))
    return questions[0], answer


def part_two(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_two({kwargs=})")
    answer: int = 0
    return questions[1], answer


def get_hash(step: str) -> int:
    hash: int = 0
    for char in step:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash
