import re
from advent.runner import register

def check_horizontal_reflection(mirror, needed_errors=0):
    print("horizontal")
    #print(mirror)
    for possible_line in range(0, len(mirror)-1):
        height_to_check = min(possible_line + 1, len(mirror) - possible_line - 1)

        errors = 0
        try:
            for i in range(0, height_to_check):
                for j in range(0, len(mirror[0])):
                    if mirror[possible_line-i][j] != mirror[possible_line + 1 + i][j]:
                        errors += 1
                        if errors > needed_errors:
                            raise Exception("Not reflective") 
            if errors == needed_errors:   
                return possible_line + 1
        except:
            pass
    return 0

def check_vertical_reflection(mirror, needed_errors=0):
    for possible_line in range(0, len(mirror[0])-1):
        width_to_check = min(possible_line + 1, len(mirror[0]) - possible_line - 1)

        errors = 0
        try:
            for i in range(0, len(mirror)):
                for j in range(0, width_to_check):
                    if mirror[i][possible_line-j] != mirror[i][possible_line + 1 + j]:
                        errors += 1
                        if errors > needed_errors:
                            raise Exception("Not reflective")
            if errors == needed_errors:   
                return possible_line + 1
        except:
            pass
    return 0

@register(13, 2023, 1)
def mirrors_1(text):
    all_mirrors = []
    for i, line in enumerate(text.split("\n")):
        if re.match(r"[\.#]+", line):
            if i == 0:
                all_mirrors.append([])
            all_mirrors[-1].append(line)
        else:
            all_mirrors.append([])

    total_reflections = 0
    for mirror in all_mirrors:
        reflection = check_horizontal_reflection(mirror)
        total_reflections += 100 * reflection
        if reflection == 0:
            reflection = check_vertical_reflection(mirror)
            
            if reflection == 0:
                raise Exception("probably shouldnt be here")
            else:
                print(reflection)
                total_reflections += reflection

    return total_reflections

@register(13, 2023, 2)
def mirrors_2(text):
    all_mirrors = []
    for i, line in enumerate(text.split("\n")):
        if re.match(r"[\.#]+", line):
            if i == 0:
                all_mirrors.append([])
            all_mirrors[-1].append(line)
        else:
            all_mirrors.append([])

    total_reflections = 0
    for mirror in all_mirrors:
        reflection = check_horizontal_reflection(mirror, 1)
        total_reflections += 100 * reflection
        if reflection == 0:
            reflection = check_vertical_reflection(mirror, 1)
            
            if reflection == 0:
                raise Exception("probably shouldnt be here")
            else:
                print(reflection)
                total_reflections += reflection

    return total_reflections