""" https://adventofcode.com/2021/day/11 """

from itertools import product
from adventofcode import LOG

FLASH_COUNTER = 0

questions = [
    "How many total flashes are there after 100 steps?",  # noqa: E501
    "What is the first step during which all octopuses flash?",
]


def part_one(**kwargs):
    global FLASH_COUNTER
    steps = 100
    octo_map = create_octo_map(kwargs["raw_data"])

    LOG.debug("Start:")
    LOG.debug(print_octopuses(octo_map))

    for i in range(steps):

        for x, y in octo_map:
            octo_map[(x, y)] += 1
        for x, y in octo_map:
            if octo_map[(x, y)] > 9:
                flash_octopus(x, y, octo_map)

        LOG.debug(f"After Step {i+1}:")
        LOG.debug(print_octopuses(octo_map))

    return questions[0], FLASH_COUNTER


def part_two(**kwargs):
    octo_map = create_octo_map(kwargs["raw_data"])
    step = 0
    while sum(v for v in octo_map.values()) > 0:
        step += 1

        for x, y in octo_map:
            octo_map[(x, y)] += 1
        for x, y in octo_map:
            if octo_map[(x, y)] > 9:
                flash_octopus(x, y, octo_map)

        LOG.debug(f"After Step {step}:")
        LOG.debug(print_octopuses(octo_map))
    return questions[1], step


def create_octo_map(input_data: list) -> dict:
    octo_map = {}
    for y, row in enumerate(input_data.split("\n")):
        for x, value in enumerate(row):
            octo_map[(x, y)] = int(value)
    return octo_map


def flash_octopus(x: int, y: int, octo_map: dict) -> None:

    global FLASH_COUNTER

    deltas = [-1, 0, 1]
    octo_map[(x, y)] = 0

    for dx, dy in [c for c in product(deltas, deltas) if c != (0, 0)]:
        try:
            if octo_map[(x + dx, y + dy)] > 0:
                octo_map[(x + dx, y + dy)] += 1
                if octo_map[(x + dx, y + dy)] > 9:
                    flash_octopus(x + dx, y + dy, octo_map)

        except KeyError:
            pass
    FLASH_COUNTER += 1
    return


def print_octopuses(octo_map: dict) -> str:
    xmax = max(x for x, _ in octo_map.keys()) + 1
    ymax = max(y for _, y in octo_map.keys()) + 1
    output = ""
    for y in range(ymax):
        output += f"{y:3d}\t"
        for x in range(xmax):
            output += f"{octo_map[(x, y)]}"
        output += "\n"
    return output
