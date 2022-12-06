def main():
    input = "206938-237000"
    input = "206938-679128"
    min = int(input.split("-")[0])
    max = int(input.split("-")[1])

    rules = ("rule2", "rule3")
    codes_ok_count = 0

    for code in range(min, max + 1):
        rule_passed = True
        for rule_name in rules:
            if not rule_passed:
                continue
            rule_function = globals()[rule_name]
            if not rule_function(code):
                rule_passed = False
                continue

        if rule_passed:
            print(f"{code} passed.")
            codes_ok_count += 1

    print(f"last code: {code}")


def rule2(code: int):
    # Two adjacent digits are the same (like 22 in 122345)

    ret_val = False
    length = len(str(code))
    unique_length = len("".join(set(str(code))))
    if length > unique_length:
        ret_val = True

    return ret_val


def rule3(code: int):
    # Going from left to right, the digits never decrease; they only ever increase
    # or stay the same (like 111123 or 135679)
    code_string = str(code)
    for i in range(1, len(code_string)):
        if code_string[i] < code_string[i - 1]:
            return False

    return True


if __name__ == "__main__":
    main()
