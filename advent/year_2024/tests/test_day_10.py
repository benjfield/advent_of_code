from advent.year_2024.day_10 import *

text = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''.split("\n")

def test_func_1():
    assert func_1(text) == 36

def test_func_2():
    assert func_2(text) == 81
