import pathlib

debug = False


def main():
    raw_data = load_data(f"d01{'_test' if debug else ''}.data")

    print(
        f"solution part one:\n\t"
        f"To what floor do the instructions take Santa? "
        f"{solution1(raw_data)}"
    )
    print(
        f"solution part one:\n\t"
        f"What is the position of the character that causes Santa to first enter the basement? "
        f"{solution2(raw_data)}"
    )
    pass


def solution1(data: str):
    return data.count("(") - data.count(")")


def solution2(data: str):
    floor = 0
    step = 0
    while floor != -1:
        floor = floor + (1 if data[step] == "(" else -1)
        step += 1
    return step


def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return inputFile.read()


if __name__ == "__main__":
    main()
