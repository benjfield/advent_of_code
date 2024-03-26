from advent.year_2020.day_5 import *

def test_binary_boarding_1():
    text = '''BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''.split("\n")

    assert binary_boarding_1(text) == 820