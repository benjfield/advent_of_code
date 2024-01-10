from advent.year_2023.day_20 import *

test_text=r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

test_text_2=r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

def test_pulse_1():
    assert pulse_1(test_text) == 32000000
    
def test_pulse_1_2():
    assert pulse_1(test_text_2) == 11687500