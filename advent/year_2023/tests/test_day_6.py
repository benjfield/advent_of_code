from advent.year_2023.day_6 import *

test_text="""Time:      7  15   30
Distance:  9  40  200"""

def test_boat_1():
    assert boat_1(test_text) == 288

def test_boat_2():
    assert boat_2(test_text) == 71503