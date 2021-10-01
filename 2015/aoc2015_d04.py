import hashlib


def main():
    print(f"solution part one: {solution1()}")
    print(f"solution part two: {solution2()}")


def solution1(puzzle_input: str = "bgvyzdsv", zero_length = 5):
    number = 0
    hash = hashlib.md5(puzzle_input.encode()).hexdigest()[:zero_length]
    while hash[:zero_length] != zero_length * '0':
        number += 1
        hash = hashlib.md5(
            f"{puzzle_input}{number:d}".encode()).hexdigest()[:zero_length]
    return number


def solution2():
    return solution1(zero_length=6)


if __name__ == "__main__":
    main()
