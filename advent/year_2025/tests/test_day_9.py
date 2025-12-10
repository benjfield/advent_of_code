from advent.year_2025.day_9 import *

text = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''.split("\n")

def test_size_1():
    assert size_1(text) == 50

def test_size_2():
    assert size_2(text) == 24