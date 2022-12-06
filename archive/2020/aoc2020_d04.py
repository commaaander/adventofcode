import re


def main():
    inputFile = open("data/d04.data")

    passports = []
    joinedLines = []

    for line in inputFile:
        if line != "\n":
            joinedLines.append(line.strip("\n"))
        else:
            passports.append(" ".join(joinedLines))
            joinedLines.clear()

    if len(joinedLines) > 0:
        passports.append(" ".join(joinedLines))

    inputFile.close()

    passportValidation(passports)


def passportValidation(passports):

    requiredFields = {
        "byr": checkBirthYear,
        "iyr": checkIssueYear,
        "eyr": checkExpirationYear,
        "hgt": checkHeight,
        "hcl": checkHairColor,
        "ecl": checkEyeColor,
        "pid": checkPassportID,
    }

    validPassportCount = 0
    invalidPassportCount = 0
    passportCount = 0
    for passport in passports:
        passportCount += 1
        print("\n")
        print(passportCount, passport)
        fieldsPresentCount = 0
        for requiredField, validationFunction in requiredFields.items():
            searchString = f"{requiredField}:([a-zA-Z0-9#]+)"
            match = re.search(searchString, passport)
            if match is not None:
                if validationFunction(match.group(1)):
                    fieldsPresentCount += 1
        if fieldsPresentCount == len(requiredFields):
            validPassportCount += 1
            print("passport valid")
        else:
            invalidPassportCount += 1
            print("passport invalid")

    print("\n\n")
    print(f"Number of Passports: {passportCount}")
    print(f"valid Passports: {validPassportCount}")
    print(f"invalid Passports: {invalidPassportCount}")


def checkBirthYear(checkValue):
    valuePassed = False
    match = re.search("([0-9]{4})", checkValue)
    if match is not None:
        if 1920 <= int(match.group(1)) <= 2002:
            valuePassed = True
    print("checkBirthYear", checkValue, valuePassed)
    return valuePassed


def checkIssueYear(checkValue):
    valuePassed = False
    match = re.search("([0-9]{4})", checkValue)
    if match is not None:
        if 2010 <= int(match.group(1)) <= 2020:
            valuePassed = True
    print("checkIssueYear", checkValue, valuePassed)
    return valuePassed


def checkExpirationYear(checkValue):
    valuePassed = False
    match = re.search("([0-9]{4})", checkValue)
    if match is not None:
        if 2020 <= int(match.group(1)) <= 2030:
            valuePassed = True
    print("checkExpirationYear", checkValue, valuePassed)
    return valuePassed


def checkHeight(checkValue):
    valuePassed = False
    allowedValues = {"in": [59, 76], "cm": [150, 193]}
    match = re.search("([0-9]+)(in|cm)", checkValue)
    if match is not None:
        if (
            allowedValues[match.group(2)][0]
            <= int(match.group(1))
            <= allowedValues[match.group(2)][1]
        ):
            valuePassed = True
    print("checkHeight", checkValue, valuePassed)
    return valuePassed


def checkHairColor(checkValue):
    valuePassed = False
    match = re.search("(#[0-9a-f]{6})", checkValue)
    if match is not None:
        valuePassed = True
    print("checkHairColor", checkValue, valuePassed)
    return valuePassed


def checkEyeColor(checkValue):
    valuePassed = False
    allowedValues = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if checkValue in allowedValues:
        valuePassed = True
    print("checkEyeColor", checkValue, valuePassed)
    return valuePassed


def checkPassportID(checkValue):
    valuePassed = False
    match = re.search("^([0-9]{9})$", checkValue)
    if match is not None:
        valuePassed = True
    print("checkPassportID", checkValue, valuePassed)
    return valuePassed


if __name__ == "__main__":
    main()
