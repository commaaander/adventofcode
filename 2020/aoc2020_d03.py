def main():
    inputFile = open("aoc2020/data/d03.data")
    inputLines = inputFile.readlines()

    results = [
        traverseMap(1, 1, inputLines)
        , traverseMap(3, 1, inputLines)
        , traverseMap(5, 1, inputLines)
        , traverseMap(7, 1, inputLines)
        , traverseMap(1, 2, inputLines)
    ]

    resultsProd = 1
    for result in results:
        print(result)
        resultsProd *= result

    print("Encountered Trees: {0}".format(resultsProd))


def traverseMap(stepX, stepY, wood):
    x = 0
    y = 0
    width = len(wood[0]) - 1

    encounteredTreesCount = 0

    while y <= len(wood) - 1:
        if wood[y][x % width] == '#':
            encounteredTreesCount += 1
        x += stepX
        y += stepY

    return encounteredTreesCount


if __name__ == "__main__":
    main()
