from advent.year_2024.day_6 import *

text = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''.split("\n")

def test_guard_1():
    assert guard_1(text) == 41

def test_guard_2():
    assert guard_2(text) == 6