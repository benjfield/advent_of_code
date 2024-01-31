from numba import int64
from numba.experimental import jitclass 
import numpy as np


spec = [
    ('initial_state', int64[:]),
    ('state', int64[:]),
    ('address', int64),
    ('input_address', int64),
    ('relative_base', int64),
    ('inputs', int64[:])
]


def pre_generate_initial_state(initial_state_string):
    return np.array([ np.int64(x) for x in initial_state_string.split(",") ], dtype=np.int64)

def computer_from_string(initial_state_string):
    return Computer(pre_generate_initial_state(initial_state_string))

def process(computer, input):
    input_array = np.array(input, dtype=np.int64)
    return computer.process(input_array)

@jitclass(spec)
class Computer:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.reset()

    def reset(self):
        self.state = self.initial_state.copy()
        self.address = 0
        self.input_address = 0
        self.relative_base = 0
        self.inputs = np.empty(0, dtype=np.int64)

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


    def get_indexes(self, mode, number_of_inputs):
        indexes = np.empty(number_of_inputs, dtype=np.int64)
        max_index = 0
        for i in range(number_of_inputs):
            mode_modulo = int((mode%(10**(i+1)))/(10**i))
            if mode_modulo == 2:
                index_to_add = self.relative_base + self.state[self.address + i + 1]
            elif mode_modulo == 1:
                index_to_add = self.address + i + 1
            elif mode_modulo > 2:
                raise Exception("not implemented")
            else:
                index_to_add = self.state[self.address + i + 1]
            indexes[i] = index_to_add
            if index_to_add > max_index:
                max_index = index_to_add
        self.check_state_length(max_index)
        return indexes

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

            if instruction == 1:
                indexes = self.get_indexes(mode, 3)
                
                self.state[indexes[2]] = self.state[indexes[1]] + self.state[indexes[0]]
                self.address += 4
            elif instruction == 2:
                indexes = self.get_indexes(mode, 3)
                
                self.state[indexes[2]] = self.state[indexes[1]] * self.state[indexes[0]]
                self.address += 4
            elif instruction == 3:
                if len(self.inputs) <= self.input_address:
                    return False, outputs
                
                indexes = self.get_indexes(mode, 1)

                self.state[indexes[0]] = self.inputs[self.input_address]
                self.input_address += 1
                self.address += 2
            elif instruction == 4:
                indexes = self.get_indexes(mode, 1)
                
                outputs.append(self.state[indexes[0]])
                
                self.address += 2
            elif instruction == 5:
                indexes = self.get_indexes(mode, 2)

                if self.state[indexes[0]] != 0:
                    self.address = self.state[indexes[1]]
                else:
                    self.address += 3
            elif instruction == 6:
                indexes = self.get_indexes(mode, 2)

                if self.state[indexes[0]] == 0:
                    self.address = self.state[indexes[1]]
                else:
                    self.address += 3
            elif instruction == 7:
                indexes = self.get_indexes(mode, 3)

                if self.state[indexes[0]] < self.state[indexes[1]]:
                    self.state[indexes[2]] = 1
                else:
                    self.state[indexes[2]] = 0

                self.address += 4
            elif instruction == 8:
                indexes = self.get_indexes(mode, 3)

                if self.state[indexes[0]] == self.state[indexes[1]]:
                    self.state[indexes[2]] = 1
                else:
                    self.state[indexes[2]] = 0

                self.address += 4            
            elif instruction == 9:
                indexes = self.get_indexes(mode, 1)

                self.relative_base += self.state[indexes[0]]
                self.address += 2


            elif instruction == 99:
                return True, outputs
            else:
                raise Exception(f"Unknown: Instruction {instruction} Address {self.address}")
            
        raise Exception("not terminated")