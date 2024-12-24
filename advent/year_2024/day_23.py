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
from numba import jit

@dataclass
class Computer:
    name: str
    sorted_neighbours: list
    neighbours: set
    greater_neighbours: list

    def add_neighbour(self, other):
        if other.name > self.name:
            self.sorted_neighbours.append(other)
            self.greater_neighbours.add(other)
        
        self.neighbours.add(other)

    def sort_neighbours(self):
        self.sorted_neighbours.sort(key= lambda n: n.name)

    def get_three_set(self, path):
        if len(path) == 2:
            if path[0] in self.neighbours:
                path = path.copy()
                path.append(self)

                for n in path:
                    if n.name[0] == "t":
                        return [path]

            return []
        else:
            path = path.copy()
            path.append(self)

            paths = []
            for neighbour in self.sorted_neighbours:
                next_paths = neighbour.get_three_set(path)

                paths += next_paths

            return paths

    @cache
    def get_biggest_remainder(self, start_node):
        biggest_remainder = []

        for neighbour in self.sorted_neighbours:
            possible_biggest_remainder = neighbour.get_biggest_remainder(start_node)

            if len(possible_biggest_remainder) >= len(biggest_remainder):
                biggest_remainder = possible_biggest_remainder

        if len(biggest_remainder) == 0:
            if start_node in self.neighbours:
                return [self]
            else:
                return []

        return [self] + biggest_remainder
    
    def get_biggest_set(self, our_biggest_set, possible_nodes):    
        if len(our_biggest_set) == 0:
            our_biggest_set = [self.name]
            possible_nodes = self.greater_neighbours
        else:
            our_biggest_set = our_biggest_set.copy()
            our_biggest_set.append(self.name)
            possible_nodes = possible_nodes.intersection(self.greater_neighbours)

        biggest_set = our_biggest_set

        for n in possible_nodes:
            possible_biggest_set = n.get_biggest_set(our_biggest_set, possible_nodes)

            if len(possible_biggest_set) > len(biggest_set):
                biggest_set = possible_biggest_set

        return biggest_set
        
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, value):
        return self.name == value.name 
    
    def __str__(self):
        return self.name
        
@register(23, 2024, 1)
def func_1(text):
    computers = {}
    for line in split_text(text, Split.LINE):
        split_line = line.split("-")

        comp_1_name = split_line[0]
        if comp_1_name in computers:
            comp_1 = computers[comp_1_name]
        else:
            comp_1 = Computer(comp_1_name, [], set(), set())
            computers[comp_1_name] = comp_1

        comp_2_name = split_line[1]
        if comp_2_name in computers:
            comp_2 = computers[comp_2_name]
        else:
            comp_2 = Computer(comp_2_name, [], set(), set())
            computers[comp_2_name] = comp_2

        comp_1.add_neighbour(comp_2)
        comp_2.add_neighbour(comp_1)

    for comp in computers.values():
        comp.sort_neighbours()

    paths = []
    for comp in computers.values():
        paths += comp.get_three_set([])

    return len(paths)

@register(23, 2024, 2)
def func_2(text):
    computers = {}
    for line in split_text(text, Split.LINE):
        split_line = line.split("-")

        comp_1_name = split_line[0]
        if comp_1_name in computers:
            comp_1 = computers[comp_1_name]
        else:
            comp_1 = Computer(comp_1_name, [], set(), set())
            computers[comp_1_name] = comp_1

        comp_2_name = split_line[1]
        if comp_2_name in computers:
            comp_2 = computers[comp_2_name]
        else:
            comp_2 = Computer(comp_2_name, [], set(), set())
            computers[comp_2_name] = comp_2

        comp_1.add_neighbour(comp_2)
        comp_2.add_neighbour(comp_1)

    biggest_set = []
    for comp in computers.values():
        possible_biggest_set = comp.get_biggest_set([], set())

        if len(possible_biggest_set) > len(biggest_set):
            biggest_set = possible_biggest_set

    return ",".join(biggest_set)