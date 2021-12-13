""" https://adventofcode.com/2021/day/11 """

from itertools import permutations


questions = [
    "Find the two entries that sum to 2020; what do you get if you multiply them together?",  # noqa: E501
    "In your expense report, what is the product of the three entries that sum to 2020?",  # noqa: E501
]


def part_one(**kwargs):

    int_data = list(int(i) for i in kwargs["raw_data"].split("\n"))
    return (
        questions[0],
        [i * j for i, j in permutations(int_data, 2) if i + j == 2020][0],
    )


def part_two(**kwargs):
    int_data = list(int(i) for i in kwargs["raw_data"].split("\n"))
    return (
        questions[0],
        [i * j * k for i, j, k in permutations(int_data, 3) if i + j + k == 2020][0],
    )
