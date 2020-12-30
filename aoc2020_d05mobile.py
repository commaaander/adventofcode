boardingPasses = []
seats = {}

def main():
    global boardingPasses, seats
    dataFile = open("data/d05mobile.data") 
    boardingPasses = dataFile.read().splitlines()
    dataFile.close()
    print(f"Read {len(boardingPasses)} boarding passes")
    
    solutionPart1()
    solutionPart2()
    

def solutionPart1():
    global boardingPasses, seats
    maxBpid = 0

    for boardingPass in boardingPasses:
        bpid, row, column = calcBPID(boardingPass)
        # print(f'{bpid} → Row: {row}, Column: {column} ')
        if row not in seats:
            seats[row] = {}
        seats[row][column] = {"code": boardingPass, "id": bpid}
        maxBpid = max(maxBpid, bpid)
        
    print(f'Solution part1: highest boarding pass ID: {maxBpid}')
    

def solutionPart2():
    global seats
    for row in sorted(seats)[1:-1]:
        if len(seats[row]) != 8:
            for column in range(8):
                if column not in seats[row]:
                    print(f"Solution part2: row {row}, column {column}, code {calcBPCode(row,column)}, ID {row * 8 + column}")
    

def calcBPID(boardingPass):
    row = calcRow(boardingPass[:7], 0, 127)
    column = calcColumn(boardingPass[-3:], 0, 7)
    bpid = row * 8 + column
    return bpid, row, column

def calcRow(code, low, high):
    # print(code[0], low, high)
    retVal = 0
    if code[0] == 'F':
        if low != high - 1:
            return calcRow(code[1:], low, ((high - low + 1) / 2 + low) - 1)
        else:
            return low
    else:
        if low != high - 1:
            return calcRow(code[1:], (high - low + 1) / 2 + low, high)
        else:
            return high
            
            
def calcColumn(code, low, high):
    # print(code[0], low, high)
    retVal = 0
    if code[0] == 'L':
        if low != high - 1:
            return calcColumn(code[1:], low, ((high - low + 1) / 2 + low) - 1)
        else:
            return low
    else:
        if low != high - 1:
            return calcColumn(code[1:], (high - low + 1) / 2 + low, high)
        else:
            return high
    return low


def calcBPCode(row, column):
    bpcode = str(bin(int(row))[2:]).replace("1", "B").replace("0", "F").rjust(7, "F")
    bpcode += str(bin(int(column))[2:]).replace("1", "R").replace("0", "L").rjust(3, "L")
    
    return bpcode


if __name__ == '__main__':
    main()

