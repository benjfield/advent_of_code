from advent.year_2022.day_17 import *

text = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''

def test_pyroclastic_flow_1():
    assert pyroclastic_flow_1(text) == 3068
    
def test_pyroclastic_flow_2():
    assert pyroclastic_flow_2(text) == 1514285714288