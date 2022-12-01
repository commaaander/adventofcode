""" https://adventofcode.com/2021/day15 """

from adventofcode import LOG
from collections import namedtuple
from math import floor

questions = [
    "What is the lowest total risk of any path from the top left to the bottom right?",  # noqa: E501
    "",  # noqa: E501
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")
    map = Map(kwargs["raw_data"].split("\n"), 1)
    graph = Graph(map.get_data())
    path, costs = graph.dijkstra(
        (0, 0),
        (
            len(kwargs["raw_data"].split("\n")[0]) - 1,
            len(kwargs["raw_data"].split("\n")) - 1,
        ),
    )
    LOG.debug(f"{costs=}")
    LOG.debug(f"{path=}")
    LOG.debug(print_cave(kwargs["raw_data"].split("\n"), path))
    return questions[0], costs


def part_two(**kwargs):
    # LOG.debug(f"part_two({kwargs=})")
    factor = 5
    map = Map(kwargs["raw_data"].split("\n"), factor)
    LOG.debug(map)
    graph = Graph(map.get_data())
    path, costs = graph.dijkstra(
        (0, 0),
        (
            map.get_size()[0] - 1,
            map.get_size()[1] - 1,
        ),
    )
    LOG.debug(f"{costs=}")
    LOG.debug(f"{path=}")
    LOG.debug(print_cave(map.get_data(), path))
    return questions[0], costs


def print_cave(cave: list, path: list) -> str:
    map = ""
    for y, row in enumerate(cave):
        for x, value in enumerate(row):
            map += value if (x, y) in path else "."
        map += "\n"
    return map


Edge = namedtuple("Edge", "start, end, cost")


class Graph:
    edges = []

    def __init__(self, raw_data) -> None:

        nodes = {}
        for y, row in enumerate(raw_data):
            for x, value in enumerate(row):
                nodes[(x, y)] = int(value)

        for node in nodes:
            x, y = node
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                if (x + dx, y + dy) in nodes:
                    self.edges.append(
                        Edge((x, y), (x + dx, y + dy), nodes[(x + dx, y + dy)])
                    )

    def vertices(self):
        return set(e.start for e in self.edges).union(e.end for e in self.edges)

    def get_neighbour(self, v):
        neighbours = []
        for e in self.edges:
            if e.start == v:
                neighbours.append((e.end, e.cost))
        return neighbours

    def path(self, source, destination, prev_v):
        path = []
        curr_v = destination
        while prev_v[curr_v] is not None:
            path.insert(0, curr_v)
            curr_v = prev_v[curr_v]
        path.insert(0, curr_v)
        return path

    def dijkstra(self, source, destination):
        distances = {v: float("inf") for v in self.vertices()}
        prev_v = {v: None for v in self.vertices()}

        distances[source] = 0
        vertices = list(self.vertices())[:]
        while len(vertices) > 0:
            LOG.debug(f"Length of vertices: {len(vertices)}")
            v = min(vertices, key=lambda u: distances[u])
            vertices.remove(v)
            if distances[v] == float("inf"):
                break
            for neighbour, cost in self.get_neighbour(v):
                path_cost = distances[v] + cost
                if path_cost < distances[neighbour]:
                    distances[neighbour] = path_cost
                    prev_v[neighbour] = v
        return self.path(source, destination, prev_v), distances[destination]


class Map:
    map_data = []
    factor = 0
    origin_size = (0, 0)

    def __init__(self, map_data: list, factor: int) -> None:
        self.map_data = map_data
        self.factor = factor
        self.origin_size = (len(self.map_data[0]), len(self.map_data[0]))

    def __str__(self) -> str:
        output = ""
        xmax, ymax = self.get_size()
        for y in range(ymax):
            for x in range(xmax):
                output += str(self.get_at(x, y))
            output += "\n"
        return output

    def get_size(self):
        return tuple(self.factor * i for i in self.origin_size)

    def get_at(self, x: int, y: int) -> int:
        xmax, ymax = self.get_size()
        if x < 0 or y < 0 or x >= xmax or y >= ymax:
            raise IndexError(f"Point ({x},{y}) not in map.")

        origin_x = x % self.origin_size[0]
        origin_y = y % self.origin_size[1]
        offset_x = floor(x / self.origin_size[0])
        offset_y = floor(y / self.origin_size[1])

        value = int(self.map_data[origin_y][origin_x]) + offset_x + offset_y
        ret_val = value - 9 * floor((value - 1) / 9)
        return ret_val

    def get_data(self) -> list:
        data = []
        xmax, ymax = self.get_size()
        for y in range(ymax):
            row = ""
            for x in range(xmax):
                row += str(self.get_at(x, y))
            data.append(row)
        return data
