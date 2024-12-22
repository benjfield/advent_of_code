from advent.year_2024.day_22 import *

text_1 = '''1
10
100
2024'''

def test_next_secret_number():
    assert next_secret_number(123) == 15887950

def test_func_1():
    assert func_1(text_1) == 37327623
  
def test_func_2():
    text = '''1
2
3
2024'''
    assert func_2(text) == 23