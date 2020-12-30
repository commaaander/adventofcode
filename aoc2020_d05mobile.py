def main():
    boardingPasses = open("data/d05mobile.data").read().splitlines()
    # boardingPasses=["FBFBBFFRLR"] #, "BBFBFBFLLL", "FFBBBFBLLL", "BFBFBFBRLR", "BFFFFFFLRR", "FBBFFBFRRL", "BFBBBBBLLL", "FBBBBFBRRL", "FFFBBBFLRR", "BBFFFFBRLL"]
    #print(boardingPasses)
    maxBpid = 0
    for boardingPass in boardingPasses:
        maxBpid = max(maxBpid, calcBPID(boardingPass))
    
    print(f'Highest Boarding pass ID: {maxBpid}')


def calcBPID(boardingPass):
    row = calcRow(boardingPass[:7], 0, 127)
    column = calcColumn(boardingPass[-3:], 0, 7)
    bpid = row * 8 + column
    # print(f'{bpid} → Row: {row}, Column: {column} ')
    return bpid

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

if __name__ == '__main__':
    main()


