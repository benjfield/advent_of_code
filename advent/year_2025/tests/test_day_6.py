from advent.year_2025.day_6 import *

text = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''.split("\n")

def test_trash_1():
    assert trash_1(text) == 4277556

def test_trash_2():
    assert trash_2(text) == 3263827