with open("data/d07.data", "r") as text:
    bags = text.read().split(".\n")


def parentbag(childbag):
    for parent in bags_dict:
        content = bags_dict[parent]
        if childbag in content:
            parentbag(parent)
            bagset.add(parent)
    return


bags_dict = {}
for bag in bags:
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
    bag = bag.split(" contain ")
    bags_dict[bag[0]] = bag[1]

bagset = set()
parentbag("shiny gold")
print(
    "Part 1: The amount of different coloured bags that can hold a shiny gold bag: "
    + str(len(bagset))
)


def add_child(parent_bag):

    content = bags_dict[parent_bag].split(", ")
    if content[0] == "no other":
        return
    else:
        for child in content:
            bagname = child[2:]
            number = int(child[0])
            if bagname in children_counting:
                children_counting[bagname] += number
            else:
                children_counting[bagname] = number
            for i in range(number):
                add_child(bagname)
        return


children_counting = {}
add_child("shiny gold")
print("Part 2: Total number of bags: " + str(sum(children_counting.values())))
