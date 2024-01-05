import numpy as np
import re
from aocd import get_data
def hail_1(text, min_boundary = 7, max_boundary = 27):
    hail_course = []

    for line in text.split("\n"):
        parse_hail = re.search(r"([-\d]+),\s+([-\d]+),\s+([-\d]+) @\s+([-\d]+),\s+([-\d]+),\s+([-\d]+)", line)

        hail_course.append({
            "position": [int(parse_hail.group(1)), int(parse_hail.group(2))],
            "direction":[int(parse_hail.group(4)), int(parse_hail.group(5))]
        })
    #print(hail_course)
    
    valid_count = 0
    for i in range(len(hail_course)):
        for j in range(i + 1, len(hail_course)):
            a = hail_course[i]
            b = hail_course[j]

            cross = np.cross(a["direction"], b["direction"])

            if cross == 0:
                #print(f"{a} {b} parallel")
                continue

            q_minus_p = np.subtract(b["position"], a["position"])

            q_minus_p_cross_s = np.cross(q_minus_p, b["direction"])

            time_1 = np.divide(q_minus_p_cross_s, cross)

            if time_1 < 0:
                #print(f"{a} {b} in past for a {time_1}")
                continue

            intersection = np.add(a["position"], np.multiply(a["direction"], time_1))

            valid_intersect = True
            for value in intersection:
                if value < min_boundary or value > max_boundary:
                    valid_intersect = False
                    break
            
            if not valid_intersect:
                #print(f"{a} {b} intersect out of bounds {intersection}")
                continue

            q_minus_p_cross_r = np.cross(q_minus_p, a["direction"])

            time_2 = np.divide(q_minus_p_cross_r, cross)

            if time_2 < 0:
                #print(f"{a} {b} in past for b {time_2}")
                continue

            #print(f"{a} {b} valid")
            valid_count += 1
    
    return valid_count

def hail_2(text):
    hail_course = []

    for line in text.split("\n"):
        parse_hail = re.search(r"([-\d]+),\s+([-\d]+),\s+([-\d]+) @\s+([-\d]+),\s+([-\d]+),\s+([-\d]+)", line)

        hail_course.append({
            "x": int(parse_hail.group(1)),
            "dx": int(parse_hail.group(4)),
            "y": int(parse_hail.group(2)),
            "dy": int(parse_hail.group(5)),
            "z": int(parse_hail.group(3)),
            "dz": int(parse_hail.group(6)),
        })

    hailstones = [[0, 1], [1, 2]]

    coeff_matrix = []
    dependent_matrix = []


    for hail_1_index, hail_2_index in hailstones:
        hail_1 = hail_course[hail_1_index]
        hail_2 = hail_course[hail_2_index]

        coeff_matrix.append([hail_2["dy"] - hail_1["dy"], hail_1["y"] - hail_2["y"], hail_1["dx"] - hail_2["dx"], hail_2["x"] - hail_1["x"], 0, 0])
        dependent_matrix.append(hail_2["x"] * hail_2["dy"] + hail_1["dx"] * hail_1 ["y"] - hail_1["x"] * hail_1 ["dy"] - hail_2["y"] * hail_2["dx"])
        coeff_matrix.append([hail_2["dz"] - hail_1["dz"], hail_1["z"] - hail_2["z"], 0, 0, hail_1["dx"] - hail_2["dx"], hail_2["x"] - hail_1["x"], ])
        dependent_matrix.append(hail_2["x"] * hail_2["dz"] + hail_1["dx"] * hail_1 ["z"] - hail_1["x"] * hail_1 ["dz"] - hail_2["z"] * hail_2["dx"])
        coeff_matrix.append([0, 0, hail_2["dz"] - hail_1["dz"], hail_1["z"] - hail_2["z"], hail_1["dy"] - hail_2["dy"], hail_2["y"] - hail_1["y"], ])
        dependent_matrix.append(hail_2["y"] * hail_2["dz"] + hail_1["dy"] * hail_1 ["z"] - hail_1["y"] * hail_1 ["dz"] - hail_2["z"] * hail_2["dy"])

    numpy_coeff_matrix = np.array(coeff_matrix)
    numpy_dependent_matrix = np.array(dependent_matrix)

    solution = np.linalg.solve(numpy_coeff_matrix, numpy_dependent_matrix)

    return solution[0] + solution[2] + solution[4]


hail_text = get_data(day=24, year=2023)
print(hail_2(hail_text))    