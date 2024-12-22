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

def next_secret_number(secret_number):
    new_secret_number = ((secret_number * 64) ^ secret_number) % 16777216

    new_secret_number = ((new_secret_number // 32) ^ new_secret_number) % 16777216

    return ((new_secret_number * 2048) ^ new_secret_number) % 16777216

def secret_number_loop(secret_number, count=2000):
    for i in range(count):
        secret_number = next_secret_number(secret_number)
    return secret_number

def price_change_loop(changes_total, secret_number, count = 2000):
    seen_changes = set()
    last_price = secret_number % 10

    sequence = 0

    for i in range(count):
        secret_number = next_secret_number(secret_number)
        price = secret_number % 10

        sequence = (sequence * 20 + price - last_price + 10) % (20 ** 4) 

        if i >= 3:
            if sequence not in seen_changes:
                changes_total[sequence] += price
                seen_changes.add(sequence)
        
        last_price = price

@register(22, 2024, 1)
def func_1(text):
    total = 0
    for x in split_text(text, split_type=Split.LINE):
        number = int(x)
        result = secret_number_loop(number)
        total += result
        
    return total

@register(22, 2024, 2)
def func_2(text):
    changes_total = defaultdict(int)
    for x in split_text(text, split_type=Split.LINE):
        price_change_loop(changes_total, int(x))

    return max(changes_total.values())