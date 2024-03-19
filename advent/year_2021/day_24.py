from advent.runner import register
class UncompiledNumber:
    def __init__(
        self,
        is_int,
        int_value = 0,
        model_index = 0):
        self.is_int = is_int
        self.int_value = int_value
        self.string_value = f"model_number[{model_index}]"
        self.set_to_0()
    
    def __str__(self):
        if self.is_int:
            return str(self.int_value)
        else:
            if self.multiplier != 1:
                string = f"{str(self.multiplier)} * {self.string_value}"
            else:
                string = self.string_value

            if self.additive != 0:
                string = f"{string} + {str(self.additive)}"
            else:
                string = string

            if self.modulo != 0:
                string = f"({string}) % {str(self.modulo)}"
            else:
                string = string

            return string

    def set_to_0(self):
        self.additive = 0
        self.multiplier = 1
        self.modulo = 0

    def copy_from_other(
        self, 
        other):
        self.is_int = False
        self.string_value = other.string_value
        self.additive = other.additive
        self.multiplier = self.multiplier
        self.modulo = other.modulo

    def addition(
        self,
        other
    ):
        if self.is_int:
            if other.is_int:
                self.int_value += other.int_value
            else:
                if other.modulo != 0:
                    self.string_value = f"{other}"
                    self.is_int == False
                    self.set_to_0()
                    self.additive = self.int_value
                else:
                    self.copy_from_other(other)
                    self.additive += self.int_value
        else:
            if other.is_int:
                if self.modulo != 0:
                    self.string_value = f"{self}"
                    self.set_to_0()
                    self.additive = other.int_value
                else:
                    self.additive += other.int_value
            else:
                if self.modulo != 0 or other.modulo != 0:
                    self.string_value = f"{self} + {other}"
                    self.set_to_0()
                else:
                    if other.multiplier != 1:
                        self.string_value = f"{self.string_value} + {other.multiplier} * {other.string_value}"
                    else:
                        self.string_value = f"{self.string_value} + {other.string_value}"
                    self.additive += other.additive

    def multiply(
        self,
        other
    ):
        if self.is_int:
            if other.is_int:
                self.int_value *= other.int_value
            else:
                if self.int_value == 0:
                    self.int_value = 0
                    self.is_int = True
                    self.set_to_0()

                elif other.modulo != 0:
                    self.string_value = f"{other}"
                    self.is_int == False
                    self.set_to_0()
                    self.multiplier = self.int_value
                else:
                    self.copy_from_other(other)
                    self.multiplier *= self.int_value
        else:
            if other.is_int:
                if other.int_value == 0:
                    self.int_value = 0
                    self.is_int = True
                    self.set_to_0()
                elif self.modulo != 0:
                    self.string_value = f"{self}"
                    self.set_to_0()
                    self.multiplier = other.int_value
                else:
                    self.additive *= other.int_value
                    self.multiplier *= other.int_value
            else:
                if self.modulo != 0 or other.modulo != 0 or self.additive != 0 or other.additive != 0:
                    self.string_value = f"({self}) * ({other})"
                    self.set_to_0()
                else:
                    self.string_value = f"({self.string_value}) * ({other.string_value})"
                    self.multiplier *= other.multiplier

    def divide(
        self,
        other
    ):
        if self.is_int:
            if other.is_int:
                self.int_value = int(self.int_value / other.int_value)
            else:
                if self.int_value % other.multiplier == 0 and other.modulo == 0:
                    self.copy_from_other(other)
                    self.multiplier = int(self.int_value / other.multiplier)
                else:
                    self.string_value = f"int({self} / ({other}))"
                    self.is_int = False
        else:
            if other.is_int:
                if self.multiplier % other.int_value == 0 and self.additive % other.int_value == 0  and self.modulo == 0:
                    self.additive = int(self.additive / other.int_value)
                    self.multiplier = int(self.multiplier / other.int_value)
                else:
                    self.string_value = f"int(({self}) / {other})"
                    self.set_to_0()
            else:
                self.string_value = f"int(({self}) / ({other}))"
                self.set_to_0()

    def modulus(
        self,
        other
    ):
        if self.is_int:
            if other.is_int:
                self.int_value = self.int_value % other.int_value
            else:
                if self.int_value == 0:
                    pass
                else:
                    self.string_value = f"{self} % {other}"
                    self.is_int = False
                    self.set_to_0()
        else:
            if other.is_int:
                if self.modulo != 0:
                    self.string_value = f"{self}"
                    self.set_to_0()
                    self.modulo = other.int_value
                else:
                    self.modulo = other.int_value
            else:
                self.string_value = f"{self} * {other}"
                self.set_to_0()

    def check_equality(
        self,
        other,
        conditions
    ):
        if self.is_int and other.is_int:
            self.int_value = int(self.int_value == other.int_value)
        elif (self.definitely_more_than_10() and other.definitely_less_than_10()) or (self.definitely_less_than_10() and other.definitely_more_than_10()):
            self.is_int = True
            self.int_value = 0
            self.set_to_0()
        elif (self.definitely_positive() and other.definitely_negative()) or (self.definitely_negative() and other.definitely_positive()):
            self.is_int = True
            self.int_value = 0
            self.set_to_0()
        elif not self.is_int and not other.is_int:
            if self.string_value == other.string_value and self.additive == other.additive and self.multiplier == other.multiplier and self.modulo == other.modulo:
                self.is_int = True
                self.int_value = 1
                self.set_to_0()
            else:
                condition_string = f"parsed_conditions[{len(conditions)}]"
                conditions[condition_string] = f"int({self} == {other})"
                self.string_value = condition_string
                self.is_int = False
                self.set_to_0()
        else:
            condition_string = f"parsed_conditions[{len(conditions)}]"
            conditions[condition_string] = f"int({self} == {other})"
            self.string_value = condition_string
            self.is_int = False
            self.set_to_0()

    def definitely_more_than_10(self):
        if (not self.is_int and self.modulo == 0 and self.additive >= 10) or (self.is_int and self.int_value >= 10):
            return True
        else:
            return False
        
    def definitely_less_than_10(self):
        if not self.is_int:
            if self.modulo != 0 and self.modulo < 10:
                return True
            if self.string_value[0:12] == "model_number" and len(self.string_value) <= 16:
                if self.additive == 0 and self.multiplier == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.int_value < 10:
                return True
            else:
                return False
        
    def definitely_negative(self):
        if not self.is_int:
            if self.string_value[0:12] == "model_number" and len(self.string_value) <= 16:
                if self.additive == 0 and self.multiplier < 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.int_value < 0:
                return True
            else:
                return False
        
    def definitely_positive(self):
        if not self.is_int:
            if self.string_value[0:12] == "model_number" and len(self.string_value) <= 16:
                if self.additive >= 0 and self.multiplier >= 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.int_value >= 0:
                return True
            else:
                return False
            
def process_rules(text):
    split_text = text.split("\n")[:72]

    data = {
        "w": UncompiledNumber(True, 0),
        "x": UncompiledNumber(True, 0),
        "y": UncompiledNumber(True, 0),
        "z": UncompiledNumber(True, 0),
    }

    conditions = {}

    model_index = 0
    for i, line in enumerate(split_text):
        instruction = line.split(" ")

        print(f"{i}: {line}")
        if len(instruction) == 3:
            if instruction[2] in data.keys():
                second_variable = data[instruction[2]]
            else:
                second_variable = UncompiledNumber(True, int(instruction[2])) 
        match instruction[0]:
            case "inp":
                data[instruction[1]] = UncompiledNumber(False, 0, model_index)
                model_index += 1
            case "add":
                data[instruction[1]].addition(second_variable)
            case "mul":
                data[instruction[1]].multiply(second_variable)
            case "div":
                data[instruction[1]].divide(second_variable)
            case "mod":
                data[instruction[1]].modulus(second_variable)
            case "eql":
                data[instruction[1]].check_equality(second_variable, conditions)

        print("w", data["w"])
        print("x", data["x"])
        print("y", data["y"])
        print("z", data["z"])
        print(" ")
        
    return data, conditions

def monad_1(text):
    rules, conditions = process_rules(text)

    rules_string = str(rules["z"])

    models = {}

    for model_index in range(14): 
        model_string = f"model_number[{model_index}]"
        models[model_string] = rules_string.count(model_string)

    print(" ")

    print(conditions)

    print(" ")

    print(models)

    print(" ")

    return str(rules["z"])

@register(24, 2021, 1)
def monad_1_check(text):
    model_number = 13579246899999
    print(check_number(text, model_number))
    print(process_rules_naive(text, model_number))
    return check_number(text, model_number) == process_rules_naive(text, model_number)


def check_number(text, model_number):
    rules, conditions = process_rules(text)

    model_number_string = str(model_number)

    model_number = []

    for char in model_number_string:
        model_number.append(int(char))

    rules_string = str(rules["z"])

    parsed_conditions = {}

    for condition_index in range(len(conditions)):
        condition_name = f"parsed_conditions[{condition_index}]"
        condition_value = eval(conditions[condition_name])
        parsed_conditions[condition_index] = condition_value
    
    print(conditions)
    print(parsed_conditions)
    print(eval(rules_string))
    return eval(rules_string)

def process_rules_naive(text, model_number):
    split_text = text.split("\n")[:72]

    data = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    model_number_string = str(model_number)

    model_index = 0
    for i, line in enumerate(split_text):
        instruction = line.split(" ")

        if len(instruction) == 3:
            if instruction[2] in data.keys():
                second_variable = data[instruction[2]]
            else:
                second_variable = int(instruction[2])
        match instruction[0]:
            case "inp":
                data[instruction[1]] = int(model_number_string[model_index])
                model_index += 1
            case "add":
                data[instruction[1]] += second_variable
            case "mul":
                data[instruction[1]] *= second_variable
            case "div":
                data[instruction[1]] = int(data[instruction[1]]/second_variable)
            case "mod":
                data[instruction[1]] = data[instruction[1]] % second_variable
            case "eql":
                if data[instruction[1]] == second_variable:
                    data[instruction[1]] = 1
                else:
                    data[instruction[1]] = 0
       
    print(data["z"]) 
    return data["z"]

            

