from advent.year_2019.day_19 import *
from advent.year_2019.computer import computer_from_string

text = '''109,424,203,1,21102,11,1,0,1105,1,282,21101,18,0,0,1106,0,259,2101,0,1,221,203,1,21101,0,31,0,1105,1,282,21101,0,38,0,1106,0,259,21001,23,0,2,21202,1,1,3,21102,1,1,1,21102,57,1,0,1105,1,303,2101,0,1,222,21002,221,1,3,20101,0,221,2,21101,259,0,1,21101,0,80,0,1105,1,225,21102,198,1,2,21102,91,1,0,1106,0,303,1201,1,0,223,21002,222,1,4,21101,0,259,3,21102,225,1,2,21102,225,1,1,21102,1,118,0,1106,0,225,21001,222,0,3,21101,0,140,2,21101,133,0,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1106,0,259,2101,0,1,223,21002,221,1,4,21002,222,1,3,21101,0,24,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,108,20207,1,223,2,21001,23,0,1,21102,1,-1,3,21102,1,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1201,-4,0,249,21202,-3,1,1,22101,0,-2,2,21202,-1,1,3,21102,1,250,0,1105,1,225,22101,0,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21101,0,343,0,1105,1,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21102,1,384,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0'''

def test_lower_edge_1():
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)
    coordinates[1] = 90
    lower_edge = find_lower_edge_on_row(computer, coordinates, 70,  80)
    assert lower_edge == 71

def test_higher_edge_1():
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)
    coordinates[1] = 90
    higher_edge = find_higher_edge_on_row(computer, coordinates, 80,  90)
    assert higher_edge == 81

def test_higher_edge_2():
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)
    coordinates[1] = 100
    higher_edge = find_higher_edge_on_row(computer, coordinates, 81,  140)
    assert higher_edge == 90

def test_find_width_in_row_1():
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)
    lower_edge, higher_edge = find_edges_in_row(computer, 90, coordinates)
    assert lower_edge == 71
    assert higher_edge == 81

def test_find_width_in_row_2():
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)
    lower_edge, higher_edge = find_edges_in_row(computer, 100, coordinates)
    assert lower_edge == 79
    assert higher_edge == 90

def test_find_width_in_row_3():
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)
    lower_edge, higher_edge = find_edges_in_row(computer, 140, coordinates)
    assert lower_edge == 110
    assert higher_edge == 126

def test_bottom_edge_1():
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)
    coordinates[0] = 117
    higher_edge = find_bottom_edge_on_column(computer, coordinates, 140,  160)
    assert higher_edge == 149

def test_find_height_at_width():
    computer = computer_from_string(text)
    coordinates = np.zeros(2, dtype=np.int32)
    bottom_edge = find_bottom_edge_at_width(computer, coordinates, 140, 10)
    assert bottom_edge == 149