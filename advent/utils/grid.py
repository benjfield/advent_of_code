from dataclasses import dataclass
from typing import Callable

@dataclass
class Grid:
    grid: list[list]

    def check_inbounds(self, coords: tuple[int, int]) -> bool:
        return self.check_inbounds_from_x_and_y(*coords)

    def check_inbounds_from_x_and_y(self, x: int, y: int) -> bool:
        return x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid)

    def get(self, coords: tuple[int, int]):
        return self.get_from_x_and_y(*coords)

    def get_from_x_and_y(self, x: int, y: int):
        return self.grid[y][x]
    
    def set(self, coords: tuple[int, int], value):
        self.set_from_x_and_y(*coords, value)

    def set_from_x_and_y(self, x: int, y: int, value):
        self.grid[y][x] = value

    def print(self, override_function: Callable[[str, int, int], str] = None):
        for y, line in enumerate(self.grid):
            if override_function is None:
                print("".join(line))
            else:
                text = [override_function(char, x, y) for x, char in enumerate(line)]
                print("".join(text))

    def score(self, score_function: Callable[[str, int, int], int]):
        score = 0
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                score += score_function(char, x, y)
        return score

def check_inbounds(grid, x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)