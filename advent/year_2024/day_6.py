from advent.runner import register
from dataclasses import dataclass
from advent.utils.direction import Direction, Rotation
from copy import deepcopy

@dataclass
class Guard:
    direction: Direction
    x: int
    y: int

    def move(self, map, debug=False):
        new_x, new_y = self.direction.move_forward(self.x, self.y)

        if new_x < 0 or new_y < 0:
            raise IndexError

        if map[new_y][new_x] == ".":
            self.x = new_x
            self.y = new_y
            return
        else:
            if debug:
                print(self.x, self.y, self.direction)
            self.direction = self.direction.rotate_with_rotation(Rotation.CLOCKWISE)
            if debug:
                print(self.x, self.y, self.direction)

@register(6, 2024, 1, True)
def guard_1(text):
    grid = []
    visited = {}
    guard = None
    for y, line in enumerate(text):
        grid.append([])
        for x, char in enumerate(line):
            if char == "^":
                guard = Guard(
                    Direction.UP,
                    x,
                    y,
                )
                grid[-1].append(".")
                visited = {(x, y)}
            else:
                grid[-1].append(char)

    while True:
        try:
            guard.move(grid)

            coords = (guard.x, guard.y)
            visited.add(coords)
        except:
            break

    return len(visited)

@register(6, 2024, 2, True)
def guard_2(text):
    grid = []
    guard = None

    for y, line in enumerate(text):
        grid.append([])
        for x, char in enumerate(line):
            if char == "^":
                start_x = x
                start_y = y
                grid[-1].append(".")
            else:
                grid[-1].append(char)

    guard = Guard(
        Direction.UP,
        start_x,
        start_y,
    )

    visited = {(guard.x, guard.y)}
    while True:
        try:
            guard.move(grid)

            coords = (guard.x, guard.y)
            visited.add(coords)
        except:
            break

    paradoxes = set()
    for change_x, change_y in visited:
        if (change_x != start_x or change_y != start_y):
            debug = False

            guard.direction = Direction.UP
            guard.x = start_x
            guard.y = start_y

            grid[change_y][change_x] = "@"

            if debug:
                debug_grid = deepcopy(grid)

            visited = {(guard.x, guard.y, guard.direction)}
            while True:
                try:
                    guard.move(grid, debug)
                    
                    coords = (guard.x, guard.y, guard.direction)

                    if debug:
                        if debug_grid[guard.y][guard.x] == ".":
                            debug_grid[guard.y][guard.x] = guard.direction.arrow_from_direction()
                        else:
                            debug_grid[guard.y][guard.x] = "+"

                    if coords in visited:
                        paradoxes.add((change_x, change_y))
                        break
                    else:
                        visited.add(coords)
                except IndexError:
                    break
            
            if debug:
                for line in debug_grid:
                    print("".join(line))

            grid[change_y][change_x] = "."

    return len(paradoxes)
