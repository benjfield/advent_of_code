from advent.year_2020.day_6 import *

text = '''abc

a
b
c

ab
ac

a
a
a
a

b'''.split("\n")

def test_custom_customs_1():
    assert custom_customs_1(text) == 11
    
def test_custom_customs_2():
    assert custom_customs_2(text) == 6