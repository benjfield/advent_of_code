from advent.year_2020.day_25 import *

def test_combo_breaker_1():
    text = '''5764801
17807724'''.split("\n")
    
    assert combo_breaker_1(text) == 14897079