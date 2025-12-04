from advent.year_2025.day_4 import *

text = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

def test_forklift_1():
    assert forklift_1(text) == 13

def test_forklift_2():
    assert forklift_2(text) == 43