import difflib

def main():
    data = load_data("d02.data")
    #print(data)
    #print(sorted(data))
    print(f"number of data sets: {len(data)}")
    
    print(f"solution part one: checksum is {solution1(data)}")
    #print(f"solution part two: {solution2(sorted(data))}")
    print(f"solution part two: {solution2(data)}")
    
            
def solution1(data):
    two_letter_string_count = 0
    three_letter_string_count = 0
    
    for box_id in data:
        
        two_letters_found = 0
        three_letters_found = 0
        
        for letter in list(set(box_id)):
            
            
            if box_id.count(letter) == 2:
                two_letters_found = 1
            
            if box_id.count(letter) == 3:
                three_letters_found = 1
        
        two_letter_string_count += two_letters_found
        three_letter_string_count += three_letters_found
    
    return two_letter_string_count*three_letter_string_count

    
def solution2(data):
    count = 0
    check_string(count, data[0],data[1:])


def check_string(count, test_string, string_list):
    for test_string2 in string_list:
        count += 1
        diffs = list(diff for diff in difflib.ndiff(test_string,test_string2) if diff[0] != ' ')
        #print(f"{count:05d}: {test_string} -> {test_string2}: {len(diffs)} changes")
        #print(diffs)
        if len(diffs) == 2:
            print(f"{count:05d}: {test_string} -> {test_string2}: {diffs} changes")
            print(diffs)
    if len(string_list) > 1:
        check_string(count, string_list[0], string_list[1:])
    return 

def load_data(filename):
    with open(f"data/{filename}") as inputFile:
        return inputFile.read().split("\n")


if __name__ == '__main__':
    main()
