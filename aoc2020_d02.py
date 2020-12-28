import re
import urllib.request


def main():
    inputFile = open("./data/d02.data")
    inputLines = inputFile.readlines()

    print('Anzahl valider Passwörter: {0}'.format(
        sum(map(checkPasswordValidity1, inputLines)))
    )
    print('Anzahl valider Passwörter: {0}'.format(
        sum(map(checkPasswordValidity2, inputLines)))
    )


def checkPasswordValidity1(line):
    match = re.search('^([0-9]+)-([0-9]+) ([a-z]): ([a-z]*)$', line)

    lowestNumber = int(match.group(1))
    highestNumber = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    if lowestNumber <= password.count(letter) <= highestNumber:
        passwordIsValid = 1
    else:
        passwordIsValid = 0

    return passwordIsValid


def checkPasswordValidity2(line):
    match = re.search('^([0-9]+)-([0-9]+) ([a-z]): ([a-z]*)$', line)

    firstIndex = int(match.group(1))
    secondIndex = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    if len(list(filter(lambda x: x == letter, [password[firstIndex-1], password[secondIndex-1]]))) == 1:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()
