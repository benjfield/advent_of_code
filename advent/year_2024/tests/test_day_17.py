from advent.year_2024.day_17 import *

text_1 = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''

def test_func_1():
    assert func_1(text_1) == "4,6,3,5,6,3,5,2,1,0"

def test_computer_1():
    computer = Computer(0, 0, 9, [])
    computer.run([2, 6])
    assert computer.b == 1

def test_computer_2():
    computer = Computer(10, 0, 0, [])
    output = computer.run([5, 0, 5, 1, 5, 4])
    assert output == [0, 1, 2]

def test_computer_3():
    computer = Computer(2024, 0, 0, [])
    output = computer.run([0, 1, 5, 4, 3, 0])
    assert output == [4,2,5,6,7,7,7,7,3,1,0]
    assert computer.a == 0

def test_computer_4():
    computer = Computer(0, 29, 0, [])
    output = computer.run([1, 7])
    assert computer.b == 26

def test_computer_5():
    computer = Computer(0, 2024, 43690, [])
    output = computer.run([4, 0])
    assert computer.b == 44354

def test_func_2():
    text = '''Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0'''

    assert func_2(text) == 117440