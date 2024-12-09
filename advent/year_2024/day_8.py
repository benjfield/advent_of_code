from advent.runner import register
import math
from itertools import combinations

@register(8, 2024, 1, True)
def func_1(text):
    antennas = {}

    for y, line in enumerate(text):
        for x, char in enumerate(line):
            if char != ".":
                if char in antennas:
                    antennas[char].append((x, y))
                else:
                    antennas[char] = [(x, y)]

    antinodes = set()

    for nodes in antennas.values():
        for n1, n2 in combinations(nodes, 2):
            difference_x = n2[0] - n1[0]
            difference_y = n2[1] - n1[1]

            antinode_1 = (n1[0] - difference_x, n1[1] -  difference_y)
            if antinode_1[0] >= 0 and antinode_1[0]< len(line) and antinode_1[1] >= 0 and antinode_1[1] < len(text):
                antinodes.add(antinode_1)

            antinode_2 = (n2[0] + difference_x, n2[1] +  difference_y)
            if antinode_2[0] >= 0 and antinode_2[0]< len(line) and antinode_2[1] >= 0 and antinode_2[1] < len(text):
                antinodes.add(antinode_2)

    return len(antinodes)

@register(8, 2024, 2, True)
def func_2(text):
    antennas = {}

    for y, line in enumerate(text):
        for x, char in enumerate(line):
            if char != ".":
                if char in antennas:
                    antennas[char].append((x, y))
                else:
                    antennas[char] = [(x, y)]

    antinodes = set()

    for nodes in antennas.values():
        for n1, n2 in combinations(nodes, 2):
            difference_x = n2[0] - n1[0]
            difference_y = n2[1] - n1[1]

            antinode = n1
            while antinode[0] >= 0 and antinode[0]< len(line) and antinode[1] >= 0 and antinode[1] < len(text):
                antinodes.add(antinode)
                antinode = (antinode[0] - difference_x, antinode[1] - difference_y)

            antinode = n1
            while antinode[0] >= 0 and antinode[0]< len(line) and antinode[1] >= 0 and antinode[1] < len(text):
                antinodes.add(antinode)
                antinode = (antinode[0] + difference_x, antinode[1] + difference_y)
                
    return len(antinodes)