import pathlib


def main():
    data = load_data("d05.data")
    print(f"data length: {len(data)}")
    print(data)


    print(f"solution part one: {solution1(data)}")
    print(f"solution part two: {solution2(data)}")


def solution1(data):
    print(f"Start: {len(data[0])} units")
    #print(data[0])
    polymere = reactions(1,data[0])
    #print(polymere)
    return len(polymere)

def solution2(data):
    return 0

def reactions(round, polymere):
    letters = "absdefghijklmnopqrstuvwxyz"
    units = list(unit+unit.upper() for unit in letters) + list(unit.upper()+unit for unit in letters)
    polymere_length = len(polymere)
    
    for unit in units:
        a = len(polymere)
        polymere = polymere.replace(unit, "")
        reaction_count = int((a-len(polymere))/2)
        if reaction_count > 0:
            print(f"replace '{unit}', {reaction_count} reations")
    
    print(f"Round {round}: {int((polymere_length - len(polymere))/2):d} reactions, {len(polymere)} units left")

    if len(polymere) < polymere_length:   
        polymere = reactions(round + 1, polymere)
        pass
    
    #print(polymere)
    return polymere
    
    

def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return inputFile.read().split("\n")


if __name__ == "__main__":
    main()
