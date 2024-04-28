from advent.year_2022.day_14 import *

text = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''.split("\n")

def test_regolith_reservoir_1():
    assert regolith_reservoir_1(text) == 24

def test_regolith_reservoir_2():
    assert regolith_reservoir_2(text) == 93