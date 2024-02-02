from numba import int64, int32
from numba.experimental import jitclass 
import numpy as np


spec = [
    ('initial_state', int64[:]),
    ('state', int64[:]),
    ('address', int32),
    ('input_address', int32),
    ('relative_base', int32),
    ('inputs', int64[:])
]

def pre_generate_initial_state(initial_state_string):
    return np.array([ np.int64(x) for x in initial_state_string.split(",") ], dtype=np.int64)

def computer_from_string(initial_state_string):
    return Computer(pre_generate_initial_state(initial_state_string))

def process(computer, input):
    input_array = np.array(input, dtype=np.int64)
    return computer.process(input_array)

#@jitclass(spec)
class Computer:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.state = self.initial_state.copy()
        self.reset_addresses_and_inputs()

    def reset_addresses_and_inputs(self):
        self.address = 0
        self.input_address = 0
        self.relative_base = 0
        self.indexes = np.zeros(3, dtype=np.int32)
        self.inputs = np.empty(0, dtype=np.int64)

    def reset(self):
        for i in range(len(self.state)):
            if i >= len(self.initial_state):
                self.state[i] = 0
            else:
                self.state[i] = self.initial_state[i]
        self.reset_addresses_and_inputs()

    def reset_to_total_state(self, total_state):
        self.state = total_state["state"].copy()
        self.address = total_state["address"]
        self.input_address = total_state["input_address"]
        self.relative_base = total_state["relative_base"]
        self.inputs = total_state["inputs"].copy()

    def get_total_state(self):
        return {
            "state": self.state.copy(),
            "address": self.address,
            "input_address": self.input_address,
            "relative_base": self.relative_base,
            "inputs": self.inputs.copy()
        }

    def update_indexes(self, mode, number_of_inputs):
        max_index = 0
        for i in range(number_of_inputs):
            mode_modulo = int((mode%(10**(i+1)))/(10**i))
            match mode_modulo:
                case 0:
                    index_to_add = self.state[self.address + i + 1]
                case 1:
                    index_to_add = self.address + i + 1
                case 2:
                    index_to_add = self.relative_base + self.state[self.address + i + 1]
                case _:
                    raise Exception("not implemented")
            self.indexes[i] = index_to_add
            if index_to_add > max_index:
                max_index = index_to_add
        self.check_state_length(max_index)

    def check_state_length(self, max_index):
        prior_length = len(self.state)
        if prior_length < max_index + 1:
            self.state = np.resize(self.state, max_index + 1)

            for i in range(prior_length, max_index + 1):
                self.state[i] = 0

    def process_without_input(self):
        return self.process(np.empty(0, dtype=np.int64))

    def process(self, input):   
        self.inputs  = np.append(self.inputs, input)
        outputs = []

        while self.address < len(self.state):
            #print(f"address {self.address} state {self.state} input {self.inputs} input_address {self.input_address}")

            instruction = self.state[self.address]%100

            mode = int(self.state[self.address]/100)

            #print(f"initial {self.state[self.address]} instruction {instruction} mode {mode}")

            match instruction:
                case 1:
                    self.update_indexes(mode, 3)
                    
                    self.state[self.indexes[2]] = self.state[self.indexes[1]] + self.state[self.indexes[0]]
                    self.address += 4
                case 2:
                    self.update_indexes(mode, 3)
                    
                    self.state[self.indexes[2]] = self.state[self.indexes[1]] * self.state[self.indexes[0]]
                    self.address += 4
                case 3:
                    if len(self.inputs) <= self.input_address:
                        return False, outputs
                    
                    self.update_indexes(mode, 1)

                    self.state[self.indexes[0]] = self.inputs[self.input_address]
                    self.input_address += 1
                    self.address += 2
                case 4:
                    self.update_indexes(mode, 1)
                    
                    outputs.append(self.state[self.indexes[0]])
                    
                    self.address += 2
                case 5:
                    self.update_indexes(mode, 2)

                    if self.state[self.indexes[0]] != 0:
                        self.address = self.state[self.indexes[1]]
                    else:
                        self.address += 3
                case 6:
                    self.update_indexes(mode, 2)

                    if self.state[self.indexes[0]] == 0:
                        self.address = self.state[self.indexes[1]]
                    else:
                        self.address += 3
                case 7:
                    self.update_indexes(mode, 3)

                    if self.state[self.indexes[0]] < self.state[self.indexes[1]]:
                        self.state[self.indexes[2]] = 1
                    else:
                        self.state[self.indexes[2]] = 0

                    self.address += 4
                case 8:
                    self.update_indexes(mode, 3)

                    if self.state[self.indexes[0]] == self.state[self.indexes[1]]:
                        self.state[self.indexes[2]] = 1
                    else:
                        self.state[self.indexes[2]] = 0

                    self.address += 4            
                case 9:
                    self.update_indexes(mode, 1)

                    self.relative_base += self.state[self.indexes[0]]
                    self.address += 2
                case 99:
                    return True, outputs
                case _:
                    raise Exception(f"Unknown: Instruction {instruction} Address {self.address}")
            
        raise Exception("not terminated")