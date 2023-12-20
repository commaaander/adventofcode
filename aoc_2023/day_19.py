""" https://adventofcode.com/2023/day/19 """

import re
from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?",
    "",  # noqa: E501
]


def part_one(**kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({kwargs=})")
    workflows, parts = _parse_raw_data(kwargs["raw_data"])
    answer: int = 0
    for part in parts:
        next_workflow = "in"
        while next_workflow not in "AR":
            rules = workflows[next_workflow]
            next_workflow = ""
            while next_workflow == "":
                for rule in rules:
                    if rule["condition"]:
                        if _check_condition(rule["condition"], part):
                            next_workflow = rule["next_workflow"]
                            break
                    else:
                        next_workflow = rule["next_workflow"]
                        break

        if next_workflow == "A":
            answer += sum(part.values())
            LOG.debug(f"{part=} -> accepted")
        else:
            LOG.debug(f"{part=} -> rejected")
    return questions[0], answer


def part_two(**kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({kwargs=})")
    answer: int = 0
    return questions[1], answer


def _parse_raw_data(raw_data: str) -> Tuple[Dict[str, List[str]], List[Dict[str, str]]]:
    workflows = {}
    parts = []
    for workflow_data in raw_data.split("\n\n")[0].splitlines():
        match = re.search(r"(.*)(\{.*\})", workflow_data)
        rules = []
        for rule in match.group(2).strip("{}").split(","):
            splited_rule = rule.split(":")
            rules.append(
                {
                    "condition": splited_rule[0] if len(splited_rule) > 1 else None,
                    "next_workflow": splited_rule[-1],
                }
            )
        workflows[match.group(1)] = rules

    for parts_data in raw_data.split("\n\n")[1].splitlines():
        part = {}
        for category_data in parts_data.strip("{}").split(","):
            category, value = category_data.split("=")
            part[category] = int(value)
        parts.append(part)

    return workflows, parts


def _check_condition(condition: str, part: Dict[str, int]) -> bool:
    operator_mapping = {
        "<": lambda x, y: x < y,
        ">": lambda x, y: x > y,
        "=": lambda x, y: x == y,
    }
    category, operator, value = re.search(r"(\w+)([<>=]+)(\d+)", condition).groups()
    if operator in operator_mapping:
        return operator_mapping[operator](part[category], int(value))
    else:
        raise ValueError(f"Unknown operator '{operator}'")
