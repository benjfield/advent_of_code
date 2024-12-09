from advent.year_2024.day_3 import *


def test_mull_1():
    text = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

    assert mull_1(text) == 161

def test_mull_2():
    text = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
    
    assert mull_2(text) == 48