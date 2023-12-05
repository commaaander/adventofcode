""" https://adventofcode.com/2021/day/14 """

import re
from adventofcode import LOG

questions = [
    "What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?",  # noqa: E501
    "",  # noqa: E501
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")
    template, rules = convert_raw_data(kwargs["raw_data"])
    LOG.debug(f"{template=}\n{rules=}")

    for count in range(10):
        new_template = ""
        for index in range(
            len(template) - 1,
        ):
            element_pair = (template[index], template[index + 1])
            inner_element = rules[element_pair] if element_pair in rules else ""
            new_template += template[index] + inner_element
        new_template += template[index + 1]
        LOG.debug(f"Round: {count + 1}, {len(new_template)} elements")
        template = new_template

    chars = {c: template.count(c) for c in set(template)}
    LOG.debug(f"{chars=}")
    return questions[0], max(chars[k] for k in chars.keys()) - min(chars[k] for k in chars.keys())


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")
    template, rules = convert_raw_data(kwargs["raw_data"])
    LOG.debug(f"{template=}\n{rules=}")

    for count in range(0):
        new_template = ""
        for index in range(
            len(template) - 1,
        ):
            element_pair = (template[index], template[index + 1])
            inner_element = rules[element_pair] if element_pair in rules else ""
            new_template += template[index] + inner_element
        new_template += template[index + 1]
        LOG.debug(f"Round: {count + 1}, {len(new_template)} elements")
        template = new_template

    chars = {c: template.count(c) for c in set(template)}
    LOG.debug(f"{chars=}")
    return questions[0], max(chars[k] for k in chars.keys()) - min(chars[k] for k in chars.keys())


def convert_raw_data(raw_data):
    rules = {}
    for rule in raw_data.split("\n")[2:]:
        match = re.match(r"([A-Z])([A-Z]) -> ([A-Z])", rule)
        rules[(match.group(1), match.group(2))] = match.group(3)

    return raw_data.split("\n")[0], rules
