from typing import Self
from advent.runner import register
import numpy as np
from scipy import optimize
import math
from dataclasses import dataclass

@dataclass
class Node:
    name: str
    output_names: list[str]
    
    def __post_init__(self: Self):
        self.outputs = []
        self.cached_output_count = {}

    def populate_outputs(self: Self, nodes: dict[str, Self]):
        self.outputs = [nodes[x] for x in self.output_names]

    def output_count(self: Self, target="out"):
        if self.name == target:
            return 1
        
        if target in self.cached_output_count:
            return self.cached_output_count[target]
        
        count = 0
        for node in self.outputs:
            count += node.output_count(target)
        
        self.cached_output_count[target] = count
        return count

@register(11, 2025, 1, True)
def server_rack_1(text):
    nodes = {"out": Node("out", [])}
    
    for line in text:
        name = line[:3]
        node = Node(name, line[5:].split(" "))

        nodes[name] = node

    for node in nodes.values():
        node.populate_outputs(nodes)

    return nodes["you"].output_count()

@register(11, 2025, 2, True)
def server_rack_2(text):
    nodes = {"out": Node("out", [])}
    
    for line in text:
        name = line[:3]
        node = Node(name, line[5:].split(" "))

        nodes[name] = node

    for node in nodes.values():
        node.populate_outputs(nodes)

    if nodes["dac"].output_count("fft") > 0:
        first = "dac"
        second = "fft"
    else:
        first = "fft"
        second = "dac"

    return nodes["svr"].output_count(first) * nodes[first].output_count(second) * nodes[second].output_count("out") 