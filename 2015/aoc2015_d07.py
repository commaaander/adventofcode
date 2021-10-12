from aoc2015_tools import load_data, dprint
import re
from os.path import basename

debug = False


def main():

    day = re.search(r"aoc.*_(?P<day>d[0-9]{2})",
                    basename(__file__)).group('day')

    raw_data = load_data(f"{day}{'_test' if debug else ''}.data",
                         split_sep='\n')

    print(
        f"solution part one:\n\t"
        f"In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a? "
        f"{solution1(raw_data)}\n",
        end="")
    # print(
    #     f"solution part two:\n\t"
    #     f"xxx? "
    #     f"{solution2(raw_data)}\n",
    #     end="")
    print()


def solution1(command_list):

    result = ""
    rs = {}

    for command in command_list:
        # 123 -> x
        m = re.match(r"(?P<v>\w+) -> (?P<t>\w+)", command)
        if m:
            dprint(debug=False, message=m.groupdict())

            if not m.group("v").isnumeric():
                try:
                    v = rs[m.group("v")]
                except:
                    v = 0
            else:
                v = int(m.group("v"))

            try:
                rs[m.group("t")] = v
                dprint(debug=True,
                       message=f"__command >{command}< successfull")
            except KeyError as e:
                print(e)
                print(f"Error in command >{command}<")
            continue

        # x AND|OR|LSHIFT|RSHIFT y -> z
        m = re.match(r"(?P<v1>\w+) (?P<o>\w+) (?P<v2>\w+) -> (?P<t>\w+)",
                     command)
        if m:
            dprint(debug=False, message=m.groupdict())

            if not m.group("v1").isnumeric():
                try:
                    v1 = rs[m.group("v1")]
                except:
                    v1 = 0
            else:
                v1 = int(m.group("v1"))

            if not m.group("v2").isnumeric():
                try:
                    v2 = rs[m.group("v2")]
                except:
                    v2 = 0
            else:
                v2 = int(m.group("v2"))

            try:
                if m.group("o") == "AND":
                    rs[m.group("t")] = v1 & v2

                elif m.group("o") == "OR":
                    rs[m.group("t")] = v1 | v2

                elif m.group("o") == "RSHIFT":
                    rs[m.group("t")] = v1 >> v2

                elif m.group("o") == "LSHIFT":
                    rs[m.group("t")] = v1 << v2

                dprint(debug=True, message=f"command >{command}< successfull")
            except KeyError as e:
                print(e)
                print(f"Error in command >{command}<")
            continue

        # NOT e -> f
        m = re.match(r"(?P<o>\w+) (?P<v>\w+) -> (?P<t>\w+)", command)
        if m:
            dprint(debug=False, message=m.groupdict())

            if not m.group("v").isnumeric():
                try:
                    v = rs[m.group("v")]
                except:
                    v = 0
            else:
                v = int(m.group("v"))

            try:
                rs[m.group("t")] = ~v
                dprint(debug=True, message=f"command >{command}< successfull")
            except KeyError as e:
                print(e)
                print(f"Error in command >{command}<")
            continue
        print(command)

    dprint(debug=True, message=sorted(rs))
    return rs["a"]


def solution2(command_list):
    result = ""
    return result


if __name__ == "__main__":
    main()
'''
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific v. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the v from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the v from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.


'''