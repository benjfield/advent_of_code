from advent.year_2019.computer import *

def test_computer_process_immediate_1():
    computer = computer_from_string("1002,4,3,4,33")
    computer.process_without_input()
    assert computer.state[4] == 99

def test_computer_output():
    computer = computer_from_string("3,0,4,0,99")
    assert process(computer, [7]) == (True, [7])

def test_computer_jump_1():
    computer = computer_from_string("3,9,8,9,10,9,4,9,99,-1,8")
    assert process(computer, [8]) == (True, [1])
    computer.reset()
    assert process(computer, [7]) == (True, [0])

def test_computer_jump_2():
    computer = computer_from_string("3,9,7,9,10,9,4,9,99,-1,8")
    assert process(computer, [7]) == (True, [1])
    computer.reset()
    assert process(computer, [8]) == (True, [0])

def test_computer_jump_3():
    computer = computer_from_string("3,3,1108,-1,8,3,4,3,99")
    assert process(computer, [8]) == (True, [1])
    computer.reset()
    assert process(computer, [7]) == (True, [0])

def test_computer_jump_4():
    computer = computer_from_string("3,3,1107,-1,8,3,4,3,99")
    assert process(computer, [7]) == (True, [1])
    computer.reset()
    assert process(computer, [8]) == (True, [0])
    
def test_computer_jump_5():
    computer = computer_from_string("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
    assert process(computer, [0]) == (True, [0])
    computer.reset()
    assert process(computer, [1]) == (True, [1])
        
def test_computer_jump_6():
    computer = computer_from_string("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
    assert process(computer, [0]) == (True, [0])
    computer.reset()
    assert process(computer, [1]) == (True, [1])
    
def test_computer_jump_7():
    computer = computer_from_string("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
    assert process(computer, [7]) == (True, [999])
    computer.reset()
    assert process(computer, [8]) == (True, [1000])
    computer.reset()
    assert process(computer, [9]) == (True, [1001])