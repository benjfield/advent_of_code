from advent.runner import register
class MonkeyNumber:
    def __init__(
        self,
        name,
        number=None,
        dependent_1_name=None,
        dependent_2_name=None,
        dependent_symbol = None
    ):
        self.name = name
        self.number = number
        self.dependent_1_name = dependent_1_name
        self.dependent_1 = None
        self.dependent_2_name = dependent_2_name
        self.dependent_2 = None
        self.dependent_symbol = dependent_symbol
        self.upstream = []

        if self.name == "humn":
            self.human_dependent = True

    def populate_dependents(
        self,
        monkey_numbers
    ):
        if self.dependent_1_name is not None:
            self.dependent_1 = monkey_numbers[self.dependent_1_name]
            self.dependent_1.upstream.append(self)

        if self.dependent_2_name is not None:
            self.dependent_2 = monkey_numbers[self.dependent_2_name]
            self.dependent_2.upstream.append(self)
        
    def process_number(
        self
    ):
        
        if self.number is None: 
            if (self.dependent_1.number is None or self.dependent_2.number is None):
                return None
            else:
                match self.dependent_symbol:
                    case "+":
                        self.number = self.dependent_1.number + self.dependent_2.number
                    case "-":
                        self.number = self.dependent_1.number - self.dependent_2.number
                    case "*":
                        self.number = self.dependent_1.number * self.dependent_2.number
                    case "/":
                        self.number = self.dependent_1.number // self.dependent_2.number
                    case _:
                        raise Exception
        for upstream_monkey in self.upstream:
            upstream_monkey.process_number()

    def __str__(self):
        if self.dependent_1 is None:
            return f"{self.name}: {self.number} -> {[x.name for x in self.upstream]}"
        elif self.number is not None:
            return f"{self.name}: ({self.number}) {self.dependent_1.name} {self.dependent_symbol} {self.dependent_2.name} -> {[x.name for x in self.upstream]}"
        else:
            return f"{self.name}: {self.dependent_1.name} {self.dependent_symbol} {self.dependent_2.name} -> {[x.name for x in self.upstream]}"

def parse_text(split_text, class_to_use=MonkeyNumber):
    monkey_numbers = {}
    for line in split_text:
        monkey_details = {}
        split_by_colon = line.split(": ")
        monkey_name = split_by_colon[0]
        monkey_details["name"] = split_by_colon[0]
        split_formula = split_by_colon[1].split(" ")
        if len(split_formula) == 1:
            monkey_details["number"] = int(split_formula[0])
        else:
            monkey_details["dependent_1_name"] = split_formula[0]
            monkey_details["dependent_symbol"] = split_formula[1]
            monkey_details["dependent_2_name"] = split_formula[2]

        monkey_number = class_to_use(**monkey_details)

        monkey_numbers[monkey_name] = monkey_number

    return monkey_numbers

@register(21, 2022, 1, True)
def monkey_math_1(split_text):
    monkey_numbers = parse_text(split_text)

    for monkey_number in monkey_numbers.values():
        monkey_number.populate_dependents(monkey_numbers)

    for monkey_number in monkey_numbers.values():
        monkey_number.process_number()

    return monkey_numbers["root"].number

class MonkeyNumberHuman(MonkeyNumber):
    def __init__(
        self,
        name,
        number=None,
        dependent_1_name=None,
        dependent_2_name=None,
        dependent_symbol = None
    ):
        super().__init__(
            name,
            number,
            dependent_1_name,
            dependent_2_name,
            dependent_symbol
        )

        self.human_dependent = False

    def process_human_dependency(
        self
    ):
        
        self.human_dependent = True
        for upstream_monkey in self.upstream:
            upstream_monkey.process_human_dependency()

    def restructure_number(
        self
    ):
        if self.name == "root":
            if self.dependent_1.human_dependent:
                self.upstream.append(self.dependent_1)
            else:
                self.upstream.append(self.dependent_2)
        elif self.name == "humn":
            self.upstream = []
        elif self.human_dependent:
            if self.dependent_1.human_dependent:
                old_dependent_1 = self.dependent_1
                self.dependent_1 = self.upstream[0]
                self.upstream = [old_dependent_1]
                match self.dependent_symbol:
                    case "+":
                        self.dependent_symbol = "-"
                    case "-":
                        self.dependent_symbol = "+"
                    case "*":
                        self.dependent_symbol = "/"
                    case "/":
                        self.dependent_symbol = "*"
                    case _:
                        raise Exception
            else:
                match self.dependent_symbol:
                    case "+":
                        old_dependent_2 = self.dependent_2
                        self.dependent_2 = self.dependent_1
                        self.dependent_1 = self.upstream[0]
                        self.upstream = [old_dependent_2]
                        self.dependent_symbol = "-"
                    case "-":
                        old_dependent_2 = self.dependent_2
                        self.dependent_2 = self.upstream[0]
                        self.upstream = [old_dependent_2]
                    case "*":
                        old_dependent_2 = self.dependent_2
                        self.dependent_2 = self.dependent_1
                        self.dependent_1 = self.upstream[0]
                        self.upstream = [old_dependent_2]
                        self.dependent_symbol = "/"
                    case "/":
                        old_dependent_2 = self.dependent_2
                        self.dependent_2 = self.upstream[0]
                        self.upstream = [old_dependent_2]
                    case _:
                        raise Exception

                
    def process_number(
        self
    ):
        if self.name == "humn":
            return None
        elif self.name == "root":
            if (self.dependent_1.number is None and self.dependent_2.number is None):
                return None
            elif self.number is None:
                if self.dependent_1.number is not None:
                    self.number = self.dependent_1.number
                else:
                    self.number = self.dependent_2.number
        elif self.number is None: 
            if (self.dependent_1.number is None or self.dependent_2.number is None):
                return None
            else:
                match self.dependent_symbol:
                    case "+":
                        self.number = self.dependent_1.number + self.dependent_2.number
                    case "-":
                        self.number = self.dependent_1.number - self.dependent_2.number
                    case "*":
                        self.number = self.dependent_1.number * self.dependent_2.number
                    case "/":
                        self.number = self.dependent_1.number // self.dependent_2.number
                    case _:
                        raise Exception
        for upstream_monkey in self.upstream:
            upstream_monkey.process_number()

@register(21, 2022, 2, True)
def monkey_math_2(split_text):
    monkey_numbers = parse_text(split_text, MonkeyNumberHuman)

    for monkey_number in monkey_numbers.values():
        monkey_number.populate_dependents(monkey_numbers)

    monkey_numbers["humn"].process_human_dependency()

    final_number = monkey_numbers["humn"].upstream[0]
    monkey_numbers["humn"].number = None

    for monkey_number in monkey_numbers.values():
        monkey_number.restructure_number()

    for monkey_number in monkey_numbers.values():
        monkey_number.process_number()

    return final_number.number

                    
                    



