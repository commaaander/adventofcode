import pathlib
import sys

def main():
    sys.setrecursionlimit(10000)

    data = load_data("d05.data")
    print(f"data length: {len(data)}")

    print(f"solution part one: {solution1(data)}")
    print(f"solution part two: {solution2(data)}")


def solution1(data):
    print(f"Start: {len(data[0])} units")
    return len(reactions(1, data[0]))


def solution2(data):

    results = {}
    for unit in "abcdefghijklmnopqrstuvwxyz":
        polymere = data[0].replace(unit, "").replace(unit.upper(), "")
        results[unit] = len(reactions(1, polymere))
        # print(f"Unit: {unit}, result: {results[unit]} ")

    return min(results.values())


def reactions(round, polymere):
    letters = "abcdefghijklmnopqrstuvwxyz"
    units = list(unit + unit.upper() for unit in letters) + list(
        unit.upper() + unit for unit in letters
    )
    polymere_length = len(polymere)

    for unit in units:
        polymere = polymere.replace(unit, "")

    # print(
    #     f"Round {round}: {int((polymere_length - len(polymere))/2):d} reactions, {len(polymere)} units left"
    # )

    if len(polymere) < polymere_length:
        polymere = reactions(round + 1, polymere)

    return polymere


def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return inputFile.read().split("\n")


if __name__ == "__main__":
    main()
