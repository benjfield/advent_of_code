from advent.year_2021.day_17 import *

def test_trick_shot_1():
    text = '''target area: x=20..30, y=-10..-5'''

    assert trick_shot_1(text) == 9
    
def test_trick_shot_2():
    text = '''target area: x=20..30, y=-10..-5'''

    assert trick_shot_2(text) == 112