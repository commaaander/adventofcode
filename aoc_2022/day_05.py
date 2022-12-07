""" https://adventofcode.com/2022/day/5 """

from adventofcode import LOG
import re

questions = [
    "After the rearrangement procedure completes, what crate ends up on top of each stack?",  # noqa: E501
    "After the rearrangement procedure completes with CrateMover 9001, what crate ends up on top of each stack?",  # noqa: E501
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")
    answer = ""

    stacks = create_crate_stacks(kwargs["raw_data"].split("\n\n")[0].split("\n"))
    rearrangement_procedure = kwargs["raw_data"].split("\n\n")[1].split("\n")

    LOG.debug(f"{stacks=}, {rearrangement_procedure=}")

    for rearrangement in rearrangement_procedure:
        LOG.debug(f"{rearrangement=}")
        count, from_stack, to_strack = re.search(r"move (.+) from (.+) to (.+)", rearrangement).groups()
        for _ in range(int(count)):
            stacks[to_strack].append(stacks[from_stack].pop())
        LOG.debug(f"{stacks=}")

    for stack in stacks.values():
        answer += stack.pop()

    return questions[0], answer


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")
    answer = ""

    stacks = create_crate_stacks(kwargs["raw_data"].split("\n\n")[0].split("\n"))
    rearrangement_procedure = kwargs["raw_data"].split("\n\n")[1].split("\n")

    LOG.debug(f"{stacks=}, {rearrangement_procedure=}")

    for rearrangement in rearrangement_procedure:
        LOG.debug(f"{rearrangement=}")
        count, from_stack, to_strack = re.search(r"move (.+) from (.+) to (.+)", rearrangement).groups()
        stacks[to_strack] += stacks[from_stack][-int(count) :]  # noqa: E203
        stacks[from_stack] = stacks[from_stack][: -int(count)]
        LOG.debug(f"{stacks=}")

    for stack in stacks.values():
        answer += stack.pop()

    return questions[1], answer


def create_crate_stacks(starting_stack):

    stacks = {}
    for stack in starting_stack[-1][1::4]:
        stacks[stack] = []

    for stack_line in reversed(starting_stack[:-1]):
        for stack, crate in enumerate(stack_line[1::4], start=1):
            if crate != " ":
                stacks[str(stack)].append(crate)

    return stacks
