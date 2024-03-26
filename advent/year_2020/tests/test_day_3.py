from advent.year_2020.day_3 import *

text = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split("\n")

def test_toboggan_1():
    assert toboggan_1(text) == 7
    
def test_toboggan_2():
    assert toboggan_2(text) == 336