class Computer:
    def __init__(self, state):
        self.state = [ int(x) for x in state.split(",") ]
        self.process_index = 0

    def get_indexes(self, mode, number_of_inputs, address):
        indexes = []
        for i in range(number_of_inputs):
            if mode & 2**i:
                indexes.append(address + i + 1)
            else:
                indexes.append(self.state[address + i + 1])
        return indexes

    def process(self, input = 0):
        address = 0
        
        outputs = []

        while address < len(self.state):
            instruction_string = str(self.state[address])

            instruction = int(instruction_string[-2:])

            mode_string = instruction_string[:-2]
            if mode_string == "":
                mode = 0
            else:
                mode = int(mode_string, 2)

            if instruction == 1:
                indexes = self.get_indexes(mode, 3, address)

                self.state[indexes[2]] = self.state[indexes[1]] + self.state[indexes[0]]
                address += 4
            elif instruction == 2:
                indexes = self.get_indexes(mode, 3, address)

                self.state[indexes[2]] = self.state[indexes[1]] * self.state[indexes[0]]
                address += 4
            elif instruction == 3:
                indexes = self.get_indexes(mode, 1, address)

                self.state[indexes[0]] = input
                address += 2
            elif instruction == 4:
                indexes = self.get_indexes(mode, 1, address)

                outputs.append(self.state[indexes[0]])
                address += 2
            elif instruction == 5:
                indexes = self.get_indexes(mode, 2, address)

                if self.state[indexes[0]] != 0:
                    address = self.state[indexes[1]]
                else:
                    address += 3
            elif instruction == 6:
                indexes = self.get_indexes(mode, 2, address)

                if self.state[indexes[0]] == 0:
                    address = self.state[indexes[1]]
                else:
                    address += 3
            elif instruction == 7:
                indexes = self.get_indexes(mode, 3, address)

                if self.state[indexes[0]] < self.state[indexes[1]]:
                    self.state[indexes[2]] = 1
                else:
                    self.state[indexes[2]] = 0

                address += 4
            elif instruction == 8:
                indexes = self.get_indexes(mode, 3, address)

                if self.state[indexes[0]] == self.state[indexes[1]]:
                    self.state[indexes[2]] = 1
                else:
                    self.state[indexes[2]] = 0

                address += 4


            elif instruction == 99:
                return outputs
            else:
                raise Exception(f"Unknown: Instruction {instruction} Address {address}")