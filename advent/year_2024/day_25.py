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

@register(25, 2024, 1)
def func_1(text):
    locks = []
    keys = []
    for block in text.split("\n\n"):
        block_lines = block.split("\n")
        heights = [0] * len(block_lines[0])

        for line in block_lines:
            for x, char in enumerate(line):
                if char == "#":
                    heights[x] += 1
        
        if block_lines[0][0] == ".":
            keys.append(heights)
        else:
            locks.append(heights)

    total = 0
    for key in keys:
        for lock in locks:
            valid_combo = True
            for i in range(len(block_lines[0])):
                if key[i] + lock[i] > 7:
                    valid_combo = False
                    break
            
            if valid_combo:
                total += 1

    return total