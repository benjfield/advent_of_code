from advent.year_2019.day_2 import *

def test_computer_process_1():
    computer = computer_from_string("1,0,0,0,99")
    computer.process_without_input()
    assert computer.state[0] == 2
    
def test_computer_process_2():
    computer = computer_from_string("2,3,0,3,99")
    computer.process_without_input()
    assert computer.state[3] == 6

def test_computer_process_3():
    computer = computer_from_string("2,4,4,5,99,0")
    computer.process_without_input()
    assert computer.state[5] == 9801

def test_computer_process_4():
    computer = computer_from_string("1,1,1,4,99,5,6,0,99")
    computer.process_without_input()
    assert computer.state[0] == 30