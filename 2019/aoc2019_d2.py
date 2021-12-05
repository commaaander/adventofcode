import pathlib

input_file = (
    f"{pathlib.Path(__file__).parent.absolute()}"
    f"/data/{pathlib.Path(__file__).stem}.data"
)


def main():

    with open(input_file) as input_data:
        program = input_data.read().split(",")

    print(
        f"\nPart 1\n*******\nvalue at position 0: "
        f"{part1(list(map(int, program)), 12, 2)}\n"
    )

    print(f"\nPart 2\n*******\nnoun-verb-value: {part2(list(map(int, program)))}\n")


def part1(program, noun, verb):

    program[1] = noun
    program[2] = verb

    i = 0

    while program[i] != 99:
        # print(f"[{i: 4}]:{program[i:i+4]}")

        if program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]

        elif program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]

        else:
            print("upss")
        i += 4
    return program[0]


def part2(program):

    for verb in range(100):
        for noun in range(100):
            output = part1(program.copy(), noun, verb)
            if output == 19690720:
                print(f"noun:{noun: 2} verb:{verb: 2} output: {output: 2}")
                return 100 * noun + verb

    raise RuntimeError("Something went wrong")


if __name__ == "__main__":
    main()
