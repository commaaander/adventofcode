""" https://adventofcode.com/2022/day/5 """

from typing import Any, Dict, List, Set, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What is the lowest location number that corresponds to any of the initial seed numbers?",
    "",
]


def part_one(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_one({kwargs=})")
    locations: Set[int] = {}
    almanac = parse_raw_data(kwargs["raw_data"])
    for seed in almanac["seeds"]:
        locations.add(process_mapping(seed, almanac))
        pass
    return questions[0], min(locations)


def part_two(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_two({kwargs=})")
    locations: List[int] = []
    almanac = parse_raw_data(kwargs["raw_data"])
    LOG.debug(f"part_two()::seeds={almanac['seeds'][0::2]}, counts={almanac['seeds'][1::2]}")
    for seed, count in zip(almanac["seeds"][0::2], almanac["seeds"][1::2]):
        LOG.debug(f"part_two()::{seed=}, {count=}")
        for i in range(count):
            locations.append(process_mapping(seed + i, almanac))
        LOG.debug(f"part_two()::location count={len(locations)}")
    return questions[1], min(locations)


def parse_raw_data(raw_data: str) -> Any:
    parsed_data = {}
    segments = raw_data.split("\n\n")
    parsed_data["seeds"] = [int(seed) for seed in segments[0].split() if seed.isdigit()]
    for segment in segments[1:]:
        map_name = segment.split(":")[0]
        parsed_data[map_name] = []
        for line in segment.split(":")[1].strip().splitlines():
            dest, source, length = line.split()
            parsed_data[map_name].append({"source": int(source), "dest": int(dest), "length": int(length)})
    LOG.debug(f"parse_raw_data()::{parsed_data}")
    return parsed_data


def map_number(number: int, map: List[Dict[str, int]]) -> int:
    for mapping in map:
        if mapping["source"] <= number <= mapping["source"] + mapping["length"]:
            number = number + (mapping["dest"] - mapping["source"])
            return number
    return number


def process_mapping(number: int, almanac) -> int:
    return map_number(
        map_number(
            map_number(
                map_number(
                    map_number(
                        map_number(
                            map_number(
                                number,
                                almanac["seed-to-soil map"],
                            ),
                            almanac["soil-to-fertilizer map"],
                        ),
                        almanac["fertilizer-to-water map"],
                    ),
                    almanac["water-to-light map"],
                ),
                almanac["light-to-temperature map"],
            ),
            almanac["temperature-to-humidity map"],
        ),
        almanac["humidity-to-location map"],
    )
