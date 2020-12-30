def main():
    with open("data/d06.data") as inputFile:
        data = inputFile.read().split("\n\n")
        questionGroups = [line.replace("\n", "") for line in data]
    
        print(f"{len(questionGroups)} question groups")
        
        uniqueQuestionsSum = 0
        for questionGroup in questionGroups:
            uniqueQuestions = {}
            for question in questionGroup:
                uniqueQuestions[question]=None
            uniqueQuestionsSum += len(sorted(uniqueQuestions.keys()))
        
        print(f"Solution part 1: Sum of unique questions: {uniqueQuestionsSum}")
        
        
if __name__ == '__main__':
    main()

