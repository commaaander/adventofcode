import re
import pathlib


def main():
    data = load_data("d04.data")
    print(f"number of data sets: {len(data)}")
    print(data)

    print(f"solution part one: {solution1(data)}")
    print(f"solution part two: {solution2(data)}")


def solution1(data):
    return 0


def solution2(data):
    return 0

def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return sorted(inputFile.read().split("\n"))


if __name__ == "__main__":
    main()
