from advent.runner import register
import numpy as np
from scipy import optimize
import math

@register(12, 2025, 1, True)
def presents_1(text):
    shape_sizes = []
    for i in range(6):
        number_of_tiles = 0 
        for line in text[i*5:(i+1)*5]:
            for char in line:
                if char == "#":
                    number_of_tiles += 1
        shape_sizes.append(number_of_tiles)

    count = 0
    for line in text[30:]:
        details = line.split(":") 

        coords = [int(x) for x in details[0].split("x")]

        size = (coords[0] // 3) * (coords[1] // 3)

        number_of_shapes = [int(x) for x in details[1].strip().split(" ")]

        total_number = sum(number_of_shapes)

        if size >= total_number:
            count += 1
        else:
            total_tiles = 0
            for i in range(len(shape_sizes)):
                total_tiles += shape_sizes[i] * number_of_shapes[i]

            if total_tiles <= coords[0] * coords[1]:
                raise Exception("Possibly solvable")

    return count 
         


