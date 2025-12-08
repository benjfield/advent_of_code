from typing import Self
from advent.runner import register
from advent.utils.split_text import create_char_grid
from advent.utils.grid import Grid
from dataclasses import dataclass
from functools import cache
from collections import defaultdict
from sortedcontainers import SortedDict

@dataclass
class Junction:
    x: int
    y: int
    z: int

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y and self.z == value.z
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __post_init__(self: Self):
        self.circuit: set = {self}
        self.circuit_length: int = 0

    @classmethod
    def from_coord_string(cls: Self, coord_string: str) -> Self:
        coords = coord_string.split(",")
        return cls(
            x=int(coords[0]),
            y=int(coords[1]),
            z=int(coords[2]),
        )

    def distance(self: Self, other: Self) -> int:
        return ((self.x - other.x)**2 + abs(self.y - other.y)**2 + abs(self.z - other.z)**2)**(1/2) 
    
    def join(self: Self, other: Self, distance: int):
        if other not in self.circuit:
            self.circuit.update(other.circuit)
            for j in other.circuit:
                j.circuit = self.circuit
                
@register(8, 2025, 1, True)
def junction_1(text, count=1000):
    junctions = [Junction.from_coord_string(line) for line in text]

    link_distances = []

    for i, junc1 in enumerate(junctions[:-1]):
        for junc2 in junctions[i+1:]:
            distance = junc1.distance(junc2)

            link_distances.append((distance, junc1, junc2))

    link_distances.sort(
        key=lambda x: x[0]
    )

    for (distance, junc1, junc2) in link_distances[:count]:
        junc1.join(junc2, distance)
    
    total_junctions = set(junctions)
    circuit_lengths = []

    i = 0
    while len(total_junctions) > 0:
        junc = next(iter(total_junctions))
        circuit_lengths.append(len(junc.circuit))
        total_junctions.difference_update(junc.circuit)

    circuit_lengths.sort(reverse=True)

    product = 1
    for i in range(3):
        product *= circuit_lengths[i]

    return product

                        
@register(8, 2025, 2, True)
def junction_2(text):
    junctions = [Junction.from_coord_string(line) for line in text]

    link_distances = []

    for i, junc1 in enumerate(junctions[:-1]):
        for junc2 in junctions[i+1:]:
            distance = junc1.distance(junc2)

            link_distances.append((distance, junc1, junc2))

    link_distances.sort(
        key=lambda x: x[0]
    )

    for (distance, junc1, junc2) in link_distances:
        junc1.join(junc2, distance)

        if len(junc1.circuit) == len(junctions):
            return junc1.x * junc2.x