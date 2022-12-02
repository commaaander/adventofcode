""" https://adventofcode.com/2022/dayXX """

from adventofcode import LOG

questions = [
    "What would your total score be if everything goes exactly according to your strategy guide?",
    "Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according"
    "to your strategy guide?",
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")

    selection_points = {"X": 1, "Y": 2, "Z": 3}
    outcome_points = {
        "X": {"A": 3, "B": 0, "C": 6},
        "Y": {"A": 6, "B": 3, "C": 0},
        "Z": {"A": 0, "B": 6, "C": 3},
    }
    total_score = 0
    for round in kwargs["raw_data"].split("\n"):

        opponents_choose, your_choose = round.split(" ")
        total_score += selection_points[your_choose]
        total_score += outcome_points[your_choose][opponents_choose]

    return questions[0], total_score


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")

    selection_points = {"X": 0, "Y": 3, "Z": 6}
    outcome_points = {
        "X": {"A": 3, "B": 1, "C": 2},
        "Y": {"A": 1, "B": 2, "C": 3},
        "Z": {"A": 2, "B": 3, "C": 1},
    }
    total_score = 0
    for round in kwargs["raw_data"].split("\n"):

        opponents_choose, your_choose = round.split(" ")
        total_score += selection_points[your_choose]
        total_score += outcome_points[your_choose][opponents_choose]

    return questions[1], total_score
