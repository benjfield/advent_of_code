from enum import Enum, IntFlag, auto
from advent.utils.direction import Direction
from advent.runner import register

class Shape(Enum):
    HOR_LINE = 0
    CROSS = 1
    LSHAPE = 2
    VER_LINE = 3
    SQUARE = 4

    def get_initial_coordinates(self, max_y):
        match self:
            case self.HOR_LINE:
                return [
                    (2, -4),
                    (3, -4),
                    (4, -4),
                    (5, -4)
                ]
            case self.CROSS:
                return [
                    (3, -4),
                    (2, -3),
                    (3, -3),
                    (4, -3),
                    (3, -2)
                ]
            case self.LSHAPE:
                return [
                    (2, -4),
                    (3, -4),
                    (4, -4),
                    (4, -3),
                    (4, -2),
                ]
            case self.VER_LINE:
                return [
                    (2, -4),
                    (2, -3),
                    (2, -2),
                    (2, -1),
                ]
            case self.SQUARE:
                return [
                    (2, -4),
                    (3, -4),
                    (2, -3),
                    (3, -3),
                ]
            
def get_flow_directions(text):
    directions = []

    for char in text:
        directions.append(Direction.direction_from_arrow(char))
    
    return directions

class RockRow(IntFlag):
    COL0 = auto()
    COL1 = auto()
    COL2 = auto()
    COL3 = auto()
    COL4 = auto()
    COL5 = auto()
    COL6 = auto()

    def print_row(self):
        string_value = "|"
        for i in range(7):
            if RockRow(2 ** i) in self:
                string_value += "#"
            else:
                string_value += "."
        string_value += "|" 

        return string_value

class RockChannel:
    def __init__(
        self,
        text
    ):
        self.flow_directions = get_flow_directions(text) 
        self.max_y = 0
        self.rocks = [RockRow(0) for x in range(7)]

    def drop_rock(self, shape_count, flow_index):
        shape_coords = Shape(shape_count % 5).get_initial_coordinates(self.max_y)

        rock_finished = False
        while not rock_finished:
            flow_direction = self.flow_directions[flow_index % len(self.flow_directions)]
            new_shape_coords = [flow_direction.move_forward_x_and_y(coord[0], coord[1]) for coord in shape_coords]

            valid_move = True
            for new_shape_coord in new_shape_coords:
                if new_shape_coord[0] < 0 or new_shape_coord[0] > 6 or RockRow(2**new_shape_coord[0]) in self.rocks[new_shape_coord[1]]:
                    valid_move = False
                    break
                
            if valid_move:
                shape_coords = new_shape_coords

            new_shape_coords = [Direction.UP.move_forward_x_and_y(coord[0], coord[1]) for coord in shape_coords]

            valid_move = True
            for new_shape_coord in new_shape_coords:
                if abs(new_shape_coord[1]) > len(self.rocks) or RockRow(2**new_shape_coord[0]) in self.rocks[new_shape_coord[1]]:
                    valid_move = False
                    rock_finished = True
                    break

            if valid_move:
                shape_coords = new_shape_coords

            flow_index += 1

        for shape_coord in shape_coords:
            self.rocks[shape_coord[1]] = self.rocks[shape_coord[1]] | RockRow(2**shape_coord[0])

        top = shape_coords[-1][1]

        for i in range(top, top - 4, -1):
            if abs(i) > len(self.rocks):
                break
            elif int(self.rocks[i]) == 127:
                self.rocks = self.rocks[i + 1:]
                break

        if top > -8:
            for i in range(top, -8, -1):
                self.rocks.append(RockRow(0))
                self.max_y += 1
        
        return shape_count + 1, flow_index
    
    def rocks_as_tuple(self):
        return tuple([int(x) for x in self.rocks[-15:]])

@register(17, 2022, 1, False)
def pyroclastic_flow_1(text):
    shape_count = 0
    flow_index = 0
    rock_channel = RockChannel(text)
    while shape_count < 2022:
        shape_count, flow_index = rock_channel.drop_rock(shape_count, flow_index)
    return rock_channel.max_y

@register(17, 2022, 2, False)
def pyroclastic_flow_2(text):
    shape_count = 0
    flow_index = 0
    rock_channel = RockChannel(text)

    period_check = {
        (0, 0, rock_channel.rocks_as_tuple()): (0, 0)
    }

    while True:
        shape_count, flow_index = rock_channel.drop_rock(shape_count, flow_index)
        
        this_shape_count = shape_count % 5
        period_key = (this_shape_count, flow_index % len(rock_channel.flow_directions), rock_channel.rocks_as_tuple())

        if period_key in period_check:
            cycle_length = (shape_count - period_check[period_key][0])
            shapes_remaining_after_initial = (1000000000000 - period_check[period_key][0])
            number_of_cycles = shapes_remaining_after_initial // cycle_length - 1
            remaining_shapes = shapes_remaining_after_initial % cycle_length

            cycle_height = (rock_channel.max_y - period_check[period_key][1])

            height_from_cycles = number_of_cycles * cycle_height

            rock_channel.max_y += height_from_cycles
            for i in range(remaining_shapes):
                shape_count, flow_index = rock_channel.drop_rock(shape_count, flow_index)

            return rock_channel.max_y

        period_check[period_key] = (shape_count, rock_channel.max_y)