from advent.runner import register
from advent.utils.split_text import split_text, Split
from advent.utils.grid import Grid
from dataclasses import dataclass
import math
from functools import cache
from collections import defaultdict

from advent.utils.direction import Direction, Rotation

from time import perf_counter

import re

from functools import partial

from advent.utils.path_finding_2 import MapNode, djikstra, has_final_coords_function, ClosedList
from dataclasses import dataclass
from enum import Enum, auto
   
def manhattan_distance(first_coord: tuple[int, int], second_coord: tuple[int, int]):
    return abs(first_coord[0] - second_coord)

@dataclass
class Map:
    width: int
    height: int
    walls: set[tuple[int, int]]

    def check_node(self, coord):
        return coord not in self.walls

    def is_wall(self, coord):
        return coord in self.walls

    def is_path(self, coord):
        return (coord[0] >=0 and coord[0] <= self.width and coord[1] >= 0 and coord[1] <= self.height) and coord not in self.walls

    def is_removable_wall(self, coord):
        return (coord[0] > 0 and coord[0] < self.width and coord[1] > 0 and coord[1] < self.height) and coord in self.walls              

@register(20, 2024, 1)
def func_1(text, saving_to_make=100):
    split_text = text.split("\n")
    width = len(split_text) - 1
    map = Map(width, width, set())
    for y, line in enumerate(split_text):
        for x, char in enumerate(line):
            coord = (x, y)
            match char:
                case "#":
                    #print(coord)
                    map.walls.add(coord)
                case "S":
                    start = coord
                case "E":
                    finish = coord

    start = MapNode(start)
                    
    node_store = djikstra(map, start, None, False).store

    shortcuts = defaultdict(list)

    for start_node, start_node_cost in node_store.items():
        distance = 2
        for abs_x in range(distance + 1):
            abs_y = distance - abs_x
            for x in {-abs_x, abs_x}:
                for y in {-abs_y, abs_y}:
                    end_coord = (start_node.coord[0] + x, start_node.coord[1] + y)
                    end_node = MapNode(end_coord)

                    if end_node in node_store:
                        end_node_cost = node_store[end_node]

                        saving = end_node_cost.get_cost() - (start_node_cost.get_cost() + distance)
                        if saving >= saving_to_make:
                            shortcuts[start_node].append(end_node)

    shortcut_count = 0
    for start, shortcut_ends in shortcuts.items():
        shortcut_count += len(shortcut_ends)

    return shortcut_count

@register(20, 2024, 2)
def func_2(text, saving_to_make=100):
    split_text = text.split("\n")
    width = len(split_text) - 1
    map = Map(width, width, set())
    for y, line in enumerate(split_text):
        for x, char in enumerate(line):
            coord = (x, y)
            match char:
                case "#":
                    #print(coord)
                    map.walls.add(coord)
                case "S":
                    start = coord
                case "E":
                    finish = coord

    start = MapNode(start)
                    
    node_store = djikstra(map, start, None, False).store

    shortcuts = defaultdict(list)

    for start_node, start_node_cost in node_store.items():
        for distance in range(2, 21):
            for abs_x in range(distance + 1):
                abs_y = distance - abs_x
                for x in {-abs_x, abs_x}:
                    for y in {-abs_y, abs_y}:
                        end_coord = (start_node.coord[0] + x, start_node.coord[1] + y)
                        end_node = MapNode(end_coord)

                        if end_node in node_store:
                            end_node_cost = node_store[end_node]

                            saving = end_node_cost.get_cost() - (start_node_cost.get_cost() + distance)
                            if saving >= saving_to_make:
                                shortcuts[start_node].append(end_node)

    shortcut_count = 0
    for start, shortcut_ends in shortcuts.items():
        shortcut_count += len(shortcut_ends)

    return shortcut_count