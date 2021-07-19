import pathlib

input_file = f"{pathlib.Path(__file__).parent.absolute()}/data/{pathlib.Path(__file__).stem}.data"


def main():

    with open(input_file) as input_data:
        wires = input_data.read().split("\n")

    d_x = dict(zip("LRUD", [-1, 1, 0, 0]))
    d_y = dict(zip("LRUD", [0, 0, 1, -1]))

    wire_paths = []
    for wire in wires:
        wire_path = set()

        pos_x = 0
        pos_y = 0
        # wire_path.add((pos_x, pos_y))
        for wire_segment in wire.split(","):
            direction = wire_segment[0]
            steps = int(wire_segment[1:])
            # print(f"Dir: {direction} Steps: {steps}")
            for _ in range(steps):
                pos_x += d_x[direction]
                pos_y += d_y[direction]
                # print (f"[{pos_x: 4}:{pos_y: 4}]")

                wire_path.add((pos_x, pos_y))
        wire_paths.append(wire_path)

    intersections = wire_paths[0].intersection(wire_paths[1])
    min_m_distance = min(abs(x[0]) + abs(x[1]) for x in intersections)

    print(
        f"Part1:\nQuestion: What is the Manhattan distance from the central port to the closest intersection?\nAnswer: {min_m_distance}"
    )

    i = 0
    for intersection in intersections:
        i += 1
        print(f"Intersection [{i}/{len(intersections)}]: {intersection}", end="\r")
        for wire_path in wire_paths:
            pass

    print("")


if __name__ == "__main__":
    main()
