from advent.runner import register
from advent.utils.split_text import split_text, Split
from dataclasses import dataclass
import math
from functools import cache
from collections import defaultdict

from advent.utils.direction import Direction

from time import perf_counter

class Region:
    id: int
    area: int
    perimeter: int
    sides: int
    letter: str
    coords: set

    def __init__(self, id, letter, coords):
        self.id = id
        self.letter = letter
        self.area = 1
        self.perimeter = 4
        self.sides = 4
        self.coords = {coords}

    def create_sides(self):
        sides = []

@register(12, 2024, 1)
def func_1(text):
    regions = {}
    region_lookup = {}
    id = 0
    for y, line in enumerate(text.split("\n")):
        for x, char, in enumerate(line):
            region = None
            region_count = 0
            for direction in [Direction.UP, Direction.LEFT]:
                coords = direction.move_forward_x_and_y(x, y)
                if coords in region_lookup:
                    this_region = region_lookup[coords]
                    if this_region.letter == char:
                        if region is None or this_region.id == region.id:
                            region = this_region
                            region_count += 1
                        else:
                            region.area += this_region.area
                            region.perimeter += this_region.perimeter
                            region.coords.update(this_region.coords)

                            region_count += 1

                            for replace_coords in this_region.coords:
                                region_lookup[replace_coords] = region

                            del regions[this_region.id]                 

            self_coords = (x, y)
            if region is not None:
                region_lookup[self_coords] = region
                region.area += 1
                region.perimeter += 4 - (2 * region_count)
                region.coords.add(self_coords)
            else:
                region = Region(id, char, self_coords)
                id += 1
                regions[region.id] = region
                region_lookup[self_coords] = region

    cost = 0
    for region in regions.values():
        cost += region.area * region.perimeter

    return cost

@register(12, 2024, 2)
def func_2(text):
    regions = {}
    region_lookup = {}
    id = 0
    for y, line in enumerate(text.split("\n")):
        for x, char, in enumerate(line):
            region = None
            direction_set = set()
            for direction in [Direction.UP, Direction.LEFT]:
                coords = direction.move_forward_x_and_y(x, y)
                if coords in region_lookup:
                    this_region = region_lookup[coords]
                    if this_region.letter == char:
                        direction_set.add(direction)
                        if region is None or this_region.id == region.id:
                            region = this_region
                        else:
                            region.area += this_region.area
                            region.perimeter += this_region.perimeter
                            region.sides += this_region.sides
                            region.coords.update(this_region.coords)

                            for replace_coords in this_region.coords:
                                region_lookup[replace_coords] = region

                            del regions[this_region.id]


            self_coords = (x, y)
            if region is not None:
                region_lookup[self_coords] = region
                region.area += 1
                region.perimeter += 4 - (2 * len(direction_set))
                region.coords.add(self_coords)

                top_left = (x - 1, y - 1)
                top_right = (x + 1, y - 1)

                if len(direction_set) == 2:
                    if top_right not in region.coords:
                        region.sides -= 2
                else:
                    if direction.UP in direction_set:
                        if top_left in region.coords:
                            region.sides += 2
                        if top_right in region.coords:
                            region.sides += 2
                    else:
                        if top_left in region.coords:
                            region.sides += 2
            else:
                region = Region(id, char, self_coords)
                id += 1
                regions[region.id] = region
                region_lookup[self_coords] = region

    cost = 0
    for region in regions.values():
        cost += region.area * region.sides

    return cost