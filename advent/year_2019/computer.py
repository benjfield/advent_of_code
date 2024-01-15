class Computer:
    def __init__(self, initial_state):
        self.initial_state = [ int(x) for x in initial_state.split(",") ]
        self.reset()

    def reset(self):
        self.state = self.initial_state.copy()
        self.address = 0
        self.input_address = 0
        self.relative_base = 0
        self.inputs = []

    def get_indexes(self, mode, number_of_inputs):
        indexes = []
        for i in range(number_of_inputs):
            mode_modulo = int((mode%(10**(i+1)))/(10**i))
            if mode_modulo == 2:
                indexes.append(self.relative_base + self.state[self.address + i + 1])
            elif mode_modulo == 1:
                indexes.append(self.address + i + 1)
            elif mode_modulo > 2:
                raise Exception("not implemented")
            else:
                indexes.append(self.state[self.address + i + 1])

        self.check_state_length(indexes)
        return indexes

    def check_state_length(self, indexes):
        max_length = max(indexes)
        for i in range(max(max_length - len(self.state) + 1, 0)):
            self.state.append(0)

    def process(self, input = []):   
        self.inputs += input
        outputs = []

        while self.address < len(self.state):
            #print(f"address {self.address} state {self.state} input {self.inputs} input_address {self.input_address}")
            instruction_string = str(self.state[self.address])

            instruction = int(instruction_string[-2:])

            mode_string = instruction_string[:-2]
            if mode_string == "":
                mode = 0
            else:
                mode = int(mode_string)

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