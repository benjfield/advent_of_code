from advent.year_2024.day_11 import *

text = '''125 17'''

def test_func_1():
    assert func_1(text) == 55312

def test_split_int():
    for number, answer in [
        (1, [1]),
        (10, [1, 0]),
        (100, [100]),
        (1000, [10, 0]),
        (10000, [10000]),
        (100000, [100, 0]),
    ]:
        assert split_int(number) == answer