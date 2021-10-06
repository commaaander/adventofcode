from aoc2015_tools import load_data, dprint
import re

debug = False


def main():
    raw_data = load_data(f"d06{'_test' if debug else ''}.data", split_sep='\n')

    print(
        f"solution part one:\n\t"
        f"How many lights are lit? "
        f"{solution1(raw_data)}\n",
        end="")
    print(
        f"solution part two:\n\t"
        f"What is the total brightness of all lights combined after following Santa's instructions? "
        f"{solution2(raw_data)}\n",
        end="")
    print()


def solution1(command_list):
    valid_commands = ["turn on", "toggle", "turn off"]
    regex = re.compile(
        r"(?P<cmd>" + r"|".join(valid_commands) +
        r") (?P<s_x>[0-9]+),(?P<s_y>[0-9]+) through (?P<e_x>[0-9]+),(?P<e_y>[0-9]+)"
    )
    len_x, len_y = 1000, 1000

    # initialize grid with 0
    grid = [[0 for x in range(len_x)] for y in range(len_y)]

    for command_line in command_list:
        command = {}
        try:
            match = regex.match(command_line)
            command = match.groupdict()
        except:
            print(f"'{command_line}' seems not to be a valid command.")
            continue
        dprint(debug, command)

        for x in range(int(command["s_x"]), int(command["e_x"]) + 1):
            for y in range(int(command["s_y"]), int(command["e_y"]) + 1):
                if command["cmd"] == 'turn on':
                    dprint(debug, f"turn on {x:03d}-{y:03d}")
                    grid[x][y] = 1
                elif command["cmd"] == 'turn off':
                    grid[x][y] = 0
                elif command["cmd"] == 'toggle' and grid[x][y] == 1:
                    grid[x][y] = 0
                elif command["cmd"] == 'toggle' and grid[x][y] == 0:
                    grid[x][y] = 1

    result = sum(grid[x][y] for x in range(len_x) for y in range(len_y))
    return result


def solution2(command_list):
    valid_commands = ["turn on", "toggle", "turn off"]
    regex = re.compile(
        r"(?P<cmd>" + r"|".join(valid_commands) +
        r") (?P<s_x>[0-9]+),(?P<s_y>[0-9]+) through (?P<e_x>[0-9]+),(?P<e_y>[0-9]+)"
    )
    len_x, len_y = 1000, 1000

    # initialize grid with 0
    grid = [[0 for x in range(len_x)] for y in range(len_y)]

    for command_line in command_list:
        command = {}
        try:
            match = regex.match(command_line)
            command = match.groupdict()
        except:
            print(f"'{command_line}' seems not to be a valid command.")
            continue
        dprint(debug, command)

        for x in range(int(command["s_x"]), int(command["e_x"]) + 1):
            for y in range(int(command["s_y"]), int(command["e_y"]) + 1):
                if command["cmd"] == 'turn on':
                    dprint(debug, f"turn on {x:03d}-{y:03d}")
                    grid[x][y] += 1
                elif command["cmd"] == 'turn off':
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif command["cmd"] == 'toggle':
                    grid[x][y] += 2

    result = sum(grid[x][y] for x in range(len_x) for y in range(len_y))
    return result


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
'''
--- Day 6: Probably a Fire Hazard ---
--- Part One ---
Because your neighbors keep defeating you in the holiday house decorating 
contest year after year, you've decided to deploy one million lights in a 
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed 
you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights 
at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include 
whether to turn on, turn off, or toggle various inclusive ranges given as 
coordinate pairs. Each coordinate pair represents opposite corners of a 
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers 
to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights 
by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning 
off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?


--- Part Two ---
You just finish implementing your winning light pattern when you realize you 
mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each 
light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of 
those lights by 1.

The phrase turn off actually means that you should decrease the brightness of 
those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of 
those lights by 2.

What is the total brightness of all lights combined after following Santa's 
instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
'''