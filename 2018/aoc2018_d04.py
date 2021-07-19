import re
import pathlib


def main():
    data = load_data("d04_sorted.data")
    print(f"number of data sets: {len(data)}")
    # print(data)

    print(f"solution part one: {solution1(data)}")
    print(f"solution part two: {solution2(data)}")


def solution1(data):

    guard_id = None
    falls_asleep = None
    wakes_up = None

    guard_sleep_times = {}

    for event in data:

        match = re.search(
            "^\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}\] Guard #([0-9]+) begins shift$",
            event,
        )
        try:
            guard_id = match.group(1).zfill(5)
            falls_asleep = None
        except AttributeError:
            pass

        if guard_id not in guard_sleep_times:
            guard_sleep_times[guard_id] = {}

        match = re.search(
            "^\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:([0-9]{2})\] falls asleep$", event
        )
        try:
            falls_asleep = int(match.group(1).lstrip("0"))
            wakes_up = None
        except ValueError:
            falls_asleep = 0
            wakes_up = None
        except AttributeError:
            pass

        match = re.search(
            "^\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:([0-9]{2})\] wakes up$", event
        )
        try:
            wakes_up = int(match.group(1).lstrip("0"))
        except ValueError:
            wakes_up = 0
        except AttributeError:
            pass

        if falls_asleep is not None and wakes_up is not None:
            for minute in range(falls_asleep, wakes_up):
                try:
                    guard_sleep_times[guard_id][f"{minute:02d}"] += 1
                except KeyError:
                    guard_sleep_times[guard_id][f"{minute:02d}"] = 1

    most_sleeping_guard_id = max(guard_sleep_times, key=lambda k: sum(guard_sleep_times[k].values()))
    most_sleeping_guard_minute = max(guard_sleep_times[most_sleeping_guard_id], key= lambda x: guard_sleep_times[most_sleeping_guard_id][x])

    return int(most_sleeping_guard_id.lstrip("0"))*int(most_sleeping_guard_minute.lstrip("0"))


def solution2(data):
    return 0


def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return sorted(inputFile.read().split("\n"))


if __name__ == "__main__":
    main()
