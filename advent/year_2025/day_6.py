from typing import Self
from advent.runner import register
from advent.utils.split_text import create_char_grid
from advent.utils.grid import Grid
from dataclasses import dataclass

@register(6, 2025, 1, True)
def trash_1(text):
    elements = []
    operations = []

    for i, line in enumerate(text):
        for j, element in enumerate(line.split()):
            if i == 0:
                elements.append([int(element)])
            elif i == len(text) - 1:
                operations.append(element)
            else:
                elements[j].append(int(element))

    total = 0

    for i, operation in enumerate(operations):
        if operation == "*":
            subtotal = 1
            for val in elements[i]:
                subtotal *= val
        else:
            subtotal = 0
            for val in elements[i]:
                subtotal += val

        total += subtotal

    return total

@register(6, 2025, 2, True)
def trash_2(text):
    as_chars = [[x for x in line] for line in text]

    total = 0
    for x in range(0, len(as_chars[0])):
        number_string = ""
        if not as_chars[len(as_chars) - 1][x].isspace():
            operation = as_chars[len(as_chars) - 1][x]
            if operation == "*":
                subtotal = 1
            else:
                subtotal = 0
        for y in range(0, len(as_chars) - 1):
            number_string += as_chars[y][x]

        if number_string.isspace():
            total += subtotal
        else:
            number = int(number_string.strip())
            if operation == "*":
                subtotal *= number
            else:
                subtotal += number
    total += subtotal

    return total