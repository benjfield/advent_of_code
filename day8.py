import re
from aocd import get_data
from math import lcm

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

    for possible_start in paths.keys():
        if possible_start[-1] == "A":
            locations.append(possible_start)

    cycle_possibilities = []

    for i in range(len(locations)):
        location = locations[i]
        cycle_keys = {}
        possible_outs = []
        step_counter = 0
        found_cycle = False
        while not found_cycle:  
            route_index = step_counter%len(route)
            cycle_key = f"{location}_{route_index}"
            if location[-1] == "Z":
                print(location)
                print(step_counter)
                possible_outs.append(step_counter)
            
            if cycle_key in cycle_keys:
                new_possible_outs = []
                for possible_out in possible_outs:
                    if possible_out > cycle_keys[cycle_key]:
                        new_possible_outs.append(possible_out)

                cycle_possibilities.append({
                    "initial": cycle_keys[cycle_key],
                    "length": step_counter - cycle_keys[cycle_key],
                    "possible_outs": new_possible_outs
                })
                found_cycle = True
            else:
                cycle_keys[cycle_key] = step_counter
                location = paths[location][route[route_index]]
                step_counter += 1

    number = cycle_possibilities[0]["possible_outs"][-1] 
    for cycle in cycle_possibilities:
        number = lcm(number, cycle["possible_outs"][0])
        
    return number

path_text = get_data(day=8, year=2023)