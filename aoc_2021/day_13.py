""" https://adventofcode.com/2021/day/11 """

import re
from adventofcode import LOG

questions = [
    "How many dots are visible after completing just the first fold instruction on your transparent paper?",  # noqa: E501
    "What code do you use to activate the infrared thermal imaging camera system?",
]


def part_one(**kwargs):

    paper_points = set(
        (int(line.split(",")[0]), int(line.split(",")[1]))
        for line in kwargs["raw_data"].split("\n")
        if re.search(r"\d+,\d+", line)
    )

    point_count = {}

    for index, instruction in enumerate(
        [line for line in kwargs["raw_data"].split("\n") if re.search(r"fold", line)],
        start=1,
    ):
        match = re.match(r".*(?P<axis>[xy])=(?P<value>\d+)", instruction)

        if match.group("axis") == "x":
            paper_points = fold_paper_x(paper_points, int(match.group("value")))
        else:
            paper_points = fold_paper_y(paper_points, int(match.group("value")))

        point_count[index] = len(paper_points)
        LOG.debug(f"{len(paper_points)} points after {index}. {instruction=}")

    return questions[0], point_count[1]


def part_two(**kwargs):

    paper_points = set(
        (int(line.split(",")[0]), int(line.split(",")[1]))
        for line in kwargs["raw_data"].split("\n")
        if re.search(r"\d+,\d+", line)
    )

    for instruction in [
        line for line in kwargs["raw_data"].split("\n") if re.search(r"fold", line)
    ]:
        match = re.match(r".*(?P<axis>[xy])=(?P<value>\d+)", instruction)

        if match.group("axis") == "x":
            paper_points = fold_paper_x(paper_points, int(match.group("value")))
        else:
            paper_points = fold_paper_y(paper_points, int(match.group("value")))

    return questions[1], print_paper(paper_points)


def fold_paper_x(paper_points: list, value: int) -> list:
    return set(((2 * value - x) if x > value else x, y) for x, y in paper_points)


def fold_paper_y(paper_points: list, value: int) -> list:
    return set((x, (2 * value - y) if y > value else y) for x, y in paper_points)


def print_paper(paper: set) -> str:
    xmax = max(x for x, _ in paper) + 1
    ymax = max(y for _, y in paper) + 1
    output = "\n"
    for y in range(ymax):
        for x in range(xmax):
            if (x, y) in paper:
                output += "*"
            else:
                output += " "
        output += "\n"
    return output
