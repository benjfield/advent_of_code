from enum import Enum, auto, Flag, IntFlag
from advent.runner import register
class ElfDirection(Enum):
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()
    EAST = auto()

    @classmethod
    def possible_neighbours(cls, neighbours, coord, directions):
        for direction in directions:
            match direction:
                case ElfDirection.NORTH:
                    if (ElfNeighbours.NORTHWEST | ElfNeighbours.NORTH | ElfNeighbours.NORTHEAST) & neighbours == 0:
                        return (coord[0], coord[1] - 1)
                case ElfDirection.SOUTH:
                    if (ElfNeighbours.SOUTHWEST | ElfNeighbours.SOUTH | ElfNeighbours.SOUTHEAST) & neighbours == 0:
                        return (coord[0], coord[1] + 1)
                case ElfDirection.WEST:
                    if (ElfNeighbours.SOUTHWEST | ElfNeighbours.WEST | ElfNeighbours.NORTHWEST) & neighbours == 0:
                        return (coord[0] - 1, coord[1])
                case ElfDirection.EAST:
                    if (ElfNeighbours.SOUTHEAST | ElfNeighbours.EAST | ElfNeighbours.NORTHEAST) & neighbours == 0:
                        return (coord[0] + 1, coord[1])
        return None

class ElfNeighbours(IntFlag):
    NORTH = auto()
    NORTHEAST = auto()
    EAST = auto()
    SOUTHEAST = auto()
    SOUTH = auto()
    SOUTHWEST = auto()
    WEST = auto()
    NORTHWEST = auto()

    @classmethod
    def check_neighbours(self, coord, elves):
        neighbours = ElfNeighbours(0)

        if (coord[0], coord[1] - 1) in elves:
            neighbours |= ElfNeighbours.NORTH

        if (coord[0] + 1, coord[1] - 1) in elves:
            neighbours |= ElfNeighbours.NORTHEAST

        if (coord[0] + 1, coord[1]) in elves:
            neighbours |= ElfNeighbours.EAST

        if (coord[0] + 1, coord[1] + 1) in elves:
            neighbours |= ElfNeighbours.SOUTHEAST

        if (coord[0], coord[1] + 1) in elves:
            neighbours |= ElfNeighbours.SOUTH

        if (coord[0] - 1, coord[1] + 1) in elves:
            neighbours |= ElfNeighbours.SOUTHWEST

        if (coord[0] - 1, coord[1]) in elves:
            neighbours |= ElfNeighbours.WEST

        if (coord[0] - 1, coord[1] - 1) in elves:
            neighbours |= ElfNeighbours.NORTHWEST

        return neighbours

def get_bounds(elves):
    min_x = None
    max_x = None
    min_y = None
    max_y = None

    for elf in elves:
        if min_x is None:
            min_x = elf[0]
            max_x = elf[0]
            min_y = elf[1]
            max_y = elf[1]
        else:
            if elf[0] < min_x:
                min_x = elf[0]
            elif elf[0] > max_x:
                max_x = elf[0]

            if elf[1] < min_y:
                min_y = elf[1]
            elif elf[1] > max_y:
                max_y = elf[1]

    return max_x, min_x, max_y, min_y

def print_elves(elves, max_x, min_x, max_y, min_y):
    for y in range(min_y, max_y + 1):
        row_string = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in elves:
                row_string += "#"
            else:
                row_string += "."
        print(row_string)
    print("")

@register(23, 2022, 1, True)
def unstable_diffusion_1(split_text):
    elves = set()
    for y, line in enumerate(split_text):
        for x, char in enumerate(line):
            if char == "#":
                elves.add((x, y))

    directions = [
        ElfDirection.NORTH,
        ElfDirection.SOUTH,
        ElfDirection.WEST,
        ElfDirection.EAST
    ]

    for i in range(10):
        next_elves = {}
        invalid_spaces = set()

        for coord in elves:
            neighbours = ElfNeighbours.check_neighbours(coord, elves)
            if int(neighbours) > 0:
                neighbour_coord = ElfDirection.possible_neighbours(neighbours, coord, directions)
                if neighbour_coord is not None:
                    if neighbour_coord not in invalid_spaces:
                        if neighbour_coord in next_elves:
                            del next_elves[neighbour_coord]
                            invalid_spaces.add(neighbour_coord)
                        else:
                            next_elves[neighbour_coord] = coord
        
        for new_coord, old_coord in next_elves.items():
            elves.remove(old_coord)
            elves.add(new_coord)

        max_x, min_x, max_y, min_y = get_bounds(elves)

        directions = directions[1:] + [directions[0]]

    max_x, min_x, max_y, min_y = get_bounds(elves)

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves) 

@register(23, 2022, 2, True)
def unstable_diffusion_2(split_text):
    elves = set()
    for y, line in enumerate(split_text):
        for x, char in enumerate(line):
            if char == "#":
                elves.add((x, y))

    directions = [
        ElfDirection.NORTH,
        ElfDirection.SOUTH,
        ElfDirection.WEST,
        ElfDirection.EAST
    ]

    i = 0
    while True:
        i += 1
        next_elves = {}
        invalid_spaces = set()

        for coord in elves:
            neighbours = ElfNeighbours.check_neighbours(coord, elves)
            if int(neighbours) > 0:
                neighbour_coord = ElfDirection.possible_neighbours(neighbours, coord, directions)
                if neighbour_coord is not None:
                    if neighbour_coord not in invalid_spaces:
                        if neighbour_coord in next_elves:
                            del next_elves[neighbour_coord]
                            invalid_spaces.add(neighbour_coord)
                        else:
                            next_elves[neighbour_coord] = coord
        
        if len(next_elves) == 0:
            return i

        for new_coord, old_coord in next_elves.items():
            elves.remove(old_coord)
            elves.add(new_coord)

        directions = directions[1:] + [directions[0]]