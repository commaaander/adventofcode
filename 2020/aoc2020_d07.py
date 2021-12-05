import re

bags = {}
specialColor = "shiny gold"


def main():
    global bags

    with open("data/d07.data") as inputFile:
        bagContentRules = inputFile.read().split("\n")

    for bagContentRule in bagContentRules:
        # print(bagContentRule)

        bagMatches = re.compile(r"\d*\s*\w+ \w+ bag").findall(bagContentRule)

        for bag in bagMatches[1:]:
            # print(bag)

            if "no other bag" not in bag:

                bagType = re.compile(r"\w+ \w+ bag").findall(bag)[0]
                bagCount = re.compile(r"\d+").findall(bag)[0]

                if bagMatches[0] not in bags:
                    bags[bagMatches[0]] = {}
                bags[bagMatches[0]][bagType] = bagCount
            else:
                bags[bagMatches[0]] = {}

    # print(bags)
    print(f"{len(bags)} bags identified.\n")

    print(f"Solution part 1: {solutionPart1()} bags found")
    print(f"Solution part 2: {solutionPart2()} bags found.\n")


def solutionPart1():
    global bags
    bagCount = 0
    i = 0

    for bag in bags.keys():
        i += 1
        found = bagContainsSpecialBag(bag, 0)
        if found:
            # print(f"{i:3d} Found the searched bag in '{bag}'")
            bagCount += 1

    return bagCount


def solutionPart2():
    global bags
    global specialColor
    sum = 0

    sum += countSpecialBagContent(bags[f"{specialColor} bag"], 0)

    return sum


def bagContainsSpecialBag(bag, recLevel):
    global specialColor
    found = False

    for bagContent in bags[bag]:
        if specialColor not in bagContent:
            found |= bagContainsSpecialBag(bagContent, recLevel + 1)
        else:
            found |= True

    return found


def countSpecialBagContent(specialColorBag, recLevel):
    global specialColor
    global bags
    sum = 0
    count = 0

    print("\t" * recLevel + f"specialColorBag: {specialColorBag}")

    if len(specialColorBag.keys()) > 0:
        for bag in specialColorBag.keys():
            if int(specialColorBag[bag]) == 0:
                count = 1
            else:
                count = int(specialColorBag[bag])
            print("\t" * recLevel + f"bag: {bag}, count: {count}")
            sum += count * countSpecialBagContent(bags[bag], recLevel + 1)
            print("\t" * recLevel + f"sum: {sum}")
    else:
        sum = 1
    return sum


if __name__ == "__main__":
    main()
