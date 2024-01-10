from advent.year_2023.day_14 import *

test_text="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""    

def test_rocks_1():
    assert rocks_1(test_text) == 136
    
def test_rocks_2():
    assert rocks_2(test_text) == 64
