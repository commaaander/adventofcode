import re
import pathlib


def main():
    data = load_data("d03.data")
    print(f"number of data sets: {len(data)}")

    print(f"solution part one: {solution1(data)}")
    print(f"solution part two: {solution2(data)}")


def solution1(data):
    fabric = get_fabric(data)
    return sum(1 for i in fabric.values() if len(i) >= 2)


def solution2(data):
    fabric = get_fabric(data)

    solo_fabric_squares = set(i[0] for i in fabric.values() if len(i) == 1)
    for solo_fabric_square in solo_fabric_squares:
        found = False
        for fabric_square in fabric.values():
            if len(fabric_square) > 1:
                if solo_fabric_square in fabric_square:
                    found = True
                    break
        if not found:
            return solo_fabric_square
    return 0


def get_fabric(data):
    fabric = {}

    for claim in data:
        match = re.search("^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$", claim)
        claim_id, claim_x_pos, claim_y_pos, claim_length, claim_height = match.groups()
        for x in range(int(claim_length)):
            for y in range(int(claim_height)):
                coords = f"{int(claim_x_pos)+x:04d}-{int(claim_y_pos)+y:04d}"
                try:
                    if claim_id not in fabric[coords]:
                        fabric[coords].append(claim_id)
                except KeyError:
                    fabric[coords] = [claim_id]
    return fabric


def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return inputFile.read().split("\n")


if __name__ == "__main__":
    main()
