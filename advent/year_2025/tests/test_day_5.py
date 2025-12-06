from advent.year_2025.day_5 import *

text = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''.split("\n")

def test_fresh_1():
    assert fresh_1(text) == 3

def test_fresh_2():
    assert fresh_2(text) == 14