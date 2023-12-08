import re
from aocd import get_data

def path_1(text):
    paths = {}
    route = ""
    for i, line in enumerate(text.split("\n")):

        if i == 0:
            route = line
        else:
            parsed_route = re.search(r"(\w+) = \((\w+), (\w+)\)", line)
            if parsed_route:
                paths[parsed_route.group(1)] = {
                    "L": parsed_route.group(2),
                    "R": parsed_route.group(3)
                }

    location = "AAA"
    step_counter = 0
    while location != "ZZZ":
        for char in route:
            location = paths[location][char]
            step_counter += 1

            if location == "ZZZ":
                break
            
    return step_counter

def path_2(text):
    paths = {}
    route = ""
    for i, line in enumerate(text.split("\n")):

        if i == 0:
            route = line
        else:
            parsed_route = re.search(r"(\w+) = \((\w+), (\w+)\)", line)
            if parsed_route:
                paths[parsed_route.group(1)] = {
                    "L": parsed_route.group(2),
                    "R": parsed_route.group(3)
                }

    locations = []
    cycle_possibilities = []


    for possible_start in paths.keys():
        if possible_start[-1] == "A":
            locations.append(possible_start)
            cycle_possibilities.append({})


    step_counter = 0
    location_check = 0
    while location_check < len(locations):
        location_check = 0

        char = route[step_counter%len(route)]

        #print(f"{step_counter} {locations} {char}")
        for i, location in enumerate(locations):
            location = paths[location][char]

            if location[-1] == "Z":
                location_check += 1

            locations[i] = location

        step_counter += 1

    return step_counter

path_text = get_data(day=8, year=2023)
print(path_2(path_text))