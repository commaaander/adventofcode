instructions = []


def main():
    global instructions

    with open("data/d08.data") as inputFile:
        instructions = inputFile.read().split("\n")

    # print(instructions)
    retVal, acc = solutionPart1()
    print(f"Solution part 1: returned acc={acc} with retVal={retVal}\n")

    retVal, acc = solutionPart2()
    print(f"Solution part 2: returned acc={acc} with retVal={retVal}")


def solutionPart1():
    global instructions
    return run(instructions.copy())


def solutionPart2():
    global instructions
    output = ""
    print(f"program length:{len(instructions) - 1 }")
    for i in range(len(instructions)):
        # print(f"Try {i:03d}")
        newInstructionSet = instructions.copy()
        retVal = None

        if "jmp" in newInstructionSet[i]:
            newInstructionSet[i] = newInstructionSet[i].replace("jmp", "nop")
            retVal, acc = run(newInstructionSet)
            output += (
                f"JMP->NOP: Try {i:03d} returned acc=>{acc:4d}< with retVal={retVal}\n"
                if retVal != -2
                else ""
            )

        elif "nop" in newInstructionSet[i]:
            newInstructionSet[i] = newInstructionSet[i].replace("nop", "jmp")
            retVal, acc = run(newInstructionSet)
            output += (
                f"NOP->JMP: Try {i:03d} returned acc=>{acc:4d}< with retVal={retVal}\n"
                if retVal != -2
                else ""
            )

        if retVal == 0:
            print(f"Success on try {i:03d}")
            break

    print(output)
    return retVal, acc


def run(program):
    retVal = None
    acc = 0
    nextInstructionIndex = 0
    lastInstructionIndex = len(program) - 1

    while True:

        if nextInstructionIndex >= lastInstructionIndex:
            print(f"overjumping {nextInstructionIndex} > {lastInstructionIndex}")
            retVal = -1
            break

        nextInstruction = program[nextInstructionIndex]
        program[nextInstructionIndex] = ""

        if nextInstruction == "":
            retVal = -2
            break

        command = nextInstruction[:3]
        value = nextInstruction[4:]

        if command == "acc":
            acc += int(value)
            # print(f"{nextInstructionIndex:04d} {nextInstruction} -> acc={acc:04d}")
            nextInstructionIndex += 1
            continue

        if command == "jmp":
            # print(f"{nextInstructionIndex:04d} {nextInstruction} -> acc={acc:04d}")
            nextInstructionIndex += int(value)
            continue

        if command == "nop":
            # print(f"{nextInstructionIndex:04d} {nextInstruction} -> acc={acc:04d}")
            nextInstructionIndex += 1
            continue

        if nextInstructionIndex == lastInstructionIndex:
            print("success")
            retVal = 0
            break

    return retVal, acc


if __name__ == "__main__":
    main()
