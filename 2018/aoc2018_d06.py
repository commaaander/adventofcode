import pathlib
import math

debug = False


def main():
    raw_data = load_data(f"d06{'_test' if debug else ''}.data")
    print(f"data length: {len(raw_data)}")

    list_data = list(
        {"x": int(point[0]), "y": int(point[1]),
         "name": get_pointname_from_index(i)}
        for i, point in enumerate(data.split(", ") for data in raw_data)
    )

    print(
        f"solution part one:\n\t"
        f"What is the size of the largest area that isn't infinite? "
        f"{solution1(list_data)}")
    pass


def solution1(data):

    # print(data)
    # find boundaries
    borders = {
        "bottom": min(point["x"] for point in data),
        "top": max(point["x"] for point in data),
        "left": min(point["y"] for point in data),
        "right": max(point["y"] for point in data)
    }

    print(f"borders: {borders}")
    print("Calculate Map")
    map = []
    i = 1
    j = 0
    for x in range(borders["bottom"], borders["top"]+1):
        for y in range(borders["left"], borders["right"]+1):
            map_entry = {"x": x, "y": y, "md": {}}
            for point in data:
                try:
                    map_entry["md"][f"{get_manhattan_distance({'x': x, 'y': y}, point):04d}"].append(point['name'])
                except:
                    map_entry["md"][f"{get_manhattan_distance({'x': x, 'y': y}, point):04d}"] = []
                    map_entry["md"][f"{get_manhattan_distance({'x': x, 'y': y}, point):04d}"].append(point['name'])
                j += 1
            map.append(map_entry)
            i += 1
    print(f"After {j} rounds: {map}")
    # determine the largest area
    pass
    print(data)


def get_manhattan_distance(point1, point2):
    return abs(point1["x"] - point2["x"]) + abs(point1["y"] - point2["y"])


def get_pointname_from_index(index):
    first_letter = math.floor(index/26)
    second_letter = index % 26
    ret_val = \
        f"{chr(first_letter + ord('A') - 1) if first_letter > 0 else ''}" + \
        f"{chr(second_letter + ord('A'))}"
    return ret_val


def load_data(filename):

    with open(
        f"{pathlib.Path(__file__).parent.absolute()}/data/{filename}"
    ) as inputFile:
        return inputFile.read().split("\n")


if __name__ == "__main__":
    main()
