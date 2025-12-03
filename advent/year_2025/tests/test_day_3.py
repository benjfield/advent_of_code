from advent.year_2025.day_3 import *

text = '''987654321111111
811111111111119
234234234234278
818181911112111'''.split("\n")

def test_batteries_1():
    assert batteries_1(text) == 357

def test_batteries_2():
    assert batteries_2(text) == 3121910778619