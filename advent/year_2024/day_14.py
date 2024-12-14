from advent.runner import register
from advent.utils.split_text import split_text, Split
from dataclasses import dataclass
import math
from functools import cache
from collections import defaultdict

from advent.utils.direction import Direction

from time import perf_counter

import re

@dataclass
class Robot:
    pos_x: int
    pos_y: int
    vel_x: int
    vel_y: int

    def move(self, moves: int, width: int, height: int):
        self.pos_x = (self.pos_x + moves * self.vel_x ) % width
        self.pos_y = (self.pos_y + moves * self.vel_y ) % height


@register(14, 2024, 1)
def func_1(text, width = 101, height = 103):
    robots = []
    for line in split_text(text, Split.LINE):

        match = re.match(r"p=([\+\-]?\d+),([\+\-]?\d+) v=([\+\-]?\d+),([\+\-]?\d+)", line)

        robots.append(Robot(
            int(match.group(1)),
            int(match.group(2)),
            int(match.group(3)),
            int(match.group(4)),
        ))

    quadrant = defaultdict(int)
    for robot in robots:
        robot.move(100, width, height)
        ignore = False
        if robot.pos_x < (width - 1)//2:
            x = 1
        elif robot.pos_x > (width - 1)//2:
            x = 2
        else:
            ignore = True
        
        if robot.pos_y < (height - 1)//2:
            y = 1
        elif robot.pos_y > (height - 1)//2:
            y = 2
        else:
            ignore = True

        if not ignore:
            quadrant[(x, y)] += 1

    safety = 1
    for i in quadrant.values():
        safety *= i

    return safety

    

@register(14, 2024, 2)
def func_2(text, width = 101, height = 103):
    robots = []
    for line in split_text(text, Split.LINE):

        match = re.match(r"p=([\+\-]?\d+),([\+\-]?\d+) v=([\+\-]?\d+),([\+\-]?\d+)", line)

        robots.append(Robot(
            int(match.group(1)),
            int(match.group(2)),
            int(match.group(3)),
            int(match.group(4)),
        ))

    print(len(robots))

    second = 0
    while True:
        heights = defaultdict(set)
        second += 1
        for robot in robots:
            robot.move(1, width, height)

            heights[robot.pos_x].add(robot.pos_y)
            
        for height_set in heights.values():
            if len(height_set) == 26:
                positions = set()
                for robot in robots:
                    positions.add((robot.pos_x, robot.pos_y))

                for y in range(103):
                    print("".join(["#" if (x,y ) in positions else "." for x in range(101)]))
                print(second)
                print("")