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

'''XORn = Xn XOR Yn
ANDn = Xn AND Yn
CARRYANDn = CARRYN AND XORn
           
Zn = CARRYN XOR XORN
CARRYN = CARRYANDn OR ANDn'''
class WireType(Enum):
    X = auto()
    Y = auto()
    Z = auto()
    XORN_CARRYN = auto()
    ANDN_CARRYANDN = auto()
    XORN = auto()
    ANDN = auto()
    CARRYANDN = auto()
    CARRYN = auto()
    UNKNOWN = auto()
            
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
                print(letter)
                raise Exception("Unknown Type")

class Wire:
    name: str
    type: WireType
    index: int
    original_state: State
    state: State
    downstream: list
    original_upstream: any
    upstream: any

    def __init__(self, name, state=State.UNKNOWN):
        self.name = name
        self.state = state
        self.original_state = state

        match = re.match(r"(\w)(\d+)", name)

        if match is None:
            self.type = WireType.UNKNOWN
            self.index = 0
        else:
            self.type = WireType.from_letter(match.group(1))
            self.index = int(match.group(2))
        
        self.downstream = []

    def set_initial_wire_type(self):
        if self.type == WireType.UNKNOWN:
            downstream_gate_types = set(
                [x.type for x in self.downstream]
            )

            if downstream_gate_types == set([GateType.AND, GateType.XOR]):
                    self.type = WireType.XORN_CARRYN
            elif downstream_gate_types == set([GateType.OR]):
                    self.type = WireType.ANDN_CARRYANDN
            else:
                raise Exception("Unknown type")

    def check_initial_wire_type(self):
        match self.type:
            case WireType.XORN_CARRYN:
                if self.upstream.designation not in set([Designation.XORN, Designation.CARRYN]):
                    return self.name
            case WireType.ANDN_CARRYANDN:
                if self.upstream.designation not in set([Designation.ANDN, Designation.CARRYANDN]):
                    return self.name
            case WireType.Z:
                if self.upstream.designation != Designation.ZN:
                    return self.name
        
        return None
               
    def set_original_upstream(self, upstream):
        self.upstream = upstream
        self.original_upstream = upstream

    def set_state(self, state):
        self.state = state
        self.propogate_state()

    def propogate_state(self):
        for g in self.downstream:
            g.check_state()

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

'''XORn = Xn XOR Yn
ANDn = Xn AND Yn

CARRYANDn = CARRYN AND XORn
Zn = CARRYN XOR XORN
CARRYN = CARRYANDn OR ANDn'''
class Designation(Enum):
    X = auto()
    Y = auto()
    Z = auto()
    XORN = auto()
    ANDN = auto()
    CARRYANDN = auto()
    ZN = auto()
    CARRYN = auto()

@dataclass
class Gate:
    state: State
    type: GateType
    designation: Designation
    index: int
    upstream: list[Wire]
    original_downstream: Wire
    downstream: Wire

    def __init__(
        self,
        type,
        upstream,
        downstream):
        self.state = State.UNKNOWN
        self.type = type
        self.upstream = upstream
        
        self.original_downstream = downstream
        self.downstream = downstream

    def set_designation(self):
        upstream_wire_types = set(
            [x.type for x in self.upstream]
        )

        if upstream_wire_types == set([WireType.X, WireType.Y]):
            self.index = self.upstream[0].index
            if self.type == GateType.AND:
                self.designation = Designation.ANDN
            elif self.type == GateType.XOR:
                self.designation = Designation.XORN
            else:
                raise Exception
        elif len(upstream_wire_types) == 1 and upstream_wire_types == set([WireType.XORN_CARRYN]):
            if self.type == GateType.AND:
                self.designation = Designation.CARRYANDN
            elif self.type == GateType.XOR:
                self.designation = Designation.ZN
            else:
                raise Exception
        elif len(upstream_wire_types) == 1 and upstream_wire_types == set([WireType.ANDN_CARRYANDN]):
            if self.type == GateType.OR:
                self.designation = Designation.CARRYN
            else:
                raise Exception 
        else:
            print(upstream_wire_types)
            raise Exception

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

def get_set_wire(wires, wire_name, state=State.UNKNOWN):
    wire = wires.get(wire_name, Wire(wire_name, state))
    if wire_name not in wires:
        wires[wire_name] = wire

    return wire

def set_up_wires_gates(text):
    wires = {}
    gates = []
    spl = text.split("\n\n")
    for line in spl[0].split("\n"):
        match = re.match(r"(.*): (0|1)", line)

        wire_name = match.group(1)
        wires[match.group(1)] = Wire(wire_name, State.from_string(match.group(2)))

    for line in spl[1].split("\n"):
        match = re.match(r"(.*) (.*) (.*) -> (.*)", line)

        wire_1 = get_set_wire(wires, match.group(1))
        wire_2 = get_set_wire(wires, match.group(3))
        wire_3 = get_set_wire(wires, match.group(4))

        gate_type = GateType.from_string(match.group(2))

        gate = Gate(gate_type, [wire_1, wire_2], wire_3)

        gates.append(gate)

        wire_1.downstream.append(gate)
        wire_2.downstream.append(gate)
        wire_3.set_original_upstream(gate)
    
    return wires, gates

@register(24, 2024, 1)
def func_1(text):
    wires, gates = set_up_wires_gates(text)

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
    wires, gates = set_up_wires_gates(text)

    for w in wires.values():
        w.set_initial_wire_type()

    for g in gates:
        g.set_designation()

    broken_names = []
    for w in wires.values():
        broken_name = w.check_initial_wire_type()
        if broken_name is not None and broken_name != "z00" and broken_name != "z45" and broken_name != "rfg":
            broken_names.append(broken_name)

    broken_names.sort()

    return ",".join(broken_names)