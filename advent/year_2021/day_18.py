from advent.runner import register
import math
import itertools

def add_snailfish_number(number_1, number_2):
    return [number_1, number_2]

def explode_all(number):
    number_changed = 0
    for a in range(len(number)):
        if isinstance(number[a], list):
            for b in range(len(number[a])):
                if isinstance(number[a][b], list):
                    for c in range(len(number[a][b])):
                        if isinstance(number[a][b][c], list):
                            for d in range(len(number[a][b][c])):
                                if isinstance(number[a][b][c][d], list):
                                    if d == 0: 
                                        if isinstance(number[a][b][c][1], int):
                                            number[a][b][c][1] += number[a][b][c][d][1]
                                        else:
                                            number[a][b][c][1][0] += number[a][b][c][d][1]
                                    else:
                                        if c == 0:
                                            if isinstance(number[a][b][1], int):
                                                number[a][b][1] += number[a][b][c][d][1]
                                            elif isinstance(number[a][b][1][0], int):
                                                number[a][b][1][0] += number[a][b][c][d][1]
                                            else:
                                                number[a][b][1][0][0] += number[a][b][c][d][1]
                                        else:
                                            if b == 0:
                                                if isinstance(number[a][1], int):
                                                    number[a][1] += number[a][b][c][d][1]
                                                elif isinstance(number[a][1][0], int):
                                                    number[a][1][0] += number[a][b][c][d][1]
                                                elif isinstance(number[a][1][0][0], int):
                                                    number[a][1][0][0] += number[a][b][c][d][1]
                                                else:
                                                    number[a][1][0][0][0] += number[a][b][c][d][1]
                                            else:
                                                if a == 0:
                                                    if isinstance(number[1], int):
                                                        number[1] += number[a][b][c][d][1]
                                                    elif isinstance(number[1][0], int):
                                                        number[1][0] += number[a][b][c][d][1]
                                                    elif isinstance(number[1][0][0], int):
                                                        number[1][0][0] += number[a][b][c][d][1]
                                                    elif isinstance(number[1][0][0][0], int):
                                                        number[1][0][0][0] += number[a][b][c][d][1]
                                                    else:
                                                        number[1][0][0][0][0] += number[a][b][c][d][1]

                                    if d == 1: 
                                        number[a][b][c][0] += number[a][b][c][d][0]
                                    else:
                                        if c == 1:
                                            if isinstance(number[a][b][0], int):
                                                number[a][b][0] += number[a][b][c][d][0]
                                            else:
                                                number[a][b][0][1] += number[a][b][c][d][0]
                                        else:
                                            if b == 1:
                                                if isinstance(number[a][0], int):
                                                    number[a][0] += number[a][b][c][d][0]
                                                elif isinstance(number[a][0][1], int):
                                                    number[a][0][1] += number[a][b][c][d][0]
                                                else:
                                                    number[a][0][1][1] += number[a][b][c][d][0]
                                            else:
                                                if a == 1:
                                                    if isinstance(number[0], int):
                                                        number[0] += number[a][b][c][d][0]
                                                    elif isinstance(number[0][1], int):
                                                        number[0][1] += number[a][b][c][d][0]
                                                    elif isinstance(number[0][1][1], int):
                                                        number[0][1][1] += number[a][b][c][d][0]
                                                    else:
                                                        number[0][1][1][1] += number[a][b][c][d][0]

                                    number[a][b][c][d] = 0
                                    number_changed += 1
    return number_changed

def split(number):
    for a in range(len(number)):
        if isinstance(number[a], list):
            for b in range(len(number[a])):
                if isinstance(number[a][b], list):
                    for c in range(len(number[a][b])):
                        if isinstance(number[a][b][c], list):
                            for d in range(len(number[a][b][c])):
                                if isinstance(number[a][b][c][d], list):
                                    raise Exception("Shouldn't happen after explode")
                                elif number[a][b][c][d] >= 10:
                                    number[a][b][c][d] = [math.floor(number[a][b][c][d]/2), math.ceil(number[a][b][c][d]/2)]
                                    return True
                        elif number[a][b][c] >= 10:
                            number[a][b][c] = [math.floor(number[a][b][c]/2), math.ceil(number[a][b][c]/2)]
                            return True
                elif number[a][b] >= 10:
                    number[a][b] = [math.floor(number[a][b]/2), math.ceil(number[a][b]/2)]
                    return True
        elif number[a] >= 10:
            number[a] = [math.floor(number[a]/2), math.ceil(number[a]/2)]
            return True
    return False

def reduce(number):
    changed = True
    while changed:
        explode_all(number)
        changed = split(number)

def addition(text):
    split_text = text.split("\n")

    number = eval(split_text[0])
    for new_line in split_text[1:]:
        number = [number, eval(new_line)]

        reduce(number)
    return number

def magnitude(number):
    if isinstance(number, int):
        return number
    else:
        return 3 * magnitude(number[0]) + 2 * magnitude(number[1]) 

@register(18, 2021, 1)
def snailfish_1(text):
    number = addition(text)

    return magnitude(number)

@register(18, 2021, 2)
def snailfish_2(text):
    largest_magnitude = 0
    
    for combo in itertools.permutations(text.split("\n"), 2):
        number = [eval(combo[0]), eval(combo[1])]

        reduce(number)

        number_magnitude = magnitude(number)

        if number_magnitude > largest_magnitude:
            largest_magnitude = number_magnitude

    return largest_magnitude


