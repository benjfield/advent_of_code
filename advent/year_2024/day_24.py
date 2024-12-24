from advent.runner import register
from advent.utils.split_text import split_text, Split
from advent.utils.grid import Grid
from dataclasses import dataclass
import math
from functools import cache
from collections import defaultdict

from advent.utils.direction import Direction, Rotation

from time import perf_counter

import re

from functools import partial

from advent.utils.path_finding_2 import MapNode, djikstra, has_final_coords_function, ClosedList
from dataclasses import dataclass
from enum import Enum, auto
from numba import jit

class State(Enum):
    UNKNOWN = auto()
    ON = auto()
    OFF = auto()

    @classmethod
    def from_string(cls, string):
        match string:
            case "1":
                return cls.ON
            case "0":
                return cls.OFF
            case _:
                raise Exception("Unknown State")

    def to_string(self):
        match self:
            case State.ON:
                return "1"
            case State.OFF:
                return "0"
            case _:
                raise Exception("Unknown State")
            
    def to_int(self):
        match self:
            case State.ON:
                return 1
            case State.OFF:
                return 0
            case _:
                raise Exception("Unknown State")
            
class WireType(Enum):
    X = auto()
    Y = auto()
    Z = auto()
    OTHER = auto()
            
    @classmethod
    def from_letter(cls, letter):
        match letter:
            case "x":
                return WireType.X
            case "y":
                return WireType.Y
            case "z":
                return WireType.Z
            case _:
                raise Exception("Unknown Type")
        
class Upstream:
    def __init__(self):
        wires = set()
        gates = set()
    
    
class Wire:
    name: str
    type: WireType
    index: int
    original_state: State
    state: State
    downstream: list
    original_upstream: any
    upstream_details: Upstream

    def __init__(self, name, state=State.UNKNOWN):
        self.name = name
        self.state = state

        match = re.match(r"(/w/d+)")

        if match is None:
            self.type = WireType.OTHER
            self.index = 0
        else:
            self.type = WireType.from_letter(match.group(1))
            self.index = WireType.from_letter(match.group(2))

        self.upstream_details = None

    def set_state(self, state):
        self.state = state
        self.propogate_state()

    def propogate_state(self):
        for g in self.downstream:
            g.check_state()

    def populate_upstream(self, reset = True):
        if self.original_upstream is None:
            return 



class GateType(Enum):
    AND = auto()
    OR = auto()
    XOR = auto()

    @classmethod
    def from_string(cls, string):
        match string:
            case "AND":
                return cls.AND
            case "OR":
                return cls.OR
            case "XOR":
                return cls.XOR
            case _:
                raise Exception("Unknown Type")
            
@dataclass
class Gate:
    state: State
    type: GateType
    upstream: list[Wire]
    downstream: Wire

    def check_state(self):
        for w in self.upstream:
            if w.state == State.UNKNOWN:
                return
        
        match self.type:
            case GateType.AND:
                for w in self.upstream:
                    if w.state == State.OFF:
                        return self.set_state(State.OFF)
                return self.set_state(State.ON)
            case GateType.OR:
                for w in self.upstream:
                    if w.state == State.ON:
                        return self.set_state(State.ON)
                return self.set_state(State.OFF)
            case GateType.XOR:
                if self.upstream[0].state != self.upstream[1].state:
                    return self.set_state(State.ON)
                return self.set_state(State.OFF)

    def set_state(self, state):
        self.state = state
        self.downstream.set_state(state)

@register(24, 2024, 1)
def func_1(text):
    wires = {}
    gates = []
    spl = text.split("\n\n")
    for line in spl[0].split("\n"):
        match = re.match(r"(.*): (0|1)", line)

        wire_name = match.group(1)
        wires[match.group(1)] = Wire(wire_name, State.from_string(match.group(2)), [])

    for line in spl[1].split("\n"):
        match = re.match(r"(.*) (.*) (.*) -> (.*)", line)

        wire_1_name = match.group(1)
        wire_1 = wires.get(wire_1_name, Wire(wire_1_name, State.UNKNOWN, []))
        if wire_1_name not in wires:
            wires[wire_1_name] = wire_1
        
        wire_2_name = match.group(3)
        wire_2 = wires.get(wire_2_name, Wire(wire_2_name, State.UNKNOWN, []))
        if wire_2_name not in wires:
            wires[wire_2_name] = wire_2

        wire_3_name = match.group(4)
        wire_3 = wires.get(wire_3_name, Wire(wire_3_name, State.UNKNOWN, []))
        if wire_3_name not in wires:
            wires[wire_3_name] = wire_3

        gate_type = GateType.from_string(match.group(2))

        gate = Gate(State.UNKNOWN, gate_type, [wire_1, wire_2], wire_3)

        gates.append(gate)

        wire_1.downstream.append(gate)
        wire_2.downstream.append(gate)

        wire_3.original_upstream.append(gate)

    for w in wires.values():
        if w.state != State.UNKNOWN:
            w.propogate_state()

    final_wire_names = [x for x in wires.keys() if x[0] == "z"]

    final_wire_names.sort()

    answer = 0
    for i, name in enumerate(final_wire_names):
        answer += wires[name].state.to_int() * (2 **i)

    return answer

@register(24, 2024, 2)
def func_2(text):
    wires = {}
    gates = []
    spl = text.split("\n\n")
    for line in spl[0].split("\n"):
        match = re.match(r"(.*): (0|1)", line)

        wire_name = match.group(1)
        wires[match.group(1)] = Wire(wire_name, State.from_string(match.group(2)), [], None)

    for line in spl[1].split("\n"):
        match = re.match(r"(.*) (.*) (.*) -> (.*)", line)

        wire_1_name = match.group(1)
        wire_1 = wires.get(wire_1_name, Wire(wire_1_name, State.UNKNOWN, [], None))
        if wire_1_name not in wires:
            wires[wire_1_name] = wire_1
        
        wire_2_name = match.group(3)
        wire_2 = wires.get(wire_2_name, Wire(wire_2_name, State.UNKNOWN, [], None))
        if wire_2_name not in wires:
            wires[wire_2_name] = wire_2

        wire_3_name = match.group(4)
        wire_3 = wires.get(wire_3_name, Wire(wire_3_name, State.UNKNOWN, [], None))
        if wire_3_name not in wires:
            wires[wire_3_name] = wire_3

        gate_type = GateType.from_string(match.group(2))

        gate = Gate(State.UNKNOWN, gate_type, [wire_1, wire_2], wire_3)

        gates.append(gate)

        wire_1.downstream.append(gate)
        wire_2.downstream.append(gate)

        wire_3.original_upstream = gate

    final_wire_names = [x for x in wires.keys() if x[0] == "z"]

    final_wire_names.sort()




    return answer