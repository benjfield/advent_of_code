
import re
import itertools
from advent.runner import register
import math

class Moon:
    def __init__(
            self,
            position):
        self.position = position
        self.velocity = {
            "x": 0,
            "y": 0,
            "z": 0
        }

    def move_to_moon(self, other_moon):
        for key in self.position.keys():
            if self.position[key] > other_moon.position[key]:
                self.velocity[key] -= 1
                other_moon.velocity[key] += 1
            elif self.position[key] < other_moon.position[key]:
                self.velocity[key] += 1
                other_moon.velocity[key] -= 1
    
    def move(self):
        for key in self.position.keys():
            self.position[key] += self.velocity[key]

    def potential_energy(self):
        total = 0
        for values in self.position.values():
            total += abs(values)
        return total

    def kinetic_energy(self):
        total = 0
        for values in self.velocity.values():
            total += abs(values)
        return total

@register(12, 2019, 1)
def moons_1(text, time=1000):
    moons = []
    for moon_text in text.split("\n"):
        matched_text = re.match(r"<x=([-\d]+), y=([-\d]+), z=([-\d]+)>", moon_text)
        position =  {
            "x": int(matched_text.group(1)),
            "y": int(matched_text.group(2)),
            "z": int(matched_text.group(3))
        }
        moons.append(Moon(position))

    for i in range(time):
        for moon, other_moon in itertools.combinations(moons, 2):
            moon.move_to_moon(other_moon)

        for moon in moons:
            moon.move()

    total_energy = 0
    for moon in moons:
        total_energy += moon.potential_energy() * moon.kinetic_energy()

    return total_energy

def create_state_key(moons, key):
    state = []
    for moon in moons:
        state.append(moon.position[key])
        state.append(moon.velocity[key])

    return tuple(state)

@register(12, 2019, 2)
def moons_2(text):
    moons = []
    for moon_text in text.split("\n"):
        matched_text = re.match(r"<x=([-\d]+), y=([-\d]+), z=([-\d]+)>", moon_text)
        position =  {
            "x": int(matched_text.group(1)),
            "y": int(matched_text.group(2)),
            "z": int(matched_text.group(3))
        }
        moons.append(Moon(position))

    x_cache = {}
    y_cache = {}
    z_cache = {}

    x_remainder = 0
    x_loop_length = 0
    y_remainder = 0
    y_loop_length = 0
    z_remainder = 0
    z_loop_length = 0

    i = 0
    while x_loop_length == 0 or y_loop_length == 0 or z_loop_length == 0:
        if x_loop_length == 0:
            x_state = create_state_key(moons, "x")
            if x_state in x_cache:
                x_remainder = x_cache[x_state]
                x_loop_length = i - x_remainder
            else:
                x_cache[x_state] = i

        if y_loop_length == 0:
            y_state = create_state_key(moons, "y")
            if y_state in y_cache:
                y_remainder = y_cache[y_state]
                y_loop_length = i - y_remainder
            else:
                y_cache[y_state] = i

        if z_loop_length == 0:
            z_state = create_state_key(moons, "z")
            if z_state in z_cache:
                z_remainder = z_cache[z_state]
                z_loop_length = i - z_remainder
            else:
                z_cache[z_state] = i

        for moon, other_moon in itertools.combinations(moons, 2):
            moon.move_to_moon(other_moon)

        for moon in moons:
            moon.move()

        i += 1

    if x_remainder != 0 or y_remainder != 0 or z_remainder != 0:
        raise Exception("Not a clean remainder")

    return math.lcm(x_loop_length, y_loop_length, z_loop_length)