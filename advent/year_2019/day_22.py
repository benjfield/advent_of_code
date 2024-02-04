from advent.runner import register
import re
import math
from numba import njit 

class Deck:
    def __init__(self, size=10007):
        self.cards = [ x for x in range(size)]

    def new_stack(self):
        self.cards.reverse()

    def cut(self, index):
        self.cards = self.cards[index:] + self.cards[:index]

    def deal(self, increment):
        i = 0
        j = 0
        old_deck = self.cards.copy()
        for i, value in enumerate(old_deck):
            destination = (i * increment)%len(self.cards)
            self.cards[destination] = value

    def process_commands(self, commands):
        for command in commands:
            match command["command"]:
                case "deal into new stack":
                    self.new_stack()
                case "cut":
                    self.cut(command["arg"])
                case "deal with increment":
                    self.deal(command["arg"])

    def run_commands(self, text):
        commands = []
        for command_text in text.split("\n"):
            command_match = re.match(r"([^0-9\-]+)([-\d]*)", command_text)
            parsed_command = {
                "command": command_match.group(1).strip(),
            }
            if command_match.group(2) is not None and command_match.group(2) != "":
                parsed_command["arg"] = int(command_match.group(2))
            commands.append(parsed_command)
        
        self.process_commands(commands)
def get_commands(text):
    commands = []
    for command_text in text.split("\n"):
        command_match = re.match(r"([^0-9\-]+)([-\d]*)", command_text)
        parsed_command = {
            "command": command_match.group(1).strip(),
        }
        if command_match.group(2) is not None and command_match.group(2) != "":
            parsed_command["arg"] = int(command_match.group(2))
        commands.append(parsed_command)
    
    return commands

#multiplier, addition
def single_card_new_stack_compilable(length):
    return -1, (length - 1)

def single_card_cut_compilable(cut_index):
    return 1, -cut_index

def single_card_deal_compilable(increment):
    return increment, 0

def compile_commands(length, commands):
    multiplier = 1
    addition = 0
    for command in commands:
        match command["command"]:
            case "deal into new stack":
                new_multiplier, new_addition = single_card_new_stack_compilable(length)
            case "cut":
                new_multiplier, new_addition = single_card_cut_compilable(command["arg"])
            case "deal with increment":
                new_multiplier, new_addition = single_card_deal_compilable(command["arg"]) 

        multiplier = multiplier * new_multiplier
        addition = addition * new_multiplier + new_addition

    return multiplier, addition

def gcdExtended(a, b):
    global x, y
 
    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b
 
    # To store results of recursive call
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd
 
def modInverse(A, M):
    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
    else:
        # m is added to handle negative x
        res = (x % M + M) % M
        return res
    
def single_card_cut_compilable_reverse(cut_index):
    return 1, cut_index

def single_card_deal_compilable_reverse(increment, length):
    multiplier = modInverse(increment, length)
    return multiplier, 0

def compile_commands_reverse(length, commands):
    multiplier = 1
    addition = 0
    for command in commands:
        match command["command"]:
            case "deal into new stack":
                new_multiplier, new_addition = single_card_new_stack_compilable(length)
            case "cut":
                new_multiplier, new_addition = single_card_cut_compilable_reverse(command["arg"])
            case "deal with increment":
                new_multiplier, new_addition = single_card_deal_compilable_reverse(command["arg"], length) 

        multiplier = multiplier * new_multiplier
        addition = addition * new_multiplier + new_addition

    return multiplier, addition

@register(22, 2019, 1)
def shuffle_1(text, size=10007, card_to_search=2019):
    commands = get_commands(text)
    multiplier, addition = compile_commands(size, commands)

    return ((multiplier * card_to_search) + addition)%size

def compile_a_number_of_times(multiplier, addition, size, times=101741582076661):
    binary_compilation_cache = {
        1: {
            "multiplier": multiplier % size,
            "addition": addition % size
        }
    }

    i = 2
    while i < times:
        addition = (addition * (multiplier + 1)) % size
        multiplier = (multiplier * multiplier) % size

        binary_compilation_cache[i] = {
            "multiplier": multiplier,
            "addition" : addition
        }

        i = i * 2

    powers_of_2 = list(binary_compilation_cache.keys())
    powers_of_2.sort()

    multiplier = 1
    addition = 0
    while times > 0:
        for i, power_of_2 in enumerate(reversed(powers_of_2)):
            if power_of_2 <= times:
                power_of_2_to_use = power_of_2
                index = (i+1) * -1
                powers_of_2 = powers_of_2[:index]
                break
        multiplier = (multiplier * binary_compilation_cache[power_of_2_to_use]["multiplier"]) % size
        addition = (addition * binary_compilation_cache[power_of_2_to_use]["multiplier"] + binary_compilation_cache[power_of_2_to_use]["addition"]) %size

        times -= power_of_2_to_use
    return multiplier, addition   

@register(22, 2019, 2)
def shuffle_2(text, size=119315717514047, index_to_reverse=2020, times_to_run=101741582076661):
    commands = get_commands(text)

    commands.reverse()

    reverse_multiplier, reverse_addition = compile_commands_reverse(size, commands)
    reverse_multiplier, reverse_addition = compile_a_number_of_times(reverse_multiplier, reverse_addition, size, times_to_run) 

    return ((reverse_multiplier * index_to_reverse) + reverse_addition)%size
        