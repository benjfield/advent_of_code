from typing import Self
from advent.runner import register
from advent.utils.split_text import create_char_grid
from advent.utils.grid import Grid
from dataclasses import dataclass
from functools import cache
from collections import defaultdict
from sortedcontainers import SortedDict
from enum import Enum, auto

@dataclass
class Coord:
    x: int
    y: int

    @classmethod
    def from_coord_string(cls: Self, coord_string: str) -> Self:
        coords = coord_string.split(",")
        return cls(
            x=int(coords[0]),
            y=int(coords[1]),
        )

    def rectangle_size(self: Self, other: Self) -> int:
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)
    
class LineDirection(Enum):
    VERTICAL = auto()
    HORIZONTAL = auto()

@dataclass
class Line:
    start: Coord
    end: Coord

    @property
    def direction(self: Self):
        if self.start.x == self.end.x:
            return LineDirection.VERTICAL
        else:
            return LineDirection.HORIZONTAL
        
    @property
    def top(self: Self):
        return max(self.start.y, self.end.y)

    @property
    def bottom(self: Self):
        return min(self.start.y, self.end.y)
    
    @property
    def right(self: Self):
        return max(self.start.x, self.end.x)
    
    @property
    def left(self: Self):
        return min(self.start.x, self.end.x)
    
    @property
    def perpendicular(self: Self):
        if self.direction == LineDirection.VERTICAL:
            y = (self.top - self.bottom) // 2 + self.bottom

            return Line(
                Coord(-1, y),
                Coord(self.start.x, y)
            )
        else:
            x = (self.right - self.left) // 2 + self.left

            return Line(
                Coord(x, -1),
                Coord(x, self.start.y)
            )
    
    def crosses(self: Self, other: Self, crosses_if_superset = False) -> bool:
        if self.direction == other.direction:
            if not crosses_if_superset:
                return False
            else:
                if self.direction == LineDirection.VERTICAL:
                    return (
                        self.start.x == other.start.x and
                        other.bottom < self.bottom and
                        self.top < other.top
                    )
                else:
                    return (
                        self.start.y == other.start.y and
                        other.left < self.left and
                        self.right < other.right
                    )

        if self.direction == LineDirection.VERTICAL:
            return (
                self.top > other.start.y > self.bottom and
                other.right > self.start.x > other.left
            )
        else:
            return (
                self.right > other.start.x > self.left and
                other.top > self.start.y > other.bottom
            )
        
    def trimmed(self: Self, other: Self) -> int:
        if self.direction != other.direction:
            return [other]

        if self.direction == LineDirection.VERTICAL:
            if self.start.x != other.start.x:
                return [other]
            
            lines = []
            if other.top > self.top >= other.bottom:
                lines.append(
                    Line(
                        Coord(self.start.x, self.top + 1),
                        Coord(self.start.x, other.top),
                    )
                )

            if other.bottom < self.bottom <= other.top:
                lines.append(
                    Line(
                        Coord(self.start.x, other.bottom),
                        Coord(self.start.x, self.bottom - 1),
                    )
                )

            return lines
        else:
            if self.start.y != other.start.y:
                return [other]
            
            lines = []
            if other.right > self.right >= other.left:
                lines.append(
                    Line(
                        Coord(self.right + 1, self.start.y),
                        Coord(other.right, self.start.y),
                    )
                )

            if other.left < self.left <= other.right:
                lines.append(
                    Line(
                        Coord(other.left, self.start.y),
                        Coord(self.left - 1, self.start.y),
                    )
                )

            return lines
        
class InvalidRectangle(Exception):
    pass

@register(9, 2025, 1, True)
def size_1(text):
    coords = [Coord.from_coord_string(line) for line in text]

    max_size = 0

    for i, coord1 in enumerate(coords[:-1]):
        for coord2 in coords[i+1:]:
            max_size = max(max_size, coord1.rectangle_size(coord2))

    return max_size
          
@register(9, 2025, 2, True)
def size_2(text):
    coords = [Coord.from_coord_string(line) for line in text]

    shape_lines = []
    for i in range(len(coords)):
        shape_lines.append(
            Line(
                coords[i-1],
                coords[i],
            ),
        )

    max_size = 0

    for i, coord1 in enumerate(coords[:-1]):
        for coord2 in coords[i+1:]:
            corner_1 = Coord(coord1.x, coord2.y)
            corner_2 = Coord(coord2.x, coord1.y)
            valid_rectangle = True
            try:
                for rectange_line in [
                    Line(coord1, corner_1),
                    Line(corner_1, coord2),
                    Line(coord2, corner_2),
                    Line(corner_2, coord1),
                ]:
                    lines = [rectange_line]
                    for shape_line in shape_lines:
                        next_lines = []
                        for line in lines:
                            next_lines += shape_line.trimmed(line) 
                        lines = next_lines
                    

                    for line in lines:
                        for shape_line in shape_lines:
                            if shape_line.crosses(line):
                                raise InvalidRectangle
                            
                        perpendicular = line.perpendicular

                        crosses = 0
                        for shape_line in shape_lines:
                            if shape_line.crosses(perpendicular, True):
                                crosses += 1

                        if crosses %2 != 1:
                            raise InvalidRectangle                  

            except InvalidRectangle:
                valid_rectangle = False

            if valid_rectangle:
                max_size = max(max_size, coord1.rectangle_size(coord2))

    return max_size