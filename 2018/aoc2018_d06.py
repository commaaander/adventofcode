import pathlib


def main():
    raw_data = load_data("d06.data")
    print(f"data length: {len(raw_data)}")

    list_data = list({"x": int(x[0]), "y": int(x[1])}
                     for x in (le.split(", ") for le in raw_data))

    print(
        f"solution part one:\n\tWhat is the size of the largest area that isn't infinite? {solution1(list_data)}")
    pass


def solution1(data):

    print(data)
    # find boundaries
    # lower boundary: min(x)
    # upper boundary: max(x)
    # left boundary: min(y)
    # right boundary: max(x)

    # filter out all points with infinite area

    # calculate the area around all points

    # determine the largest area
    pass


def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return inputFile.read().split("\n")


if __name__ == "__main__":
    main()
