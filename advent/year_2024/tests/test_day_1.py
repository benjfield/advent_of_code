from advent.year_2024.day_1 import *

text = '''3   4
4   3
2   5
1   3
3   9
3   3'''.split("\n")

def test_hysteria_1():
    assert hysteria_1(text) == 11

def test_hysteria_2():
    assert hysteria_2(text) == 31