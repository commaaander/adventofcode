from aoc2015_tools import load_data
import re

debug = False


def main():
    raw_data = load_data(f"d05{'_test' if debug else ''}.data", split_sep='\n')

    print(
        f"solution part one:\n\t"
        f"How many strings are nice? "
        f"{solution1(raw_data)}\n",
        end="")
    print(
        f"solution part two:\n\t"
        f"How many strings are nice under these new rules? "
        f"{solution2(raw_data)}\n",
        end="")


def solution1(word_list):
    nice_word_count = 0
    rule1 = re.compile(r"[aeiou].*[aeiou].*[aeiou]")
    rule2 = re.compile(r"(.)\1")
    rule3 = re.compile(r"ab|cd|pq|xy")

    for word in word_list:
        if test_rule(rule1, word) and test_rule(
                rule2, word) and not test_rule(rule3, word):
            if debug:
                print(f"{word} is nice")
            nice_word_count += 1
    return nice_word_count


def solution2(word_list):
    nice_word_count = 0
    rule1 = re.compile(r"(..).*\1")
    rule2 = re.compile(r"(.).\1")

    for word in word_list:
        if test_rule(rule1, word) and test_rule(rule2, word):
            if debug:
                print(f"{word} is nice")
            nice_word_count += 1
    return nice_word_count


def test_rule(regex, word: str):

    ret_val = False
    match = re.search(regex, word)
    if match:
        ret_val = True
        if debug:
            print(f"{regex} {word} result: {match.group()}", )
    else:
        if debug:
            print(f"{regex} {word} did not pass", )
    return ret_val


if __name__ == "__main__":
    main()
