import re
from advent.utils.direction import Direction
from advent.runner import register

class HorizontalWire:
    def __init__(self, vertical, horizontal_1, horizontal_2):
        self.vertical = vertical
        self.horizontal_start = min(horizontal_1, horizontal_2)
        self.horizontal_finish = max(horizontal_1, horizontal_2)

    def cross(self, vertical_wire):
        if (vertical_wire.horizontal >= self.horizontal_start and vertical_wire.horizontal <= self.horizontal_finish
            and self.vertical >= vertical_wire.vertical_start and self.vertical <= vertical_wire.vertical_finish):
            return True, self.vertical, vertical_wire.horizontal
        return False, 0, 0
    
    def __str__(self):
        return f"horizontal on {self.vertical}: {self.horizontal_start} to {self.horizontal_finish}"

class VerticalWire:
    def __init__(self, horizontal, vertical_1, vertical_2):
        self.horizontal = horizontal
        self.vertical_start = min(vertical_1, vertical_2)
        self.vertical_finish = max(vertical_1, vertical_2)

    def cross(self, horizontal_wire):
        if (horizontal_wire.vertical >= self.vertical_start and horizontal_wire.vertical <= self.vertical_finish
            and self.horizontal >= horizontal_wire.horizontal_start and self.horizontal <= horizontal_wire.horizontal_finish):
            return True, horizontal_wire.vertical, self.horizontal
        return False, 0, 0 

    def __str__(self):
        return f"vertical on {self.horizontal}: {self.vertical_start} to {self.vertical_finish}"
    
@register(3, 2019, 1)
def wires_1(text):
    wire_paths = []

    for instruction_set in text.split("\n"):
        wire_paths.append({
            "horizontal": [],
            "vertical": []
        }) 
        x = 0
        y = 0
        for instruction in instruction_set.split(","):
            parsed_instruction = re.match(r".*([RLDU])(.*)", instruction)

            direction = Direction.direction_from_letter(parsed_instruction.group(1))
            distance = int(parsed_instruction.group(2))

            start_x = x
            start_y = y
            x, y = direction.move_forward_x_and_y(start_x, start_y, distance)

            if direction.is_horizontal():
                wire_paths[-1]["horizontal"].append(HorizontalWire(y, start_x, x))
            else:
                wire_paths[-1]["vertical"].append(VerticalWire(x, start_y, y))

    crosses = []

    for wire in wire_paths[1]["horizontal"]:
        for wire_to_cross in wire_paths[0]["vertical"]:
            is_cross, cross_x, cross_y = wire_to_cross.cross(wire)            
            if is_cross:
                crosses.append({"x": cross_x, "y": cross_y})

    for wire in wire_paths[1]["vertical"]:
        for wire_to_cross in wire_paths[0]["horizontal"]:
            is_cross, cross_x, cross_y = wire_to_cross.cross(wire)            
            if is_cross:
                crosses.append({"x": cross_x, "y": cross_y})

    closest_distance = 1000000000
    for cross in crosses:
        distance = abs(cross["x"]) + abs(cross["y"])
        if distance < closest_distance and distance > 0:
            closest_distance = distance

    return closest_distance
        

@register(3, 2019, 2)
def wires_2(text):
    wire_paths = []

    for instruction_set in text.split("\n"):
        wire_paths.append({
            "horizontal": [],
            "vertical": []
        }) 
        x = 0
        y = 0
        for instruction in instruction_set.split(","):
            parsed_instruction = re.match(r".*([RLDU])(.*)", instruction)

            direction = Direction.direction_from_letter(parsed_instruction.group(1))
            distance = int(parsed_instruction.group(2))

            start_x = x
            start_y = y
            x, y = direction.move_forward_x_and_y(start_x, start_y, distance)

            if direction.is_horizontal():
                wire_paths[-1]["horizontal"].append(HorizontalWire(y, start_x, x))
            else:
                wire_paths[-1]["vertical"].append(VerticalWire(x, start_y, y))

    crosses = {}

    for wire in wire_paths[1]["horizontal"]:
        for wire_to_cross in wire_paths[0]["vertical"]:
            is_cross, cross_x, cross_y = wire_to_cross.cross(wire)            
            if is_cross:
                crosses[f"{cross_x}_{cross_y}"] = []

    for wire in wire_paths[1]["vertical"]:
        for wire_to_cross in wire_paths[0]["horizontal"]:
            is_cross, cross_x, cross_y = wire_to_cross.cross(wire)            
            if is_cross:
                crosses[f"{cross_x}_{cross_y}"] = []

    for instruction_set in text.split("\n"):
        wire_paths.append({
            "horizontal": [],
            "vertical": []
        }) 
        x = 0
        y = 0
        count = 0
        for instruction in instruction_set.split(","):
            parsed_instruction = re.match(r".*([RLDU])(.*)", instruction)

            direction = Direction.direction_from_letter(parsed_instruction.group(1))
            distance = int(parsed_instruction.group(2))

            for i in range(distance):
                x, y = direction.move_forward_x_and_y(x, y)
                count += 1

                square = f"{y}_{x}"
                if square in crosses:
                    crosses[square].append(count)

    smallest_distance_between_crosses = 1000000
    for cross_distance in crosses.values():
        distance = sum(cross_distance)
        if distance < smallest_distance_between_crosses and distance > 0:
            smallest_distance_between_crosses = distance

    return smallest_distance_between_crosses