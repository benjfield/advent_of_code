from advent.runner import register
import math
from itertools import combinations
from dataclasses import dataclass
from functools import lru_cache
from advent.utils.direction import Direction

map = None

@lru_cache
def reachable_ends(x, y):
    value = map[y][x]
    if value == 9:
        return {(x, y)}
    
    end_points = set()
    for direction in Direction:
        neighbour_x, neighbour_y = direction.move_forward(x, y)

        if neighbour_x >= 0 and neighbour_x < len(map[0]) and neighbour_y >= 0 and neighbour_y < len(map):
            if map[neighbour_y][neighbour_x] == value + 1:
                end_points.update(
                    reachable_ends(neighbour_x, neighbour_y)
                )

    return end_points

@register(10, 2024, 1, True)
def func_1(text):
    global map
    map = []
    for line in text:
        map.append([int(x) for x in line])

    total = 0
    for y, line in enumerate(map):
        for x, value in enumerate(line):
            if value == 0:
                total += len(reachable_ends(x, y))

    return total

@lru_cache
def reachable_ends_rating(x, y):
    value = map[y][x]
    if value == 9:
        return 1
    
    rating = 0
    for direction in Direction:
        neighbour_x, neighbour_y = direction.move_forward(x, y)

        if neighbour_x >= 0 and neighbour_x < len(map[0]) and neighbour_y >= 0 and neighbour_y < len(map):
            if map[neighbour_y][neighbour_x] == value + 1:
                rating += reachable_ends_rating(neighbour_x, neighbour_y)

    return rating

@register(10, 2024, 2, True)
def func_2(text):
    global map
    map = []
    for line in text:
        map.append([int(x) for x in line])

    total = 0
    for y, line in enumerate(map):
        for x, value in enumerate(line):
            if value == 0:
                total += reachable_ends_rating(x, y)

    return total