""" https://adventofcode.com/2023/day/15 """

from typing import Any, Dict, List, Tuple

from adventofcode import LOG
import re

questions: List[str] = [
    "What is the sum of the results?",
    "What is the focusing power of the resulting lens configuration?",
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
    boxes = {key: {} for key in range(256)}
    for step in kwargs["raw_data"].split(","):
        label = re.search((r"^[a-z]+"), step).group(0)
        box_number = get_hash(label)
        match step:
            case _ if re.search(r"=", step):
                focal_length = int(re.search(r"\d*$", step).group(0))
                boxes[box_number][label] = focal_length
            case _ if re.search(r"-", step):
                try:
                    del boxes[box_number][label]
                except KeyError:
                    pass
    for box_number, box in boxes.items():
        for slot, focal_length in enumerate(box.values()):
            answer += (box_number + 1) * (slot + 1) * focal_length
    return questions[1], answer


def get_hash(step: str) -> int:
    hash: int = 0
    for char in step:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash
