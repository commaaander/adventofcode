""" https://adventofcode.com/2022/day/4 """

from adventofcode import LOG
import re

questions = [
    "In how many assignment pairs does one range fully contain the other?",  # noqa: E501
    "In how many assignment pairs do the ranges overlap?",  # noqa: E501
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")
    answer = 0

    for assignment in kwargs["raw_data"].split("\n"):
        match = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", assignment)
        LOG.debug(f"{assignment=}, {match=}")
        a1, a2, b1, b2 = map(int, match.groups())
        if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
            answer += 1

    return questions[0], answer


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")
    answer = 0

    for assignment in kwargs["raw_data"].split("\n"):
        match = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", assignment)
        a1, a2, b1, b2 = map(int, match.groups())
        if len(set(range(a1, a2 + 1)) & set(range(b1, b2 + 1))):
            answer += 1

    return questions[1], answer
