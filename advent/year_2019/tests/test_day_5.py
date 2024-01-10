from advent.year_2019.computer import *

def test_computer_process_immediate_1():
    computer = Computer("1002,4,3,4,33")
    computer.process()
    assert computer.state[4] == 99

def test_computer_output():
    computer = Computer("3,0,4,0,99")
    assert computer.process(7) == [7]

def test_computer_jump_1():
    computer = Computer("3,9,8,9,10,9,4,9,99,-1,8")
    assert computer.process(8) == [1]
    computer = Computer("3,9,8,9,10,9,4,9,99,-1,8")
    assert computer.process(7) == [0]

def test_computer_jump_2():
    computer = Computer("3,9,7,9,10,9,4,9,99,-1,8")
    assert computer.process(7) == [1]
    computer = Computer("3,9,7,9,10,9,4,9,99,-1,8")
    assert computer.process(8) == [0]

def test_computer_jump_3():
    computer = Computer("3,3,1108,-1,8,3,4,3,99")
    assert computer.process(8) == [1]
    computer = Computer("3,3,1108,-1,8,3,4,3,99")
    assert computer.process(7) == [0]

def test_computer_jump_4():
    computer = Computer("3,3,1107,-1,8,3,4,3,99")
    assert computer.process(7) == [1]
    computer = Computer("3,3,1107,-1,8,3,4,3,99")
    assert computer.process(8) == [0]
    
def test_computer_jump_5():
    computer = Computer("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
    assert computer.process(0) == [0]
    computer = Computer("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
    assert computer.process(1) == [1]
        
def test_computer_jump_6():
    computer = Computer("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
    assert computer.process(0) == [0]
    computer = Computer("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
    assert computer.process(1) == [1]
    
def test_computer_jump_7():
    computer = Computer("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
    assert computer.process(7) == [999]
    computer = Computer("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
    assert computer.process(8) == [1000]
    computer = Computer("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
    assert computer.process(9) == [1001]