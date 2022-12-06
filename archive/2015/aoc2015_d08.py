from aoc2015_tools import load_data
import re
from os.path import basename

debug = False


def main():

    day = re.search(r"aoc.*_(?P<day>d[0-9]{2})", basename(__file__)).group("day")

    raw_data = load_data(f"{day}{'_test' if debug else ''}.data", split_sep="\n")

    question1 = ""
    print(
        f"""Solution part one:
            {question1}: {solution1(raw_data)}
        """
    )
    # print(
    #     f"solution part two:\n\t"
    #     f"xxx? "
    #     f"{solution2(raw_data)}\n",
    #     end="")
    print()


def solution1(**kwargs) -> None:
    return None


def solution2(**kwargs) -> None:
    return None


if __name__ == "__main__":
    main()
