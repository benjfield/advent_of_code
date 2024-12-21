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
   
from itertools import permutations

alphanumeric_positions = {
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "A": (2, 3),
    "I": (0, 3),
}

direction_positions = {
    "^": (1, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
    "A": (2, 0),
    "I": (0, 0),
}

class KeypadType(Enum):
    ALPHANUMERIC = auto()
    DIRECTION = auto()

@cache
def encode_phrase_1(code, origin_type):
    match origin_type:
        case KeypadType.ALPHANUMERIC:
            position_dict = alphanumeric_positions
        case KeypadType.DIRECTION:
            position_dict = direction_positions
        case _:
            raise Exception

    invalid_position = position_dict["I"]
    current_position = position_dict["A"]

    for i, letter in enumerate(code):
        destination = position_dict[letter]
        encoding = encode_move(destination, current_position, invalid_position)
        current_position = destination

        if i == 0:
            results = list(encoding)
        else:
            new_results = []
            for result in results:
                for encode in encoding:
                    new_results.append(result + encode)
            results = new_results

    return results

def shortest_phrases(phrases):
    shortest_length = 1000000
    for result in phrases:
        if len(result) < shortest_length:
            shortest_length = len(result)
    
    return [x for x in phrases if len(x) == shortest_length]

@cache
def encode_move(destination, current_position, invalid_position):
    encoding = []  

    if destination[0] > current_position[0]:
        encoding += [">"] * (destination[0] - current_position[0])
    else:
        encoding += ["<"] * abs(destination[0] - current_position[0])

    if destination[1] > current_position[1]:
        encoding += ["v"] * (destination[1] - current_position[1])
    else:
        encoding += ["^"] * abs(destination[1] - current_position[1])

    final_encodes = set()

    for ordering in permutations(encoding, len(encoding)):
        valid_order = True
        finger_position = current_position
        for letter in ordering:
            direction = Direction.direction_from_arrow(letter)
            finger_position = direction.move_forward(finger_position)
            if finger_position == invalid_position:
                valid_order = False
                break
        
        if valid_order:
            final_encodes.add(tuple(ordering) + tuple("A"))

    return final_encodes

@cache
def get_min_length(phrase, current_depth, max_depth=3):
    if current_depth == max_depth:
        return len(phrase)
    else:   
        match current_depth:
            case 0:
                position_dict = alphanumeric_positions
            case _:
                position_dict = direction_positions

        invalid_position = position_dict["I"]
        current_position = position_dict["A"]

        length = 0
        for char in phrase:
            destination = position_dict[char]
            encoding = encode_move(destination, current_position, invalid_position)

            min_length = min([get_min_length(x, current_depth + 1, max_depth) for x in encoding])
            
            length += min_length
            current_position = destination
        return length

def decode_code(code, return_position):
    reverse_dict = {}

    for k, v in return_position.items():
        reverse_dict[v] = k

    current_position = return_position["A"]
    result = []

    for letter in code:
        if letter == "A":
            result.append(reverse_dict[current_position])
        else:
            direction = Direction.direction_from_arrow(letter)
            current_position = direction.move_forward(current_position)
    
    return result

@register(21, 2024, 1)
def func_1(text):
    complexity = 0
    for line in split_text(text, Split.LINE):
        length = get_min_length(line, 0)

        match = re.match(r"(\d+)A", line)

        complexity += length * int(match.group(1))

    return complexity

@register(21, 2024, 2)
def func_2(text):
    complexity = 0
    for line in split_text(text, Split.LINE):
        length = get_min_length(line, 0, 26)

        match = re.match(r"(\d+)A", line)

        complexity += length * int(match.group(1))

    return complexity