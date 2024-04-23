from advent.year_2022.day_9 import *

text = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split("\n")

def test_rope_bridge_1():
    assert rope_bridge_1(text) == 13
    
def test_rope_bridge_2():
    assert rope_bridge_2(text) == 1
    
def test_rope_bridge_2_1():
    assert rope_bridge_2('''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''.split("\n")) == 36