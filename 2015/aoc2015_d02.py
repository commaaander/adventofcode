import pathlib
import re
from functools import reduce

debug = False


def main():
    raw_data = load_data(f"d02{'_test' if debug else ''}.data")

    print(f"solution part one:\n\t"
          f"How many total square feet of wrapping paper should they order? "
          f"{solution1(raw_data)}")
    print(f"solution part one:\n\t"
          f"How many total feet of ribbon should they order? "
          f"{solution2(raw_data)}")
    pass


def solution1(present_list):

    wrapping_paper_length = 0

    for index, present in enumerate(present_list):

        match = re.match('(?P<l>[0-9]+)x(?P<w>[0-9]+)x(?P<h>[0-9]+)', present)
        size = match.groupdict()

        wrapping_paper_length += 2 * int(size['l']) * int(size['w'])
        wrapping_paper_length += 2 * int(size['w']) * int(size['h'])
        wrapping_paper_length += 2 * int(size['h']) * int(size['l'])
        wrapping_paper_length += min([
            int(size['l']) * int(size['w']),
            int(size['w']) * int(size['h']),
            int(size['h']) * int(size['l'], )
        ])

    return wrapping_paper_length


def solution2(present_list):
    ribbon_length = 0

    for index, present in enumerate(present_list):

        match = re.match('(?P<l>[0-9]+)x(?P<w>[0-9]+)x(?P<h>[0-9]+)', present)

        # get a sorted list of the int values found by regex
        side_lengths = sorted(int(i) for i in match.groupdict().values())

        ribbon_length += 2 * side_lengths[0]
        ribbon_length += 2 * side_lengths[1]
        ribbon_length += reduce(lambda a, b: a * b, side_lengths)

    return ribbon_length


def load_data(filename):

    with open(f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
              ) as inputFile:
        return inputFile.read().split('\n')


if __name__ == "__main__":
    main()
