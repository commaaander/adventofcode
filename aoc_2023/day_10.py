"""
https://adventofcode.com/2023/day/10


"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from rich import print

from adventofcode import LOG

questions: List[str] = [
    "How many steps along the loop does it take to get from the starting position to the point farthest from the starting"
    " position?",
    "How many tiles are enclosed by the loop?",
]


def part_one(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_one({kwargs=})")
    maze = PipeMaze(kwargs["raw_data"])
    LOG.debug(f"part_one():: starting point={maze.get_starting_point()}")
    maze.calc_path_length()
    print(maze)
    answer: int = max(point.distance for point in maze.pipes.values())
    return questions[0], answer


def part_two(**kwargs: Dict[str, Any]) -> Tuple[str, str]:
    LOG.debug(f"part_two({kwargs=})")
    answer: int = 0
    return questions[1], answer


def parse_raw_data(raw_data: str) -> Any:
    parsed_data = {}

    return parsed_data


@dataclass
class Point:
    x: int
    y: int
    pipe_type: str
    distance: int = -1


class PipeMaze:
    def __init__(self, map_data: str) -> None:
        self.pipes: Dict[Tuple[int, int], Point] = {}
        self.starting_point: Point = Point(-1, -1, "S")
        self.width = None
        self.height = 0

        for y, x_line in enumerate(map_data.splitlines()):
            line_length = len(x_line)
            if self.width is None:
                self.width = line_length
            elif self.width != line_length:
                raise ValueError(f"Suspicious x_line length ({line_length} != {self.width}) in row {y}.")

            for x, pipe_type in enumerate(x_line):
                if pipe_type != ".":
                    self.pipes[(x, y)] = Point(x, y, pipe_type)
                    if pipe_type == "S":
                        self.starting_point = Point(x, y, pipe_type)

            self.height = y + 1

    def __rich__(self) -> str:
        pipe_type_map = {"F": "┌", "7": "┐", "J": "┘", "L": "└", "|": "│", "-": "─", "S": "[red]S[/red]"}

        rows = []
        for y in range(self.height):
            row = [f"{y:003d} "]
            for x in range(self.width):
                point = self.get_point_at(x, y)
                if not point:
                    row.append("[blue]█[/blue]")
                else:
                    if point.distance > 0:
                        row.append("[green]")
                    row.append(pipe_type_map.get(point.pipe_type, "X"))
                    if point.distance > 0:
                        row.append("[/green]")
            rows.append("".join(row))

        return "\n".join(rows)

    def get_point_at(self, x: int, y: int) -> Optional[Point]:
        try:
            p = self.pipes[(x, y)]
        except KeyError:
            return None
        return p

    def get_starting_point(self):
        return self.starting_point

    def get_neighbor_point(self, p, direction: str) -> Optional[Point]:
        direction_deltas = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}

        try:
            dx, dy = direction_deltas[direction]
        except KeyError:
            LOG.debug(f"PipeMaze::get_neighbor_point({p}, {direction}) Direction not valid.")
            return None

        try:
            n = self.pipes[(p.x + dx, p.y + dy)]
        except KeyError:
            LOG.debug(f"PipeMaze::get_neighbor_point({p}, {direction}) Point not found in map.")
            return None

        return n

    def get_connected_points(self, point: Point) -> List[Optional[Point]]:
        valid_directions = {
            "F": ["E", "S"],
            "-": ["E", "W"],
            "7": ["S", "W"],
            "|": ["N", "S"],
            "J": ["N", "W"],
            "L": ["N", "E"],
            "S": ["S", "E", "N", "W"],
        }
        valid_connectors = {
            "N": ["S", "|", "F", "7"],
            "E": ["S", "-", "J", "7"],
            "S": ["S", "|", "J", "L"],
            "W": ["S", "-", "F", "L"],
        }

        connected_points: List[Optional[Point]] = []
        for direction in valid_directions[point.pipe_type]:
            neighbor_point = self.get_neighbor_point(point, direction)
            if neighbor_point and neighbor_point.pipe_type in valid_connectors[direction]:
                connected_points.append(neighbor_point)
        LOG.debug(f"Found {connected_points=}")
        return connected_points

    def calc_path_length(self) -> None:
        self.get_next_connected_point(None, self.starting_point, 0)

    def get_next_connected_point(self, last_point: Optional[Point], point: Point, depth: int) -> None:
        stack = [(last_point, point, depth)]

        while stack:
            last_point, point, depth = stack.pop()
            point.distance = min(point.distance if point.distance >= 0 else depth + 1, depth)
            depth += 1

            for connected_point in self.get_connected_points(point):
                if last_point and connected_point == last_point:
                    LOG.debug(f"Skipping {connected_point}, already visited")
                elif connected_point.pipe_type == "S":
                    LOG.debug(f"Starting point {connected_point} arrived")
                else:
                    LOG.debug(f"Updating {connected_point}")
                    stack.append((point, connected_point, depth))
