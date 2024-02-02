from advent.runner import register
from advent.year_2019.computer import computer_from_string
from advent.utils.binary_search import find_first
import numpy as np
from functools import partial

@register(19, 2019, 1)
def tractor_1(text, grid_size=50):
    computer = computer_from_string(text)
    total = 0
    coordinates = np.zeros(2, dtype=np.int32)
    for x in range(grid_size):
        for y in range(grid_size):
            coordinates[0] = x
            coordinates[1] = y
            if is_in_beam(computer, coordinates):
                total += 1

    return total

lower_edges = {}
higher_edges = {}

def is_in_beam(computer, coordinates):
    computer.reset()
    finished, output = computer.process(coordinates)
    if output[0] == 1:
        return True
    return False

def is_in_beam_row(computer, coordinates, reverse, value):
    coordinates[0] = value
    if reverse:
        return not is_in_beam(computer, coordinates)
    return is_in_beam(computer, coordinates)

def find_lower_edge_on_row_function(computer, coordinates):
    return partial(is_in_beam_row, computer, coordinates, False)

def find_lower_edge_on_row(computer, coordinates, minimum_bound, maximum_bound):
    check_function = find_lower_edge_on_row_function(computer, coordinates)
    return find_first(check_function, minimum_bound, maximum_bound)

def find_higher_edge_on_row_function(computer, coordinates):
    return partial(is_in_beam_row, computer, coordinates, True)

def find_higher_edge_on_row(computer, coordinates, minimum_bound, maximum_bound):
    check_function = find_higher_edge_on_row_function(computer, coordinates)
    return find_first(check_function, minimum_bound, maximum_bound) - 1

def is_in_beam_column(computer, coordinates, reverse, value):
    coordinates[1] = value
    if reverse:
        return not is_in_beam(computer, coordinates)
    return is_in_beam(computer, coordinates)

def find_bottom_edge_on_column_function(computer, coordinates):
    return partial(is_in_beam_column, computer, coordinates, True)

def find_bottom_edge_on_column(computer, coordinates, minimum_bound, maximum_bound):
    check_function = find_bottom_edge_on_column_function(computer, coordinates)
    return find_first(check_function, minimum_bound, maximum_bound) - 1
        
def find_edges_in_row(computer, row, coordinates):
    #Assumption on width
    minimum_width = int(row/10)

    start_possible_beam = minimum_width * 3
    final_possible_beam = minimum_width * 14

    coordinates[1] = row
    prior_x = 0
    for x in range(start_possible_beam, final_possible_beam, minimum_width):
        coordinates[0] = x
        if is_in_beam(computer, coordinates):
            lower_edge = find_lower_edge_on_row(computer, coordinates, prior_x, x - 1)
            lower_edges[row] = lower_edge
            higher_edge = find_higher_edge_on_row(computer, coordinates, x + 1, final_possible_beam)
            higher_edges[row] = higher_edge
            if final_possible_beam == higher_edge:
                raise Exception("Assumption on maximum beam are invalid")
            return lower_edge, higher_edge
        prior_x = x + 1
    raise Exception("Didnt find any beam")

def find_bottom_edge_at_width(computer, coordinates, row, requested_width = 100):
    lower_edge, higher_edge = find_edges_in_row(computer, row, coordinates)

    width = higher_edge - lower_edge + 1

    column_to_find_height = higher_edge - requested_width + 1
    if column_to_find_height >= lower_edge:
        coordinates[0] = column_to_find_height

        bottom_edge = find_bottom_edge_on_column(computer, coordinates, row + 1, row + 4 * width)
        return bottom_edge
    else:
        return 0
        
def is_height_100_at_width(computer, coordinates, row_to_check):
    height = find_bottom_edge_at_width(computer, coordinates, row_to_check) - row_to_check + 1
    return height >= 100

def find_highest_row_with_height_function(computer, coordinates):
    return partial(is_height_100_at_width, computer, coordinates)

def find_highest_row_with_height(computer, coordinates, minimum_bound, maximum_bound):
    check_function = find_highest_row_with_height_function(computer, coordinates)
    return find_first(check_function, minimum_bound, maximum_bound)

@register(19, 2019, 2)
def tractor_2(text):
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)

    every_row_to_check = 100

    lower_row_bound = 0

    i = 1
    while True:
        row = every_row_to_check * i
        bottom_edge = find_bottom_edge_at_width(computer, coordinates, row)

        height = bottom_edge - row + 1

        if height > 100:
            highest_row = find_highest_row_with_height(computer, coordinates, lower_row_bound + 1, row - 1)

            lower_edge = lower_edges[highest_row]
            higher_edge = higher_edges[highest_row]

            for j in range(lower_edge, higher_edge - 100 + 1):
                coordinates[0] = j
                bottom_edge = find_bottom_edge_on_column(computer, coordinates, highest_row + 1, highest_row + 101)

                #Could do binary search here but leaving it for now
                if bottom_edge - highest_row + 1 == 100:
                    return j * 10000 + highest_row
            return (higher_edge - 100 + 1) * 10000 + highest_row
        else:
            lower_row_bound = row
            i += 1
