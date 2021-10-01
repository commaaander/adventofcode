import pathlib

debug = False


def main():
    raw_data = load_data(f"d03{'_test' if debug else ''}.data")

    print(f"solution part one:\n\t"
          f"How many houses receive at least one present? "
          f"{solution1(raw_data)}")
    print(f"solution part one:\n\t"
          f"This year, how many houses receive at least one present "
          f"{solution2(raw_data)}")


def solution1(directions: str):
    visited_houses = {}
    cur_pos_x = 0
    cur_pos_y = 0

    visited_houses[f"{cur_pos_x:04d}-{cur_pos_y:04d}"] = 1

    for direction in directions:

        if direction == '>':
            cur_pos_x += 1
        elif direction == '^':
            cur_pos_y += 1
        elif direction == '<':
            cur_pos_x -= 1
        elif direction == 'v':
            cur_pos_y -= 1
        try:
            visited_houses[f"{cur_pos_x:04d}-{cur_pos_y:04d}"] += 1
        except KeyError:
            visited_houses[f"{cur_pos_x:04d}-{cur_pos_y:04d}"] = 1

    return len(visited_houses)


def solution2(directions: str):
    visited_houses = {}

    elf_pos_x = 0
    elf_pos_y = 0

    robo_pos_x = 0
    robo_pos_y = 0

    step = 0

    visited_houses[f"{elf_pos_x:04d}-{elf_pos_y:04d}"] = 2

    while step < len(directions):
        direction = directions[step]
        if direction == '>':
            elf_pos_x += 1
        elif direction == '^':
            elf_pos_y += 1
        elif direction == '<':
            elf_pos_x -= 1
        elif direction == 'v':
            elf_pos_y -= 1
        try:
            visited_houses[f"{elf_pos_x:04d}-{elf_pos_y:04d}"] += 1
        except KeyError:
            visited_houses[f"{elf_pos_x:04d}-{elf_pos_y:04d}"] = 1
        step += 1

        direction = directions[step]
        if direction == '>':
            robo_pos_x += 1
        elif direction == '^':
            robo_pos_y += 1
        elif direction == '<':
            robo_pos_x -= 1
        elif direction == 'v':
            robo_pos_y -= 1
        try:
            visited_houses[f"{robo_pos_x:04d}-{robo_pos_y:04d}"] += 1
        except KeyError:
            visited_houses[f"{robo_pos_x:04d}-{robo_pos_y:04d}"] = 1
        step += 1

    return len(visited_houses)


def load_data(filename):

    with open(f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
              ) as inputFile:
        return inputFile.read()


if __name__ == "__main__":
    main()
