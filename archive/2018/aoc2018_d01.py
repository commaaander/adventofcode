def main():
    data = load_data("d01.data")
    # print(data)
    print(f"number of data sets: {len(data)}")

    print(f"solution part one: resulting frequency is {solution1(data)}")
    print(f"solution part two: first frequency twice reached is: {solution2(data)}")


def solution1(data):
    return sum(data)


def solution2(data):

    cur_freq = 0
    frequencies = {0}

    while True:
        for freq_change in data:
            cur_freq += freq_change
            if cur_freq in frequencies:
                return cur_freq
            else:
                frequencies.add(cur_freq)
    return cur_freq


def load_data(filename):
    with open(f"data/{filename}") as inputFile:
        return list(int(val) for val in inputFile.read().split("\n"))


if __name__ == "__main__":
    main()
