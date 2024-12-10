from advent.runner import register
from advent.utils.split_text import split_text, Split
from functools import lru_cache
from advent.utils.direction import Direction
from advent.utils.grid import check_inbounds

map = None

@lru_cache
def reachable_ends(x, y):
    value = map[y][x]
    if value == 9:
        return {(x, y)}
    
    end_points = set()
    for direction in Direction:
        neighbour_x, neighbour_y = direction.move_forward(x, y)

        if check_inbounds(map, neighbour_x, neighbour_y):
            if map[neighbour_y][neighbour_x] == value + 1:
                end_points.update(
                    reachable_ends(neighbour_x, neighbour_y)
                )

    return end_points

@register(10, 2024, 1)
def func_1(text):
    global map
    map = split_text(text, Split.INT_GRID)

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

        if check_inbounds(map, neighbour_x, neighbour_y):
            if map[neighbour_y][neighbour_x] == value + 1:
                rating += reachable_ends_rating(neighbour_x, neighbour_y)

    return rating

@register(10, 2024, 2)
def func_2(text):
    global map
    map = split_text(text, Split.INT_GRID)

    total = 0
    for y, line in enumerate(map):
        for x, value in enumerate(line):
            if value == 0:
                total += reachable_ends_rating(x, y)

    return total