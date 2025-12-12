from advent.runner import register
import numpy as np
from scipy import optimize
import math

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

        c = np.ones(len(coeffs), dtype=int)
        a = np.transpose(np.array(coeffs))
        b = target

        solution = optimize.linprog(
            c=c,
            A_eq=a,
            b_eq=b,
            integrality=1,
        )
        
        totals += round(solution.fun)

    return totals