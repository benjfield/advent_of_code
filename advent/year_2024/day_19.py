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
from enum import Enum, auto

towel_patterns = {}

class Stripe(Enum):
    WHITE = auto()
    BLUE = auto()
    BLACK = auto()
    RED = auto()
    GREEN = auto()

    @classmethod 
    def from_letter(cls, letter):
        match letter:
            case "w":
                return cls.WHITE
            case "u":
                return cls.BLUE
            case "b":
                return cls.BLACK
            case "r":
                return cls.RED
            case "g":
                return cls.GREEN
            case _:
                return Exception

def towelSolver(remaining_stripes):
    for towel in towel_patterns[remaining_stripes[0]]:
        if remaining_stripes[:len(towel)] == towel:
            if len(remaining_stripes) == len(towel):
                return True
            else:
                if towelSolver(remaining_stripes[len(towel):]):
                    return True
                
    return False

@register(19, 2024, 1)
def func_1(text):
    global towel_patterns
    towel_patterns = defaultdict(list)
    
    split_text = text.split("\n\n")
    for letters in split_text[0].split(", "):
        towel = []
        for letter in letters:
            towel.append(Stripe.from_letter(letter))
        towel_patterns[towel[0]].append(towel)
    count = 0
    for pattern in split_text[1].split("\n"):
        stripes = []
        for letter in pattern:
            stripes.append(Stripe.from_letter(letter))
        if towelSolver(stripes):
            count += 1

    return count

@cache
def towelSolverCount(remaining_stripes):
    count = 0
    for towel in towel_patterns[remaining_stripes[0]]:
        if remaining_stripes[:len(towel)] == towel:
            if len(remaining_stripes) == len(towel):
                count += 1
            else:
                count += towelSolverCount(tuple(remaining_stripes[len(towel):]))
                
    return count

@register(19, 2024, 2)
def func_2(text):
    global towel_patterns
    towel_patterns = defaultdict(list)
    
    split_text = text.split("\n\n")
    for letters in split_text[0].split(", "):
        towel = []
        for letter in letters:
            towel.append(Stripe.from_letter(letter))
        towel_patterns[towel[0]].append(tuple(towel))

    count = 0
    for pattern in split_text[1].split("\n"):
        stripes = []
        for letter in pattern:
            stripes.append(Stripe.from_letter(letter))

        count += towelSolverCount(tuple(stripes)) 

    return count