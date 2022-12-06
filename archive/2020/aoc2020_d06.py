questionGroups = []


def main():
    global questionGroups
    with open("data/d06.data") as inputFile:
        data = inputFile.read().split("\n\n")
        questionGroups = [line.replace("\n", "#") for line in data]

    print(f"{len(questionGroups)} question groups")
    print(f"Solution part 1: Sum of answered questions: {solutionPart1()}")
    print(f"Solution part 2: Sum of everyone answered questions: {solutionPart2()}")


def solutionPart1():
    global questionGroups
    questionsSum = 0

    for questionGroup in questionGroups:
        questions = {}
        for question in questionGroup:
            if question != "#":
                questions[question] = None
        questionsSum += len(sorted(questions))

    return questionsSum


def solutionPart2():
    global questionGroups
    questionsSum = 0

    for questionGroup in questionGroups:
        questions = {}
        for question in questionGroup:
            if question not in questions:
                questions[question] = 1
            else:
                questions[question] += 1
        passengerPerGroupCount = questions["#"] + 1 if "#" in questions else 1
        for question in questions.keys():
            if question != "#" and questions[question] == passengerPerGroupCount:
                questionsSum += 1

    return questionsSum


if __name__ == "__main__":
    main()
