from advent.year_2025.day_1 import *

text = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''.split("\n")

def test_safe_lock_1():
    assert safe_lock_1(text) == 3

def test_safe_lock_2():
    assert safe_lock_2(text) == 6