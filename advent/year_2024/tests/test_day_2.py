from advent.year_2024.day_2 import *

text = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''.split("\n")

def test_reports_1():
    assert reports_1(text) == 2

def test_reports_2():
    assert reports_2(text) == 4