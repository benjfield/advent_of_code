from advent.year_2021.day_2 import *

def test_submarine_1():
    text = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''
    assert submarine_1(text) == 150