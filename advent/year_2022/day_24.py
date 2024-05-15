from enum import Enum, auto, Flag, IntFlag
from advent.runner import register
from advent.utils.direction import Direction
from advent.utils.path_finding import djikstra, Node
from functools import partial


class BlizzardNode(Node):
    def __init__(self, x, y, round):
       self.x = x
       self.y = y
       self.round = round

    def get_neighbours(self, maps, cost):
        next_round = self.round + 1
        if len(maps) == next_round:
            add_new_map(maps)
        elif next_round > len(maps):
            raise Exception

        neighbours = []

        for x, y in [
            (self.x, self.y),
            (self.x - 1, self.y), 
            (self.x + 1, self.y), 
            (self.x, self.y - 1), 
            (self.x, self.y + 1)
        ]:
            
            if y >= 0 and y <= len(maps[-1]) - 1:
                if maps[next_round][y][x] is not None and maps[next_round][y][x] == Direction(0):
                    possible_neighbour = type(self)(
                        x=x,
                        y=y,
                        round=next_round
                    )
                    self.append_neighbours(neighbours, possible_neighbour, next_round)
                
        return neighbours
        
    def __hash__(self):
        return hash((self.x, self.y, self.round))
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.round == other.round:
            return True
        return False

    def __str__(self):
        return f"x {self.x} y {self.y} round {self.round}"
    
def add_new_map(maps):
    new_map = []
    for row in maps[-1]:
        new_map.append([])
        for tile in row:
            if tile is None:
                new_map[-1].append(None)
            else:
                new_map[-1].append(Direction(0))

    for y, row in enumerate(maps[-1]):
        for x, tile in enumerate(row):
            if tile is not None:
                if tile & Direction.UP:
                    if y == 1:
                        next_y = len(maps[-1]) - 2
                    else:
                        next_y = y - 1
                    
                    new_map[next_y][x] |= Direction.UP
                    
                if tile & Direction.RIGHT:
                    if x == len(maps[-1][y]) - 2:
                        next_x = 1
                    else:
                        next_x = x + 1
                    
                    new_map[y][next_x] |= Direction.RIGHT
                    
                if tile & Direction.DOWN:
                    if y == len(maps[-1]) - 2:
                        next_y = 1
                    else:
                        next_y = y + 1
                    
                    new_map[next_y][x] |= Direction.DOWN   

                if tile & Direction.LEFT:
                    if x == 1:
                        next_x = len(maps[-1][y]) - 2
                    else:
                        next_x = x - 1
                    
                    new_map[y][next_x] |= Direction.LEFT

    maps.append(new_map)

def is_final_blizzard_node(final_x, final_y, this_node):
    if this_node.x == final_x and this_node.y == final_y:
        return True
    else:
        return False

def is_final_blizzard_node_function(final_x, final_y):
    return partial(is_final_blizzard_node, final_x, final_y)

@register(24, 2022, 1, True)
def blizzard_basin_1(split_text):
    map = []
    for line in split_text:
        map.append([])
        for char in line:
            if char == "#":
                map[-1].append(None)
            elif char == ".":
                map[-1].append(Direction(0))
            else:
                map[-1].append(Direction.direction_from_arrow(char))

    maps = [map]

    start_point = BlizzardNode(
        1,
        0,
        0
    )

    terminate_function = is_final_blizzard_node_function(len(map[-1]) - 2, len(map) - 1)

    return djikstra(maps, start_point, terminate_function=terminate_function) - 1


@register(24, 2022, 2, True)
def blizzard_basin_2(split_text):
    map = []
    for line in split_text:
        map.append([])
        for char in line:
            if char == "#":
                map[-1].append(None)
            elif char == ".":
                map[-1].append(Direction(0))
            else:
                map[-1].append(Direction.direction_from_arrow(char))

    maps = [map]

    start_point = BlizzardNode(
        1,
        0,
        0
    )

    terminate_function = is_final_blizzard_node_function(len(map[-1]) - 2, len(map) - 1)

    time = djikstra(maps, start_point, terminate_function=terminate_function)

    start_point = BlizzardNode(
        len(map[-1]) - 2,
        len(map) - 1,
        time
    )

    terminate_function = is_final_blizzard_node_function(1, 0)

    time = djikstra(maps, start_point, terminate_function=terminate_function)

    start_point = BlizzardNode(
        1,
        0,
        time
    )

    terminate_function = is_final_blizzard_node_function(len(map[-1]) - 2, len(map) - 1)

    return djikstra(maps, start_point, terminate_function=terminate_function) - 1