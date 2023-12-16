from enum import Flag, auto
from aocd import get_data
from copy import deepcopy

class Direction(Flag):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

    def rotate(self, clockwise = True):
        if clockwise:
            if self == Direction.UP:
                return Direction.RIGHT
            elif self == Direction.RIGHT:
                return Direction.DOWN
            elif self == Direction.DOWN:
                return Direction.LEFT
            else:
                return Direction.UP
        else:
            if self == Direction.UP:
                return Direction.LEFT
            elif self == Direction.RIGHT:
                return Direction.UP
            elif self == Direction.DOWN:
                return Direction.RIGHT
            else:
                return Direction.DOWN

    def flip(self):
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.RIGHT:
            return Direction.LEFT
        elif self == Direction.DOWN:
            return Direction.UP
        else:
            return Direction.RIGHT
            
    def move_forward(self, x, y):
        if self == Direction.UP:
            return x, y - 1
        elif self == Direction.RIGHT:
            return x + 1, y
        elif self == Direction.DOWN:
            return x, y + 1
        else:
            return x - 1, y

    def in_direction_total(self, direction_total):
        if self in direction_total:
            return True

    def add_to_direction_total(self, direction_total):
        return self | direction_total

def energise_tiles(layout_matrix, energised_matrix, x, y, direction):
    while(y < len(layout_matrix) and y >= 0 and x < len(layout_matrix[0]) and x >= 0 and not direction.in_direction_total(energised_matrix[y][x])):
        energised_matrix[y][x] = direction.add_to_direction_total(energised_matrix[y][x])
        if layout_matrix[y][x] == ".":
            x, y = direction.move_forward(x, y)
        elif ((direction == Direction.UP or direction == Direction.DOWN) and layout_matrix[y][x] == "|") or ((direction == Direction.LEFT or direction == Direction.RIGHT) and layout_matrix[y][x] == "-"):
            x, y = direction.move_forward(x, y)
        elif  (layout_matrix[y][x] == "|" or layout_matrix[y][x] == "-"):
            direction = direction.rotate()
            other_direction = direction.flip()
            energise_tiles(layout_matrix, energised_matrix, x, y, other_direction)
        elif layout_matrix[y][x] == "/":
            if direction == Direction.LEFT or direction == Direction.RIGHT:
                direction = direction.rotate(False)
            else:
                direction = direction.rotate()
            x, y = direction.move_forward(x, y)
        elif layout_matrix[y][x] == "\\":
            if direction == Direction.LEFT or direction == Direction.RIGHT:
                direction = direction.rotate()
            else:
                direction = direction.rotate(False)
            x, y = direction.move_forward(x, y)
        else:
            raise Exception("Shouldnt be here")

def count(energised_matrix):
    count = 0
    for line in energised_matrix:
        for total in line:
            if bool(total):
                count += 1
    return count

def energise_1(text):
    layout_matrix = []
    energised_matrix = []
    for i, line in enumerate(text.split("\n")):
        layout_matrix.append([])
        energised_matrix.append([])
        for char in line:
            layout_matrix[-1].append(char)
            energised_matrix[-1].append(Direction(0))

    energise_tiles(layout_matrix, energised_matrix, 0, 0, Direction.RIGHT)

    return count(energised_matrix)

def energise_2(text):
    layout_matrix = []
    energised_matrix = []
    for i, line in enumerate(text.split("\n")):
        layout_matrix.append([])
        energised_matrix.append([])
        for char in line:
            layout_matrix[-1].append(char)
            energised_matrix[-1].append(Direction(0))

    max_count = 0
    
    for x in range(len(layout_matrix[0])):  
        this_energised_matrix = deepcopy(energised_matrix)

        energise_tiles(layout_matrix, this_energised_matrix, x, 0, Direction.DOWN)

        max_count = max(max_count, count(this_energised_matrix))

        this_energised_matrix = deepcopy(energised_matrix)

        energise_tiles(layout_matrix, this_energised_matrix, x, len(layout_matrix), Direction.UP)

        max_count = max(max_count, count(this_energised_matrix))

    for y in range(len(layout_matrix)):  
        this_energised_matrix = deepcopy(energised_matrix)

        energise_tiles(layout_matrix, this_energised_matrix, 0, y, Direction.RIGHT)

        max_count = max(max_count, count(this_energised_matrix))

        this_energised_matrix = deepcopy(energised_matrix)

        energise_tiles(layout_matrix, this_energised_matrix, len(layout_matrix[0]), y, Direction.LEFT)

        max_count = max(max_count, count(this_energised_matrix))

    return max_count

energise_text = get_data(day=16, year=2023)
print(energise_2(energise_text))