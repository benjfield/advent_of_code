from advent.year_2020.day_8 import *


def test_handheld_halting_1():
    text = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split("\n")
    
    assert handheld_halting_1(text) == 5

def test_handheld_halting_2():
    text = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split("\n")
    
    assert handheld_halting_2(text) == 8