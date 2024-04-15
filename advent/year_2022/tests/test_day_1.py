from advent.year_2022.day_1 import *

text = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''.split("\n")

def test_calorie_count_1():
    assert calorie_count_1(text) == 24000

def test_calorie_count_2():
    assert calorie_count_2(text) == 45000