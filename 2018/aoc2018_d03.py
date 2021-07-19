import re

def main():
    data = load_data("d03.data")
    #print(data)
    #print(sorted(data))
    print(f"number of data sets: {len(data)}")
    
    print(f"solution part one: {solution1(data)}")
    #print(f"solution part two: {solution2(data)}")
    

            
def solution1(data):
    fabric = {}
    
    for claim in data[:10]:
        
        #print(claim)
        
        match = re.search('^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$', claim)
        claim_id, claim_x_pos, claim_y_pos, claim_length, claim_height = match.groups()         
        
        for x in range(int(claim_length)):
            for y in range(int(claim_height)):
                try:
                    fabric[f"{int(claim_x_pos)+x:04d}-{int(claim_y_pos)+y:04d}"] += 1
                except KeyError as ke:
                    fabric[f"{int(claim_x_pos)+x:04d}-{int(claim_y_pos)+y:04d}"] = 0
        
    
    multi_claims_count = len()
    print(fabric)
    
    
    
def solution2(data):
    pass


def load_data(filename):
    with open(f"data/{filename}") as inputFile:
        return inputFile.read().split("\n")


if __name__ == '__main__':
    main()
