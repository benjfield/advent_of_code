from advent.runner import register
from advent.utils.split_text import split_text, Split
from advent.utils.grid import Grid
from dataclasses import dataclass
import math
from functools import cache
from collections import defaultdict

from advent.utils.direction import Direction

from time import perf_counter

import re

from functools import partial

from advent.utils.path_finding_2 import Node, djikstra, has_final_coords_function
from dataclasses import dataclass

from numba import jit, int64, types

@dataclass
class Computer:
    a: int
    b: int
    c: int
    output: list[int]

    def combo_operand(self, literal_operand):
        match literal_operand:
            case _ if literal_operand <= 3:
                return literal_operand
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                raise NotImplementedError

    def run_instruction(self, instruction, literal_operand, instruction_pointer):        
        match instruction:
            case 0:
                self.a = self.a // (2**self.combo_operand(literal_operand))
            case 1:
                self.b = self.b ^ literal_operand
            case 2:
                self.b = self.combo_operand(literal_operand) % 8
            case 3:
                if self.a != 0:
                    return literal_operand
            case 4:
                self.b = self.b ^ self.c
            case 5:
                self.output.append(self.combo_operand(literal_operand) % 8)
            case 6:
                self.b = self.a // (2**self.combo_operand(literal_operand))
            case 7:
                self.c = self.a // (2**self.combo_operand(literal_operand))
        
        return instruction_pointer + 2           

    def run(self, instructions: list[int]):
        instruction_pointer = 0
        while instruction_pointer < len(instructions) - 1:
            
            instruction_pointer = self.run_instruction(
                instructions[instruction_pointer],
                instructions[instruction_pointer + 1],
                instruction_pointer)
            
        return self.output
    
    def reset(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.output.clear()

    def find_expected(self, instructions: tuple[int]):
        instruction_pointer = 0
        while instruction_pointer < len(instructions) - 1:
            added_output = False
            if instructions[instruction_pointer] == 5:
                added_output = True
            
            instruction_pointer = self.run_instruction(
                instructions[instruction_pointer],
                instructions[instruction_pointer + 1],
                instruction_pointer)
            
            if added_output:
                if self.output[-1] != instructions[len(self.output) - 1]:
                    return False
                elif len(self.output) == len(instructions):
                    return True
            
        return False

@jit
def run_program(a):
    a_mod_8 = a % 8
    return (a_mod_8 ^ 5) ^ (a // (2 ** (a_mod_8 ^ 1) )) % 8, a // 8

@jit
def find_expected(instructions: tuple[int], a: int):
    for i in range(len(instructions)):
        if a < 0:
            return False
        
        output, a = run_program(a)

        if output != instructions[i]:
            return False

    return True

@jit
def find_a(instructions: tuple[int]):
    a = 8 ** len(instructions)
    while True:
        found_answer = find_expected(instructions, a)

        if found_answer:
            return a

        a += 1

def find_result_recursive(instructions, index, a):
    for i in range(8):
        potential_a = a * 8 + i
        output, _ = run_program(potential_a)
        if output == instructions[index]:
            if index == 0:
                return True, potential_a
            else:
                found_answer, answer = find_result_recursive(instructions, index - 1, potential_a)
                if found_answer:
                    return True, answer
            
    return False, 0

        
def func_1(text):
    lines = text.split("\n")
    a = int(lines[0].split(" ")[-1])
    b = int(lines[1].split(" ")[-1])
    c = int(lines[2].split(" ")[-1])

    instructions = [int(x) for x in lines[4].split(" ")[-1].split(",")]

    output = Computer(a, b, c, []).run(instructions)

    return ",".join([str(x) for x in output])
        
@register(17, 2024, 1)
def func_1_1(text):
    lines = text.split("\n")
    a = int(lines[0].split(" ")[-1])
    output = []

    while a > 0:
        output_int, a = run_program(a)
        output.append(output_int)

    return ",".join([str(x) for x in output])

def func_2(text):
    lines = text.split("\n")
    instructions = tuple(int(x) for x in lines[4].split(" ")[-1].split(","))
    found_answer = False
    a = 0
    computer = Computer(0, 0, 0, [])
    while True:
        if a % 10000 == 0:
            print(a)
        computer.reset(a)
        found_answer = computer.find_expected(instructions)

        if found_answer:
            return a

        a += 1
    
@register(17, 2024, 2)
def func_2_1(text):
    lines = text.split("\n")
    instructions = tuple(int(x) for x in lines[4].split(" ")[-1].split(","))
    found_answer, answer = find_result_recursive(instructions, len(instructions) - 1, 0)

    if not found_answer:
        print("Here")
        raise Exception

    return answer