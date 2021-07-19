import re
import pathlib

def main():
    data = load_data("d03.data")
    # print(data)
    # print(sorted(data))
    print(f"number of data sets: {len(data)}")

    print(f"solution part one: {solution1(data)}")
    # print(f"solution part two: {solution2(data)}")


def solution1(data):
    fabric = {}

    for claim in data:

        # print(claim)

        match = re.search("^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$", claim)
        claim_id, claim_x_pos, claim_y_pos, claim_length, claim_height = match.groups()

        for x in range(int(claim_length)):
            for y in range(int(claim_height)):
                try:
                    fabric[f"{int(claim_x_pos)+x:04d}-{int(claim_y_pos)+y:04d}"] += 1
                except KeyError as ke:
                    fabric[f"{int(claim_x_pos)+x:04d}-{int(claim_y_pos)+y:04d}"] = 1

    # print(fabric)
    print(f"{len(fabric)} entries in fabric")

    return sum(1 for i in fabric.values() if i >= 2)
    

def solution2(data):
    pass


def load_data(filename):

    with open(f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}") as inputFile:
        return inputFile.read().split("\n")


if __name__ == "__main__":
    main()
