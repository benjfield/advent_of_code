from advent.year_2024.day_7 import *

text = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''.split("\n")

def test_func_1():
    assert func_1(text) == 3749

def test_func_2():
    assert func_2(text) == 11387

def test_func_2_2():
    assert func_2_2(text) == 11387