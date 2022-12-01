""" https://adventofcode.com/2022/day01 """

from adventofcode import LOG

questions = [
    "Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?",
    "Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?",
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")

    calories_list = kwargs["raw_data"].split("\n")

    calories_per_elf = []
    calories = 0
    for c in calories_list:
        if c == "":
            calories_per_elf.append(calories)
            calories = 0
        else:
            calories += int(c)

    return questions[0], max(calories_per_elf)


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")

    calories_list = kwargs["raw_data"].split("\n")

    calories_per_elf = []
    calories = 0
    for c in calories_list:
        if c == "":
            calories_per_elf.append(calories)
            calories = 0
        else:
            calories += int(c)

    return questions[1], sum(sorted(calories_per_elf, reverse=True)[:3])
