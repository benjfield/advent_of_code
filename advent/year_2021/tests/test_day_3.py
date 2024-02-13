from advent.year_2021.day_3 import *

def test_binary_power_1():
    text = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
    assert binary_power_1(text) == 198
    
def test_binary_power_2():
    text = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
    assert binary_power_2(text) == 230