from aocd import get_data
import re

def pipes_1(text):
    pipes = []
    start_x = ""
    start_y = ""
    for y, line in enumerate(text.split("\n")):
        this_pipe = []
        for x, char in enumerate(re.findall(r"(.)", line)):
            this_pipe.append(char)
            if char == "S":
                start_x = x
                start_y = y
        pipes.append(this_pipe)


    for start_direction in range(3):
        number_of_moves = 0
        direction = start_direction
        x = start_x
        y = start_y
        found_loop = False

        while True:
            if direction == 0:
                x = x + 1
            elif direction == 1:
                y = y + 1
            elif direction == 2:
                x = x - 1
            else:
                y = y - 1

            if (x < 0) or (x > len(pipes[0])) or (y < 0) or (y > len(pipes)):
                break

            char = pipes[y][x]

            number_of_moves += 1
            #print(f"{direction} {char} {number_of_moves}")

            if char == "S":
                found_loop = True
                break
            elif direction == 0:
                if char == "-":
                    pass
                elif char == "J":
                    direction -= 1
                elif char == "7":
                    direction += 1 
                else:
                    break
            elif direction == 1:
                if char == "|":
                    pass
                elif char == "L":
                    direction -= 1
                elif char == "J":
                    direction += 1 
                else:
                    break
            elif direction == 2:
                if char == "-":
                    pass
                elif char == "F":
                    direction -= 1
                elif char == "L":
                    direction += 1 
                else:
                    break
            elif direction == 3:
                if char == "|":
                    pass
                elif char == "7":
                    direction -= 1
                elif char == "F":
                    direction += 1 
                else:
                    break
            else:
                break
            direction = (direction + 4)%4

        print(number_of_moves)
        if found_loop:
            # I think this must always be an even number
            return int(number_of_moves/2)

def pipes_2(text):
    pipes = []
    start_x = ""
    start_y = ""
    for y, line in enumerate(text.split("\n")):
        this_pipe = []
        for x, char in enumerate(re.findall(r"(.)", line)):
            this_pipe.append(char)
            if char == "S":
                start_x = x
                start_y = y
        pipes.append(this_pipe)


    for start_direction in range(3):
        potential_x_enclosures = {}
        potential_y_enclosures = {}

        number_of_moves = 0
        direction = start_direction
        x = start_x
        y = start_y
        found_loop = False

        while True:
            if direction == 0:
                x = x + 1
            elif direction == 1:
                y = y + 1
            elif direction == 2:
                x = x - 1
            else:
                y = y - 1

            if (x < 0) or (x > len(pipes[0])) or (y < 0) or (y > len(pipes)):
                break

            char = pipes[y][x]

            number_of_moves += 1
            #print(f"{direction} {char} {number_of_moves}")

            if char == "S":
                found_loop = True
                if start_direction == direction:
                    if direction == 0 or 2:
                        char = "-"
                    else:
                        char = "|"
                elif direction == 0:
                    if start_direction == 1:
                        char = "7"
                    else:
                        char = "J"
                elif direction == 1:
                    if start_direction == 2:
                        char = "J"
                    else:
                        char = "L"
                elif direction == 2:
                    if start_direction == 3:
                        char = "L"
                    else:
                        char = "F"
                else:
                    if start_direction == 0:
                        char = "F"
                    else:
                        char = "7"
                pipes[y][x] = char
            elif direction == 0:
                if char == "-":
                    pass
                elif char == "J":
                    direction -= 1
                elif char == "7":
                    direction += 1 
                else:
                    break
            elif direction == 1:
                if char == "|":
                    pass
                elif char == "L":
                    direction -= 1
                elif char == "J":
                    direction += 1 
                else:
                    break
            elif direction == 2:
                if char == "-":
                    pass
                elif char == "F":
                    direction -= 1
                elif char == "L":
                    direction += 1 
                else:
                    break
            elif direction == 3:
                if char == "|":
                    pass
                elif char == "7":
                    direction -= 1
                elif char == "F":
                    direction += 1 
                else:
                    break
            else:
                break
            direction = (direction + 4)%4

            add_to_x = False
            add_to_y = False

            if char == "|":
                add_to_x = True
            elif char == "-":
                add_to_y = True
            else:
                add_to_x = True
                add_to_y = True

            if add_to_x:
                if y in potential_x_enclosures:
                    potential_x_enclosures[y].append(x)
                else:
                    potential_x_enclosures[y] = [x]

            if add_to_y:
                if x in potential_y_enclosures:
                    potential_y_enclosures[x].append(y)
                else:
                    potential_y_enclosures[x] = [y]

            if found_loop: 
                break

        #I think you only need to do one of these as all space must be enclosed by both
        if found_loop:
            total_enclosed = 0
            for y, potential_x_enclosure in potential_x_enclosures.items():
                potential_x_enclosure.sort()
                
                i = 0
                while i < len(potential_x_enclosure) - 1:
                    x = potential_x_enclosure[i]
                    next_x = potential_x_enclosure[i+1]
                    if (pipes[y][x] == "F" and pipes[y][next_x] == "7") or (pipes[y][x] == "L" and pipes[y][next_x] == "J"):
                        i += 2
                    else:
                        if (pipes[y][x] == "F" or pipes[y][x] == "L"):
                            i +=1

                        for x in range(potential_x_enclosure[i] + 1, potential_x_enclosure[i+1]):
                            total_enclosed += 1
                        
                        if i + 1 < len(potential_x_enclosure):
                            next_x = potential_x_enclosure[i+1]
                            if pipes[y][next_x] != "|":
                                next_next_x = potential_x_enclosure[i+2]
                                
                                if (pipes[y][next_x] == "F" and pipes[y][next_next_x] == "J") or (pipes[y][next_x] == "L" and pipes[y][next_next_x] == "7"):
                                    i += 3
                                else:
                                    i += 2
                            else:
                                i += 2

            return total_enclosed
        
pipe_text = get_data(day=10, year=2023) 



