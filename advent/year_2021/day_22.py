from advent.runner import register
import re

class Cube:
    def __init__(
        self,
        x_min,
        x_max,
        y_min,
        y_max,
        z_min,
        z_max,
        on = True
        ):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max
        self.on = on

    def __str__(self):
        return f"{self.on}, x_min={self.x_min}, x_max={self.x_max}, y_min={self.y_min}, y_max={self.y_max}, z_min={self.z_min}, z_max={self.z_max}"

    def limited_size(self):
        space_to_check_x_min = max(self.x_min, -50)
        space_to_check_x_max = min(self.x_max, 50)
        space_to_check_y_min = max(self.y_min, -50)
        space_to_check_y_max = min(self.y_max, 50)
        space_to_check_z_min = max(self.z_min, -50)
        space_to_check_z_max = min(self.z_max, 50)

        if space_to_check_x_min > space_to_check_x_max or space_to_check_y_min > space_to_check_y_max or space_to_check_z_min > space_to_check_z_max:
            return 0
        else:
            return (space_to_check_x_max - space_to_check_x_min + 1) * (space_to_check_y_max - space_to_check_y_min + 1) * (space_to_check_z_max - space_to_check_z_min + 1)

    def size(self):
            return (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1) * (self.z_max - self.z_min + 1)

    def remove_collision_space(
        self,
        collision_space_x_min,
        collision_space_x_max,
        collision_space_y_min,
        collision_space_y_max,
        collision_space_z_min,
        collision_space_z_max
        ):
        cubes = []
        if self.x_min < collision_space_x_min:
            cubes.append(Cube(
                self.x_min,
                collision_space_x_min - 1,
                self.y_min,
                self.y_max,
                self.z_min,
                self.z_max,
                self.on
            ))
        if self.x_max > collision_space_x_max:
            cubes.append(Cube(
                collision_space_x_max + 1,
                self.x_max,
                self.y_min,
                self.y_max,
                self.z_min,
                self.z_max,
                self.on
            ))
        if self.y_min < collision_space_y_min:
            cubes.append(Cube(
                collision_space_x_min,
                collision_space_x_max,
                self.y_min,
                collision_space_y_min - 1,
                self.z_min,
                self.z_max,
                self.on
            ))
        if self.y_max > collision_space_y_max:
            cubes.append(Cube(
                collision_space_x_min,
                collision_space_x_max,
                collision_space_y_max + 1,
                self.y_max,
                self.z_min,
                self.z_max,
                self.on
            ))
        if self.z_min < collision_space_z_min:
            cubes.append(Cube(
                collision_space_x_min,
                collision_space_x_max,
                collision_space_y_min,
                collision_space_y_max,
                self.z_min,
                collision_space_z_min - 1,
                self.on
            ))
        if self.z_max > collision_space_z_max:
            cubes.append(Cube(
                collision_space_x_min,
                collision_space_x_max,
                collision_space_y_min,
                collision_space_y_max,
                collision_space_z_max + 1,
                self.z_max,
                self.on
            ))
        
        return cubes

def find_collision(cube_1, cube_2):
    collision_space_x_min = max(cube_1.x_min, cube_2.x_min)
    collision_space_x_max = min(cube_1.x_max, cube_2.x_max)
    collision_space_y_min = max(cube_1.y_min, cube_2.y_min)
    collision_space_y_max = min(cube_1.y_max, cube_2.y_max)
    collision_space_z_min = max(cube_1.z_min, cube_2.z_min)
    collision_space_z_max = min(cube_1.z_max, cube_2.z_max)

    if collision_space_x_min > collision_space_x_max or collision_space_y_min > collision_space_y_max or collision_space_z_min > collision_space_z_max:
        return [cube_1], [cube_2]
    else:
        if cube_2.on:
            return [cube_1], cube_2.remove_collision_space(
                collision_space_x_min,
                collision_space_x_max,
                collision_space_y_min,
                collision_space_y_max,
                collision_space_z_min,
                collision_space_z_max
            )
        else:
            return cube_1.remove_collision_space(
                collision_space_x_min,
                collision_space_x_max,
                collision_space_y_min,
                collision_space_y_max,
                collision_space_z_min,
                collision_space_z_max
            ), [cube_2]

@register(22, 2021, 1)
def cubes_1(text):
    split_text = text.split("\n")
    paresed_cubes = []

    for line in split_text:
        parsed_text = re.match(r"(\w+) x=(-{0,1}\d+)\.\.(-{0,1}\d+),y=(-{0,1}\d+)\.\.(-{0,1}\d+),z=(-{0,1}\d+)\.\.(-{0,1}\d+)", line)

        if parsed_text.group(1) == "on":
            cube_on = True
        elif parsed_text.group(1) == "off":
            cube_on = False
        else:
            raise Exception("Parse error")
        
        paresed_cubes.append(Cube(
            int(parsed_text.group(2)),
            int(parsed_text.group(3)),
            int(parsed_text.group(4)),
            int(parsed_text.group(5)),
            int(parsed_text.group(6)),
            int(parsed_text.group(7)),
            cube_on
        ))

    on_cubes = []

    for parsed_cube in paresed_cubes:
        if parsed_cube.on:
            cubes_to_check = [parsed_cube]
            for on_cube in on_cubes:
                next_cubes_to_check = []
                for cube_to_check in cubes_to_check:
                    _, these_cubes_to_check = find_collision(on_cube, cube_to_check)
                    next_cubes_to_check += these_cubes_to_check
                cubes_to_check = next_cubes_to_check
            on_cubes += cubes_to_check
        else:
            next_on_cubes = []
            for on_cube in on_cubes:
                these_on_cubes, _ = find_collision(on_cube, parsed_cube)
                next_on_cubes += these_on_cubes
            on_cubes = next_on_cubes

    cubes = 0

    for cube in on_cubes:
        cubes += cube.limited_size()

    return cubes

@register(22, 2021, 2)
def cubes_2(text):
    split_text = text.split("\n")
    paresed_cubes = []

    for line in split_text:
        parsed_text = re.match(r"(\w+) x=(-{0,1}\d+)\.\.(-{0,1}\d+),y=(-{0,1}\d+)\.\.(-{0,1}\d+),z=(-{0,1}\d+)\.\.(-{0,1}\d+)", line)

        if parsed_text.group(1) == "on":
            cube_on = True
        elif parsed_text.group(1) == "off":
            cube_on = False
        else:
            raise Exception("Parse error")
        
        paresed_cubes.append(Cube(
            int(parsed_text.group(2)),
            int(parsed_text.group(3)),
            int(parsed_text.group(4)),
            int(parsed_text.group(5)),
            int(parsed_text.group(6)),
            int(parsed_text.group(7)),
            cube_on
        ))

    on_cubes = []

    for parsed_cube in paresed_cubes:
        if parsed_cube.on:
            cubes_to_check = [parsed_cube]
            for on_cube in on_cubes:
                next_cubes_to_check = []
                for cube_to_check in cubes_to_check:
                    _, these_cubes_to_check = find_collision(on_cube, cube_to_check)
                    next_cubes_to_check += these_cubes_to_check
                cubes_to_check = next_cubes_to_check
            on_cubes += cubes_to_check
        else:
            next_on_cubes = []
            for on_cube in on_cubes:
                these_on_cubes, _ = find_collision(on_cube, parsed_cube)
                next_on_cubes += these_on_cubes
            on_cubes = next_on_cubes

    cubes = 0

    for cube in on_cubes:
        cubes += cube.size()

    return cubes