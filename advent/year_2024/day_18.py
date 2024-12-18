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

from advent.utils.path_finding_2 import Node, djikstra, has_final_coords_function, ClosedList
from dataclasses import dataclass
        
class ByteNode(Node):
    coord: tuple[int, int]

    def __init__(self, coord):
        self.coord = coord

    def check_valid_neighbour(self, map, direction, neighbour_coord):
        return map.check_node(neighbour_coord)

@dataclass
class Map:
    width: int
    walls: set[tuple[int, int]]

    def check_node(self, coord):
        return (coord[0] >=0 and coord[0] <= self.width and coord[1] >= 0 and coord[1] <= self.width) and coord not in self.walls

@register(18, 2024, 1)
def func_1(text, number_to_place=1024, width = 70):
    map = Map(width, set())
    for line in text.split("\n")[:number_to_place]:
        split_line = line.split(",")
        map.walls.add((int(split_line[0]), int(split_line[1])))

    final = (width, width)

    terminate_function = has_final_coords_function(final)

    start = ByteNode((0,0))

    result = djikstra(map, start, terminate_function, False)

    return result.get_cost()

@register(18, 2024, 2)
def func_2(text, width = 70):
    coords = []
    map = Map(width, set())
    for line in text.split("\n"):
        split_line = line.split(",")
        coord = (int(split_line[0]), int(split_line[1]))
        map.walls.add(coord)
        coords.append(coord)

    final = (width, width)

    terminate_function = has_final_coords_function(final)

    start = ByteNode((0,0))

    for coord_to_remove in reversed(coords):
        map.walls.remove(coord_to_remove)

        result = djikstra(map, start, terminate_function, False)

        if not isinstance(result, ClosedList):
            return coord_to_remove