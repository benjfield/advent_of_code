
from enum import Enum
from collections import deque
from advent.runner import register
import re

class InspectionOperation(Enum):
    SQUARE = 1
    ADD = 2
    MUL = 3

class Monkey:
    def __init__(
        self,
        items,
        operation,
        test_level,
        true_monkey_id,
        false_monkey_id
        ):
        self.items = deque(items)
        if operation == "old * old":
            #Neater to store a func?
            self.operation_enum = InspectionOperation.SQUARE
        else:
            split_operation = operation.split(" ")

            if split_operation[1] == "+":
                self.operation_enum = InspectionOperation.ADD
            else:
                self.operation_enum = InspectionOperation.MUL

            self.operation_value = int(split_operation[2])
        self.test_level = test_level
        self.true_monkey_ids = true_monkey_id
        self.false_monkey_id = false_monkey_id
        self.inspect_count = 0

    def populate_monkeys(self, monkeys):
        self.true_monkey = monkeys[self.true_monkey_ids]
        self.false_monkey = monkeys[self.false_monkey_id]

    def inspect_and_throw_all(self, divisor=3):
        while len(self.items) > 0:
            self.inspect_and_throw(divisor)

    def inspect_and_throw(self, divisor=3):
        if len(self.items) > 0:
            object_to_throw = self.items.popleft()
            
            self.inspect_count += 1

            match self.operation_enum:
                case InspectionOperation.SQUARE:
                    object_to_throw *= object_to_throw
                case InspectionOperation.ADD:
                    object_to_throw += self.operation_value
                case InspectionOperation.MUL:
                    object_to_throw *= self.operation_value
                case _:
                    raise Exception

            object_to_throw = object_to_throw // divisor

            if object_to_throw % self.test_level == 0:
                self.true_monkey.items.append(object_to_throw)
            else:
                self.false_monkey.items.append(object_to_throw)

    def inspect_and_throw_all_2(self, divisor=3):
        while len(self.items) > 0:
            self.inspect_and_throw_2(divisor)

    def inspect_and_throw_2(self, divisor=3):
        if len(self.items) > 0:
            object_to_throw = self.items.popleft()
            
            self.inspect_count += 1

            match self.operation_enum:
                case InspectionOperation.SQUARE:
                    object_to_throw *= object_to_throw
                case InspectionOperation.ADD:
                    object_to_throw += self.operation_value
                case InspectionOperation.MUL:
                    object_to_throw *= self.operation_value
                case _:
                    raise Exception

            object_to_throw = object_to_throw % divisor

            if object_to_throw % self.test_level == 0:
                self.true_monkey.items.append(object_to_throw)
            else:
                self.false_monkey.items.append(object_to_throw)

def get_monkey_args(split_text):
    all_monkey_args = []

    for i in range(0, len(split_text), 7):
        monkey_args = {}
        
        starting_items_parse = re.search(r"  Starting items: (.*)", split_text[i + 1])
        monkey_args["items"] = [int(x) for x in starting_items_parse.group(1).split(", ")]
        
        operation_parse = re.search(r"  Operation: new = (.*)", split_text[i + 2])
        monkey_args["operation"] = operation_parse.group(1)

        test_parse = re.search(r"  Test: divisible by (\d+)", split_text[i + 3])
        monkey_args["test_level"] = int(test_parse.group(1))
        
        true_monkey_parse = re.search(r"    If true: throw to monkey (\d+)", split_text[i + 4])
        monkey_args["true_monkey_id"] = int(true_monkey_parse.group(1))

        false_monkey_parse = re.search(r"    If false: throw to monkey (\d+)", split_text[i + 5])
        monkey_args["false_monkey_id"] = int(false_monkey_parse.group(1))
                
        all_monkey_args.append(monkey_args)
    
    return all_monkey_args

@register(11, 2022, 1, True)
def monkey_in_the_middle_1(split_text):
    all_monkey_args = get_monkey_args(split_text)

    monkeys = []
    for monkey_args in all_monkey_args:
        monkey = Monkey(**monkey_args)
        monkeys.append(monkey)

    for monkey in monkeys:
        monkey.populate_monkeys(monkeys)

    for i in range(20):
        for monkey in monkeys:
            monkey.inspect_and_throw_all()

    inspect_counts = []
    for monkey in monkeys:
        inspect_counts.append(monkey.inspect_count)

    inspect_counts.sort(reverse=True)

    return inspect_counts[0] * inspect_counts[1]

@register(11, 2022, 2, True)
def monkey_in_the_middle_2(split_text):
    all_monkey_args = get_monkey_args(split_text)

    divisor = 1

    monkeys = []
    for monkey_args in all_monkey_args:
        monkey = Monkey(**monkey_args)
        monkeys.append(monkey)
        divisor *= monkey.test_level

    divisor *= divisor

    for monkey in monkeys:
        monkey.populate_monkeys(monkeys)

    for i in range(10000):
        for monkey in monkeys:
            monkey.inspect_and_throw_all_2(divisor)

    inspect_counts = []
    for monkey in monkeys:
        inspect_counts.append(monkey.inspect_count)

    inspect_counts.sort(reverse=True)

    return inspect_counts[0] * inspect_counts[1]