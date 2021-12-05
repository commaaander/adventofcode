from aoc2015_tools import load_data, dprint
import re

debug = False


def main():
    raw_data = load_data(f"d06{'_test' if debug else ''}.data", split_sep="\n")

    print(
        f"solution part one:\n\t"
        f"How many lights are lit? "
        f"{solution1(raw_data)}\n",
        end="",
    )
    print(
        f"solution part two:\n\t"
        f"What is the total brightness of all lights combined after following "
        f"Santa's instructions? "
        f"{solution2(raw_data)}\n",
        end="",
    )
    print()


def solution1(command_list):
    valid_commands = ["turn on", "toggle", "turn off"]
    regex = re.compile(
        r"(?P<cmd>"
        + r"|".join(valid_commands)
        + r") (?P<s_x>[0-9]+),(?P<s_y>[0-9]+) through (?P<e_x>[0-9]+),(?P<e_y>[0-9]+)"
    )
    len_x, len_y = 1000, 1000

    # initialize grid with 0
    grid = [[0 for x in range(len_x)] for y in range(len_y)]

    for command_line in command_list:
        command = {}
        try:
            match = regex.match(command_line)
            command = match.groupdict()
        except Exception:
            print(f"'{command_line}' seems not to be a valid command.")
            continue
        dprint(debug, command)

        for x in range(int(command["s_x"]), int(command["e_x"]) + 1):
            for y in range(int(command["s_y"]), int(command["e_y"]) + 1):
                if command["cmd"] == "turn on":
                    dprint(debug, f"turn on {x:03d}-{y:03d}")
                    grid[x][y] = 1
                elif command["cmd"] == "turn off":
                    grid[x][y] = 0
                elif command["cmd"] == "toggle" and grid[x][y] == 1:
                    grid[x][y] = 0
                elif command["cmd"] == "toggle" and grid[x][y] == 0:
                    grid[x][y] = 1

    result = sum(grid[x][y] for x in range(len_x) for y in range(len_y))
    return result


def solution2(command_list):
    valid_commands = ["turn on", "toggle", "turn off"]
    regex = re.compile(
        r"(?P<cmd>"
        + r"|".join(valid_commands)
        + r") (?P<s_x>[0-9]+),(?P<s_y>[0-9]+) through (?P<e_x>[0-9]+),(?P<e_y>[0-9]+)"
    )
    len_x, len_y = 1000, 1000

    # initialize grid with 0
    grid = [[0 for x in range(len_x)] for y in range(len_y)]

    for command_line in command_list:
        command = {}
        try:
            match = regex.match(command_line)
            command = match.groupdict()
        except Exception:
            print(f"'{command_line}' seems not to be a valid command.")
            continue
        dprint(debug, command)

        for x in range(int(command["s_x"]), int(command["e_x"]) + 1):
            for y in range(int(command["s_y"]), int(command["e_y"]) + 1):
                if command["cmd"] == "turn on":
                    dprint(debug, f"turn on {x:03d}-{y:03d}")
                    grid[x][y] += 1
                elif command["cmd"] == "turn off":
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif command["cmd"] == "toggle":
                    grid[x][y] += 2

    result = sum(grid[x][y] for x in range(len_x) for y in range(len_y))
    return result


def test_rule(regex, word: str):

    ret_val = False
    match = re.search(regex, word)
    if match:
        ret_val = True
        if debug:
            print(
                f"{regex} {word} result: {match.group()}",
            )
    else:
        if debug:
            print(
                f"{regex} {word} did not pass",
            )
    return ret_val


if __name__ == "__main__":
    main()
