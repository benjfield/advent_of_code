import re
import math
from advent.runner import register

@register(6, 2023, 1)
def boat_1(text):
    text_lines = text.split("\n")
    times = re.findall(r"(\d+)", text_lines[0])
    distances = re.findall(r"(\d+)", text_lines[1])

    if len(times) != len(distances):
        raise Exception("incorrect parsing")

    margins_multiple = 1

    for i in range(len(times)):
        time = int(times[i])
        #Add one as it must beat it
        distance = int(distances[i]) + 1

        maximum_time = math.floor((time + (time**2 - 4 * distance)**(1/2))/2)

        minimum_time = math.ceil((time - (time**2 - 4 * distance)**(1/2))/2)

        print(f"max {maximum_time} min {minimum_time}")
        if maximum_time >= minimum_time:
            margins_multiple = margins_multiple * (maximum_time - minimum_time + 1)

    return margins_multiple

@register(6, 2023, 2)
def boat_2(text):
    text_lines = text.split("\n")
    #Could equally find replace white space
    time = ""

    for time_string in re.findall(r"(\d+)", text_lines[0]):
        time += time_string
        
    distance = ""

    for distance_string in re.findall(r"(\d+)", text_lines[1]):
        distance += distance_string

    time = int(time)
    #Add one as it must beat it
    distance = int(distance) + 1

    maximum_time = math.floor((time + (time**2 - 4 * distance)**(1/2))/2)

    minimum_time = math.ceil((time - (time**2 - 4 * distance)**(1/2))/2)

    return maximum_time - minimum_time + 1
    