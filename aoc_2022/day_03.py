""" https://adventofcode.com/2022/day/3 """

from adventofcode import LOG

questions = [
    "Find the item type that appears in both compartments of each rucksack. "
    "What is the sum of the priorities of those item types?",
    "Find the item type that corresponds to the badges of each three-Elf group. "
    "What is the sum of the priorities of those item types?",
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")
    priorities_sum = 0
    for rucksack in kwargs["raw_data"].split("\n"):

        compartment1 = rucksack[: len(rucksack) // 2]
        compartment2 = rucksack[-len(rucksack) // 2 :]  # noqa: E203

        for letter in compartment1:
            if letter in compartment2:
                LOG.debug(f"{compartment1}|{compartment2}: {letter=} {ord(letter)=}")
                priorities_sum += priority(letter)
                break
    return questions[0], priorities_sum


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")
    priorities_sum = 0

    rucksacks = iter(kwargs["raw_data"].split("\n"))
    try:
        while True:
            letter_set = set(next(rucksacks)) & set(next(rucksacks)) & set(next(rucksacks))
            priorities_sum += priority(letter_set.pop())
    except StopIteration:
        pass

    return questions[1], priorities_sum


def priority(letter: str) -> int:
    priority = ord(letter) - 96
    if priority < 0:
        priority += 58
    return priority
