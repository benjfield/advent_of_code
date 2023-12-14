from aocd import get_data
import re
import copy

def move_rocks_west(beam, start, finish, round_count):
    for index in range(start, finish):
        if index < start + round_count:
            beam[index] = "O"
        else:
            beam[index] = "."

def move_rocks_east(beam, start, finish, round_count):
    for index in range(start, finish):
        if index >= finish - round_count:
            beam[index] = "O"
        else:
            beam[index] = "."


def tilt_horizontal(rock_beams, east=True):
    for i, beam in enumerate(rock_beams):
        first_hash = 0
        round_count = 0
        for j, rock_char in enumerate(beam):
            if rock_char == "#":
                if east:
                    move_rocks_east(beam, first_hash, j, round_count)
                else:
                    move_rocks_west(beam, first_hash, j, round_count)

                first_hash = j + 1
                round_count = 0
            elif rock_char == "O":
                round_count += 1

        if east:
            move_rocks_east(beam, first_hash, len(beam), round_count)
        else:
            move_rocks_west(beam, first_hash, len(beam), round_count)

def move_rocks_north(rock_beams, row, start, finish, round_count):
    for index in range(start, finish):
        if index < start + round_count:
            rock_beams[index][row] = "O"
        else:
            rock_beams[index][row] = "."

def move_rocks_south(rock_beams, row, start, finish, round_count):
    for index in range(start, finish):
        if index >= finish - round_count:
            rock_beams[index][row] = "O"
        else:
            rock_beams[index][row] = "."

def tilt_vertical(rock_beams, north=True):
    for i in range(len(rock_beams[0])):
        first_hash = 0
        round_count = 0
        for j in range(len(rock_beams)):
            if rock_beams[j][i] == "#":
                if north:
                    move_rocks_north(rock_beams, i, first_hash, j, round_count)
                else:
                    move_rocks_south(rock_beams, i, first_hash, j, round_count)

                first_hash = j + 1
                round_count = 0
            elif rock_beams[j][i] == "O":
                round_count += 1

        if north:
            move_rocks_north(rock_beams, i, first_hash, len(rock_beams), round_count)
        else:
            move_rocks_south(rock_beams, i, first_hash, len(rock_beams), round_count)

def spin_cycle(rock_beams):
    tilt_vertical(rock_beams, True)
    tilt_horizontal(rock_beams, False)
    tilt_vertical(rock_beams, False)
    tilt_horizontal(rock_beams, True)

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

    tilt_vertical(rock_beams)

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
        spin_cycle(rock_beams)

        position = calculate_position_check(rock_beams)
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