from adventofcode import LOG

""" https://adventofcode.com/2023/day/01

--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on
it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is
unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky")
and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where
do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we
need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a
very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading
the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value
that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last
digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three,
four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

"""


questions = [
    "Consider your entire calibration document. What is the sum of all of the calibration values?",  # noqa: E501
    "",  # noqa: E501
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")
    answer = 0

    for line in kwargs["raw_data"].splitlines():
        digits_line = "".join(filter(lambda x: x.isdigit(), line))
        condensed_digits_line = 10 * int(digits_line[0]) + int(digits_line[-1])
        answer += condensed_digits_line
        LOG.debug(f"part_one({digits_line=}, {condensed_digits_line=}, {answer})")

    return questions[0], answer


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")
    answer = 0

    for line in kwargs["raw_data"].splitlines():
        numbers = []
        while True:
            line = search_and_replace_numberword(line)
            if line[0].isdigit():
                numbers.append()

    return questions[1], answer


def search_and_replace_numberword(line: str) -> str:
    for number, word in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        if line.startswith(word):
            line = line.replace(word, str(number))

    return line
