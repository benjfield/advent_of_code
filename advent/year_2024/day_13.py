from advent.runner import register
from advent.utils.split_text import split_text, Split
from dataclasses import dataclass
import math
from functools import cache
from collections import defaultdict

from advent.utils.direction import Direction

from time import perf_counter

import re

@register(13, 2024, 1)
def func_1(text):
    inputs = text.split("\n\n")

    cost = 0
    for input in inputs:
        match = re.match(r"Button A: X([\+\-]\d+), Y([\+\-]\d+)\nButton B: X([\+\-]\d+), Y([\+\-]\d+)\nPrize: X=([\+\-]?\d+), Y=([\+\-]?\d+)", input)

        x_a = int(match.group(1))
        y_a = int(match.group(2))
        x_b = int(match.group(3))
        y_b = int(match.group(4))
        x_total = int(match.group(5))
        y_total = int(match.group(6))

        b_presses = (x_a * y_total - y_a * x_total) / (x_a * y_b - y_a * x_b)

        if b_presses.is_integer():
            a_presses = (x_total - x_b * b_presses) / x_a

            if a_presses.is_integer():

                if a_presses <= 100 and b_presses <= 100:
                    cost += a_presses *3 + b_presses*1

    return cost

@register(13, 2024, 2)
def func_2(text):
    inputs = text.split("\n\n")

    cost = 0
    for input in inputs:
        match = re.match(r"Button A: X([\+\-]\d+), Y([\+\-]\d+)\nButton B: X([\+\-]\d+), Y([\+\-]\d+)\nPrize: X=([\+\-]?\d+), Y=([\+\-]?\d+)", input)

        x_a = int(match.group(1))
        y_a = int(match.group(2))
        x_b = int(match.group(3))
        y_b = int(match.group(4))
        x_total = int(match.group(5)) + 10000000000000
        y_total = int(match.group(6)) + 10000000000000

        b_presses = (x_a * y_total - y_a * x_total) / (x_a * y_b - y_a * x_b)

        if b_presses.is_integer():
            a_presses = (x_total - x_b * b_presses) / x_a

            if a_presses.is_integer():
                cost += a_presses *3 + b_presses*1

    return cost