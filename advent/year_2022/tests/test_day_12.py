from advent.year_2022.day_12 import *

text = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''.split("\n")

def test_hill_climbing_1():
    assert hill_climbing_1(text) == 31