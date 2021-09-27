import pathlib


def main():
    raw_data = load_data("d06_test.data")
    print(f"data length: {len(raw_data)}")

    list_data = list({"x": int(x[0]), "y": int(x[1])}
                     for x in (le.split(", ") for le in raw_data))

    print(
        f"solution part one:\n\tWhat is the size of the largest area that isn't infinite? {solution1(list_data)}")
    pass


def solution1(data):

    print(data)
    # find boundaries
    borders = {
        "bottom": min(point["x"] for point in data),
        "top": max(point["x"] for point in data),
        "left": min(point["y"] for point in data),
        "right": max(point["y"] for point in data)
    }

    i = 1
    for x in range(borders["bottom"], borders["top"]+1):
        for y in range(borders["left"], borders["right"]+1):
            for point in data:
                print(
                    f"Point Nr. {i:07d}({x:03d}-{y:03d}) -> {point['x']:03d}-{point['y']:03d}: {getManhattanDistance({'x':x, 'y':y}, point)}", end="\n")
            i += 1


    # determine the largest area
    pass


def getManhattanDistance(point1, point2):
    return abs(point1["x"] - point2["x"]) + abs(point1["y"] - point2["y"])


def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return inputFile.read().split("\n")


if __name__ == "__main__":
    main()
