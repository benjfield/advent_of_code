from day21 import *

test_text=r"""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

def test_garden_1():
    assert garden_1(test_text, 6) == 16
    
def test_garden_2():
    assert garden_2(test_text, 6) == 16

def test_garden_2_2():
    assert garden_2(test_text, 10) == 50
    
def test_garden_2_3():
    assert garden_2(test_text, 50) == 1594