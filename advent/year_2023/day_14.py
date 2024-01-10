import re
import copy
from advent.runner import register

def tilt_east(rock_beams):
    positions = []
    for i in range(len(rock_beams)):
        next_o = len(rock_beams[0])
        for j in reversed(range(len(rock_beams[0]))):
            if rock_beams[i][j] == "#":
                next_o = j
            elif rock_beams[i][j] == "O":
                next_o -= 1
                rock_beams[i][j] = "."
                rock_beams[i][next_o] = "O"

                positions.append(len(rock_beams[0])*i + next_o)

    return tuple(positions)

def tilt_west(rock_beams):
    for i in range(len(rock_beams)):
        next_o = -1
        for j in range(len(rock_beams[0])):
            if rock_beams[i][j] == "#":
                next_o = j
            elif rock_beams[i][j] == "O":
                next_o += 1
                rock_beams[i][j] = "."
                rock_beams[i][next_o] = "O"
                
def tilt_south(rock_beams):
    for i in range(len(rock_beams[0])):
        next_o = len(rock_beams)
        for j in reversed(range(len(rock_beams))):
            if rock_beams[j][i] == "#":
                next_o = j
            elif rock_beams[j][i] == "O":
                next_o -= 1
                rock_beams[j][i] = "."
                rock_beams[next_o][i] = "O"

def tilt_north(rock_beams):
    for i in range(len(rock_beams[0])):
        next_o = -1
        for j in range(len(rock_beams)):
            if rock_beams[j][i] == "#":
                next_o = j
            elif rock_beams[j][i] == "O":
                next_o += 1
                rock_beams[j][i] = "."
                rock_beams[next_o][i] = "O"

def spin_cycle(rock_beams):
    tilt_north(rock_beams)
    tilt_west(rock_beams)
    tilt_south(rock_beams)
    return tilt_east(rock_beams)

def calculate_load(rock_beams):
    total_load = 0
    for beam_number, beam in enumerate(rock_beams):
        for rock_char in beam:
            if rock_char == "O":
                total_load += (len(beam) - beam_number)
    return total_load

@register(14, 2023, 1)
def rocks_1(text):
    rock_beams = []
    for i, line in enumerate(text.split("\n")):
        beam = []
        for j, char in enumerate(line):
            beam.append(char)
        rock_beams.append(beam)

    tilt_north(rock_beams)

    return calculate_load(rock_beams)

@register(14, 2023, 2)
def rocks_2(text):
    rock_beams = []
    for i, line in enumerate(text.split("\n")):
        beam = []
        for j, char in enumerate(line):
            beam.append(char)
        rock_beams.append(beam)

    previous_positions = {}

    total = 1000000000

    for i in range(0, total):
        position = spin_cycle(rock_beams)
        if position not in previous_positions:
            previous_positions[position] = i
        else:
            period = i - previous_positions[position]

            number_to_run = (total - (i+1))%period 

            previous_positions[position] = i
            break
            
    for i in range(number_to_run):
        spin_cycle(rock_beams)

    return calculate_load(rock_beams)