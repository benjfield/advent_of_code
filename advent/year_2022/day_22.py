from advent.runner import register
from enum import Enum, auto
from advent.utils.direction import Direction, Rotation
import re

class Tile(Enum):
    SPACE = auto()
    WALL = auto()
    WRAP = auto()

    @classmethod
    def get_tile_from_text(cls, text_tile):
        match text_tile:
            case " ":
                return Tile.WRAP
            case "#":
                return Tile.WALL
            case ".":
                return Tile.SPACE
            case "_":
                raise Exception

    def get_text_from_tile(self):
        match self:
            case Tile.SPACE:
                return "."
            case Tile.WALL:
                return "#"
            case Tile.WRAP:
                return " "

class Space:
    def __init__(
        self,
        x,
        y
    ):
        self.x = x
        self.y = y
        self.neighbours = {}

    def populate_neighbours(
        self,
        tiles,
        spaces
    ):
        other_side = {
            Direction.UP: (self.x, -1),
            Direction.RIGHT: (-1, self.y),
            Direction.DOWN: (self.x, 0),
            Direction.LEFT: (0, self.y),
        }

        for direction in Direction:
            coord = direction.move_forward_x_and_y(self.x, self.y)
            
            if tiles[coord[1]][coord[0]] == Tile.WRAP:
                coord = other_side[direction]

                while tiles[coord[1]][coord[0]] == Tile.WRAP:
                    coord = direction.move_forward_x_and_y(coord[0], coord[1])

            if tiles[coord[1]][coord[0]] == Tile.SPACE:

                if coord[1] < 0:
                    y = len(tiles) + coord[1]
                else:
                    y = coord[1]

                if coord[0] < 0:
                    x = len(tiles[y]) + coord[0]
                else:
                    x = coord[0]

                self.neighbours[direction] = spaces[(x, y)]
            elif tiles[coord[1]][coord[0]] == Tile.WALL:
                self.neighbours[direction] = self

    def move(
        self,
        direction
    ):
        return self.neighbours[direction]

def preprocess_print_tiles(tiles):
    tiles_strings = []
    for line in tiles:
        line_string = ""
        for tile in line:
            line_string += tile.get_text_from_tile()
        tiles_strings.append(line_string)
    return tiles_strings

def print_tiles(tiles_strings, current_position, direction):
    for y, row in enumerate(tiles_strings):
        if y != current_position.y:
            print(row)
        else:
            row_string = ""
            for x, tile in enumerate(row):
                if x != current_position.x:
                    row_string += tile
                else:
                    row_string += direction.arrow_from_direction()
            print(row_string)

@register(22, 2022, 1, True)
def monkey_map_1(split_text):
    max_line_length = 0
    for line in split_text[:-2]:
        if len(line) > max_line_length:
            max_line_length = len(line)

    tiles = [[Tile.WRAP for x in range(max_line_length + 2)]]

    for line in split_text[:-2]:
        tiles.append([Tile.get_tile_from_text(tile) for tile in " " + line])

        wraps_to_add = max_line_length + 1 - len(line)
        for i in range(wraps_to_add):
            tiles[-1].append(Tile.WRAP)

    tiles.append([Tile.WRAP for x in range(max_line_length + 2)])

    tiles_strings = preprocess_print_tiles(tiles)
    spaces = {}

    current_position = None

    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if tile == Tile.SPACE:
                this_space = Space(x, y)
                spaces[(x, y)] = this_space

                if current_position is None:
                    current_position = this_space

    for space in spaces.values():
        space.populate_neighbours(tiles, spaces)

    direction = Direction.RIGHT

    parsed_command = re.search(r"(\d+)([LR]{0,1})(.*)", split_text[-1])

    #print_tiles(tiles_strings, current_position, direction)
    while parsed_command is not None:
        for i in range(int(parsed_command.group(1))):
            current_position = current_position.move(direction)

        if len(parsed_command.group(2)) > 0:
            rotation = Rotation.from_letter(parsed_command.group(2))

            direction = direction.rotate_with_rotation(rotation)
    
        #print(parsed_command.group(1), parsed_command.group(2))
        #print_tiles(tiles_strings, current_position, direction)
        #print(current_position.x, current_position.y, current_position.neighbours)
        #input()
        parsed_command = re.search(r"(\d+)([LR]{0,1})(.*)", parsed_command.group(3))

    direction_numbers = {
        Direction.UP: 3,
        Direction.RIGHT: 0,
        Direction.DOWN: 1,
        Direction.LEFT: 2
    }

    return 1000 * current_position.y + 4 * current_position.x + direction_numbers[direction]


class CubeSpace(Space):
    def __init__(
        self,
        x,
        y
    ):
        self.x = x
        self.y = y
        self.neighbours = {}

    def populate_neighbours(
        self,
        tiles,
        spaces
    ):
        side_length = 50
        other_side = {
            Direction.UP: {
                0: ((51, 50 + self.x), Direction.RIGHT), #1
                1: ((1, 100 + self.x), Direction.RIGHT), #2
                2: ((self.x - 100, 200), Direction.UP), #3
            },
            Direction.RIGHT: {
                0: ((100, 151 - self.y), Direction.LEFT), #4
                1: ((50 + self.y, 50), Direction.UP), #5
                2: ((150, 151 - self.y), Direction.LEFT), #4
                3: ((self.y - 100, 150), Direction.UP), #6
            },
            Direction.DOWN: {
                0: ((self.x + 100, 1), Direction.DOWN), #3
                1: ((50, self.x + 100), Direction.LEFT), #6
                2: ((100, self.x - 50), Direction.LEFT) #5
            },
            Direction.LEFT: {
                0: ((1, 151 - self.y), Direction.RIGHT), #7
                1: ((self.y - 50, 101), Direction.DOWN), #1
                2: ((51, 151 - self.y), Direction.RIGHT), #7
                3: ((self.y - 100, 1), Direction.DOWN), #2
            }
        }

        for direction in Direction:
            original_direction = direction
            coord = direction.move_forward_x_and_y(self.x, self.y)
            
            if tiles[coord[1]][coord[0]] == Tile.WRAP:
                if direction in (Direction.LEFT, Direction.RIGHT):
                    neighbour_index = (self.y - 1) // side_length
                else:
                    neighbour_index = (self.x - 1) // side_length

                coord, direction = other_side[direction][neighbour_index]

            if tiles[coord[1]][coord[0]] == Tile.SPACE:
                self.neighbours[original_direction] = (spaces[coord], direction)
            elif tiles[coord[1]][coord[0]] == Tile.WALL:
                self.neighbours[original_direction] = (self, original_direction)
            else:
                print(neighbour_index, other_side[original_direction][neighbour_index])
                print(self.x, self.y, original_direction, coord, direction)
                raise Exception    
            
def print_tiles_with_trail(tiles_strings, visited_positions):
    for y, row in enumerate(tiles_strings):
        row_string = ""
        for x, tile in enumerate(row):
            if (x, y) not in visited_positions:
                row_string += tile
            else:
                row_string += visited_positions[(x,y)].arrow_from_direction()
        print(row_string)

@register(22, 2022, 2, True)
def monkey_map_2(split_text):
    max_line_length = 0
    for line in split_text[:-2]:
        if len(line) > max_line_length:
            max_line_length = len(line)

    tiles = [[Tile.WRAP for x in range(max_line_length + 2)]]

    for line in split_text[:-2]:
        tiles.append([Tile.get_tile_from_text(tile) for tile in " " + line])

        wraps_to_add = max_line_length + 1 - len(line)
        for i in range(wraps_to_add):
            tiles[-1].append(Tile.WRAP)

    tiles.append([Tile.WRAP for x in range(max_line_length + 2)])

    tiles_strings = preprocess_print_tiles(tiles)
    spaces = {}

    current_position = None

    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if tile == Tile.SPACE:
                this_space = CubeSpace(x, y)
                spaces[(x, y)] = this_space

                if current_position is None:
                    current_position = this_space

    for space in spaces.values():
        space.populate_neighbours(tiles, spaces)

    direction = Direction.RIGHT

    parsed_command = re.search(r"(\d+)([LR]{0,1})(.*)", split_text[-1])

    #print_tiles_with_trail(tiles_strings, {(current_position.x, current_position.y): direction})
    while parsed_command is not None:
        start_point = (current_position.x, current_position.y)
        visited_tiles = {start_point: direction}
        gone_over_edge = False
        original_direction = direction
        for i in range(int(parsed_command.group(1))):
            current_position, direction = current_position.move(direction)
            visited_tiles[(current_position.x, current_position.y)] = direction
            if direction != original_direction:
                gone_over_edge = True

        if len(parsed_command.group(2)) > 0:
            rotation = Rotation.from_letter(parsed_command.group(2))

            direction = direction.rotate_with_rotation(rotation)
    
        #visited_tiles[(current_position.x, current_position.y)] = direction
        if gone_over_edge:
            pass
            #print(parsed_command.group(1), parsed_command.group(2))
            #print_tiles_with_trail(tiles_strings, visited_tiles)
            #print(start_point, original_direction)
            #print(current_position.x, current_position.y, current_position.neighbours)
            #input()
        parsed_command = re.search(r"(\d+)([LR]{0,1})(.*)", parsed_command.group(3))

    direction_numbers = {
        Direction.UP: 3,
        Direction.RIGHT: 0,
        Direction.DOWN: 1,
        Direction.LEFT: 2
    }

    return 1000 * current_position.y + 4 * current_position.x + direction_numbers[direction]