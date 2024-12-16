from advent.runner import register
from advent.utils.split_text import split_text, Split
from advent.utils.grid import Grid
from dataclasses import dataclass
import math
from functools import cache
from collections import defaultdict

from advent.utils.direction import Direction

from time import perf_counter

import re

from functools import partial

from advent.utils.path_finding_2 import Node, djikstra, has_final_coords_function

class ReindeerNode(Node):
    coord: tuple[int, int]
    entry_direction: Direction

    def __init__(self, coord, entry_direction):
        self.coord = coord
        self.entry_direction = entry_direction

    def check_valid_neighbour(self, map, direction, neighbour_coord):
        return direction != self.entry_direction.flip() and neighbour_coord in map

    def get_additional_cost(self, map, direction, neighbour_coord):
        if direction == self.entry_direction:
            return 1
        else:
            return 1001
            
    def get_neighbour(self, map, direction, neighbour_coord):
        return type(self)(
            neighbour_coord,
            direction
        )
    
    def __hash__(self):
        return hash((self.coord, self.entry_direction))
    
    def __eq__(self, other):
        return self.coord == other.coord and self.entry_direction == other.entry_direction

    def __str__(self):
        return f"x {self.coord[0]} y {self.coord[1]} direction {self.entry_direction}"

@register(16, 2024, 1)
def func_1(text):
    paths = set()

    for y, line in enumerate(split_text(text, Split.LINE)):
        for x, char in enumerate(line):
            if char == ".":
                paths.add((x, y))
            elif char == "S":
                start = (x, y)
                paths.add((x, y))
            elif char == "E":
                final = (x, y)
                paths.add((x, y))

    terminate_function = has_final_coords_function(final)

    start = ReindeerNode(start, Direction.RIGHT)

    return djikstra(paths, start, terminate_function).get_cost()

@register(16, 2024, 2)
def func_2(text):
    paths = set()

    for y, line in enumerate(split_text(text, Split.LINE)):
        for x, char in enumerate(line):
            if char == ".":
                paths.add((x, y))
            elif char == "S":
                start = (x, y)
                paths.add((x, y))
            elif char == "E":
                final = (x, y)
                paths.add((x, y))

    start = ReindeerNode(start, Direction.RIGHT)

    store = djikstra(paths, start)
    lowest_cost = 100000000000

    for node, node_cost in store.store.items():
        if node.coord == final and node_cost.get_cost() < lowest_cost:
            lowest_cost = node_cost.get_cost()
            path = node_cost.path

    return len(path)