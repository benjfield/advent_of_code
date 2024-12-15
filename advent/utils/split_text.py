from enum import Enum, auto
from advent.utils.grid import Grid

class Split(Enum):
    NONE = auto()
    LINE = auto()
    INT_GRID = auto()
    CHAR_GRID = auto()

def split_text(text: str, split_type: Split, as_grid: bool = False):
    match split_type:
        case Split.NONE:
            return text
        case Split.LINE:
            return text.split("\n")
        case Split.INT_GRID:
            grid = create_int_grid(text)

            if as_grid:
                return Grid(grid)
            else:
                return grid
        case Split.CHAR_GRID:
            grid = create_char_grid(text)
            
            if as_grid:
                return Grid(grid)
            else:
                return grid
        case _:
            raise Exception("Invalid Enum")

def create_int_grid(text: str) -> list[list[int]]:
    return [
        [int(x) for x in line] for line in text.split("\n")
    ]

def create_char_grid(text: str) -> list[list[str]]:
    return [
        [x for x in line] for line in text.split("\n")
    ]