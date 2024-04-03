from advent.year_2020.day_12 import *

def test_rain_risk_1():
    text = '''F10
N3
F7
R90
F11'''.split("\n")
    
    assert rain_risk_1(text) == 25
    
def test_rain_risk_2():
    text = '''F10
N3
F7
R90
F11'''.split("\n")
    
    assert rain_risk_2(text) == 286