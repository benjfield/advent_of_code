from advent.year_2020.day_14 import *

def test_docking_data_1():
    text = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.split("\n")
    
    assert docking_data_1(text) == 165
    
def test_docking_data_2():
    text = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.split("\n")
    
    assert docking_data_2(text) == 208