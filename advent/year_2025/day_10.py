from typing import Self
from advent.runner import register
from advent.utils.split_text import create_char_grid
from advent.utils.grid import Grid
from dataclasses import dataclass
import numpy as np
from scipy import linalg, optimize

def values_in_detail(detail: str):
    return [int(x) for x in detail[1:-1].split(",")]

@register(10, 2025, 2, True)
def buttons_2(text):
    totals = 0

    for line in text:
        details = line.split(" ")
        target = np.array(values_in_detail(details[-1]))

        coeffs = []
        for button in details[1:-1]:
            button_coeff = np.zeros_like(target)
            for light_index in values_in_detail(button):
                button_coeff[light_index] = 1
            coeffs.append(button_coeff)

        solution = optimize.linprog(
            c=np.ones(len(details[1:-1])),
            A_eq=np.transpose(np.array(coeffs)),
            b_eq=np.copy(target),
            integrality=1,
        )

        solution_presses = np.array([int(x) for x in solution.x])

        check_answer = np.matmul(
            np.transpose(np.array(coeffs)),
            solution_presses
        )

        if not np.array_equal(target, check_answer):
            print(solution)
            print(target)
            print(check_answer)
            raise Exception
        
        totals += int(solution.fun)

    return totals