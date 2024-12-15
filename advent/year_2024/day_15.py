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
    
def score_warehouse_1(char, x, y):
    if char == "O":
        return 100 * y + x
    else:
        return 0
    
@register(15, 2024, 1)
def func_1(text):
    ts = text.split("\n\n")

    grid = split_text(ts[0], Split.CHAR_GRID, True)
    
    for x, line in enumerate(grid.grid):
        for y, char in enumerate(line):
            if char == "@":
                bot_coords = (x, y)
                grid.set(bot_coords, ".")

    directions = []
    for arrow in ts[1]:
        if arrow in {">", "<", "v", "^"}:
            directions.append(Direction.direction_from_arrow(arrow))
        
    for direction in directions:
        next_bot_coords = direction.move_forward(bot_coords)
        
        next_char = grid.get(next_bot_coords)
        if next_char == "O":
            final_bot_coords = next_bot_coords
            while grid.get(final_bot_coords) == "O":
                final_bot_coords = direction.move_forward(final_bot_coords)

            final_char = grid.get(final_bot_coords)
            if final_char == ".":
                grid.set(final_bot_coords, "O")
                grid.set(next_bot_coords, ".")
                bot_coords = next_bot_coords
            elif final_char == "#":
                pass
            else:
                raise Exception
        elif next_char == ".":
                bot_coords = next_bot_coords
        else:
            pass
                                
    return grid.score(score_warehouse_1)

def override_print_warehouse(bot_x, bot_y, char, x, y):
    if x == bot_x and y == bot_y:
        return "@"
    else:
        return char   
    
def score_warehouse_2(char, x, y):
    if char == "[":
        return 100 * y + x
    else:
        return 0

@register(15, 2024, 2)
def func_2(text):
    ts = text.split("\n\n")
    
    grid = []

    for x, line in enumerate(ts[0].split("\n")):
        grid.append([])
        for y, char in enumerate(line):
            if char == "#":
                grid[-1].append("#")
                grid[-1].append("#")
            elif char == "O":
                grid[-1].append("[")
                grid[-1].append("]")
            elif char == ".":
                grid[-1].append(".")
                grid[-1].append(".")
            elif char == "@":
                bot_coords = (2 * x, y)
                grid[-1].append(".")
                grid[-1].append(".")

    grid = Grid(grid)

    directions = []
    for arrow in ts[1]:
        if arrow in {">", "<", "v", "^"}:
            directions.append(Direction.direction_from_arrow(arrow))
        
    for direction in directions:
        next_bot_coords = direction.move_forward(bot_coords)

        next_char = grid.get(next_bot_coords)
        if next_char in {"[", "]"}:
            if direction in {Direction.UP, Direction.DOWN}:
                this_row_coords = [next_bot_coords]
                potential_moves = []
                wall = False
                while len(this_row_coords) > 0 and not wall:
                    coords_to_check = []
                    for coord in this_row_coords:
                        char = grid.get(coord)
                        next_coord = direction.move_forward(coord)
                        coords_to_check.append(next_coord)

                        potential_moves.append((coord, char, next_coord))

                        if char == "[":
                            coords_to_check.append(Direction.RIGHT.move_forward(next_coord))
                            potential_moves.append((Direction.RIGHT.move_forward(coord), "]", Direction.RIGHT.move_forward(next_coord)))
                        else:
                            coords_to_check.append(Direction.LEFT.move_forward(next_coord))
                            potential_moves.append((Direction.LEFT.move_forward(coord), "[", Direction.LEFT.move_forward(next_coord)))

                    this_row_coords = []
                    for coord in coords_to_check:
                        char = grid.get(coord)
                        if char in {"[", "]"}:
                            this_row_coords.append(coord)
                        elif char == "#":
                            wall = True

                if not wall:
                    for old_coord, tile, new_coord in reversed(potential_moves):
                        grid.set(new_coord, tile)
                        grid.set(old_coord, ".")
                    bot_coords = next_bot_coords
            else:
                final_bot_coords = next_bot_coords

                potential_moves = []
                while grid.get(final_bot_coords) in {"[", "]"}:
                    potential_moves.append((final_bot_coords, grid.get(final_bot_coords), direction.move_forward(final_bot_coords)))
                    final_bot_coords = direction.move_forward(final_bot_coords)

                char = grid.get(final_bot_coords)
                if char == ".":
                    for old_coord, tile, new_coord in reversed(potential_moves):
                        grid.set(new_coord, tile)
                        grid.set(old_coord, ".")
                    bot_coords = next_bot_coords
                elif char == "#":
                    pass
                else:
                    raise Exception
        elif next_char == ".":
                    bot_coords = next_bot_coords
        else:
            pass
                
    return grid.score(score_warehouse_2)