from advent.year_2023.day_21 import *

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