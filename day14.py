from aocd import get_data
import re
import copy

def tilt_east(rock_beams):
    positions = []
    for i in range(len(rock_beams)):
        first_hash = len(rock_beams[0])
        round_count = 0
        for j in reversed(range(len(rock_beams[0]))):
            if rock_beams[i][j] == "#":
                first_hash = j
                round_count = 0
            elif rock_beams[i][j] == "O":
                round_count += 1
                rock_beams[i][j] = "."
                rock_beams[i][first_hash - round_count] = "O"

                positions.append(len(rock_beams[0])*i + (first_hash - round_count) + 1)
                
    return tuple(positions)

def tilt_west(rock_beams):
    for i in range(len(rock_beams)):
        first_hash = -1
        round_count = 0
        for j in range(len(rock_beams[0])):
            if rock_beams[i][j] == "#":
                first_hash = j
                round_count = 0
            elif rock_beams[i][j] == "O":
                round_count += 1
                rock_beams[i][j] = "."
                rock_beams[i][first_hash + round_count] = "O"
                
def tilt_south(rock_beams):
    for i in range(len(rock_beams[0])):
        first_hash = len(rock_beams)
        round_count = 0
        for j in reversed(range(len(rock_beams))):
            if rock_beams[j][i] == "#":
                first_hash = j
                round_count = 0
            elif rock_beams[j][i] == "O":
                round_count += 1
                rock_beams[j][i] = "."
                rock_beams[first_hash - round_count][i] = "O"

def tilt_north(rock_beams):
    for i in range(len(rock_beams[0])):
        first_hash = -1
        round_count = 0
        for j in range(len(rock_beams)):
            if rock_beams[j][i] == "#":
                first_hash = j
                round_count = 0
            elif rock_beams[j][i] == "O":
                round_count += 1
                rock_beams[j][i] = "."
                rock_beams[first_hash + round_count][i] = "O"

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

def calculate_position_check(rock_beams):
    positions = []
    for beam_number, beam in enumerate(rock_beams):
        for column_number, rock_char in enumerate(beam):
            if rock_char == "O":
                positions.append(len(rock_beams[0])*beam_number + column_number + 1)
    return tuple(positions)

def rocks_1(text):
    rock_beams = []
    for i, line in enumerate(text.split("\n")):
        beam = []
        for j, char in enumerate(line):
            beam.append(char)
        rock_beams.append(beam)

    tilt_north(rock_beams)

    return calculate_load(rock_beams)

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

rocks_text = get_data(day=14, year=2023)
print(rocks_2(rocks_text))