import re
import itertools
from advent.runner import register

class FoundBeaconMatch(Exception):
    pass

@register(19, 2021, 1)
def scanners_1(text):
    scanners_and_beacons = []
    for line in text.split("\n"):
        if len(line) == 0:
            pass
        elif line[0:3] == "---":
            scanners_and_beacons.append(set())
        else:
            parsed = re.match(r"(-{0,1}\d+),(-{0,1}\d+),(-{0,1}\d+)", line)

            scanners_and_beacons[-1].add((
                int(parsed.group(1)),
                int(parsed.group(2)),
                int(parsed.group(3))
            ))

    zero_based_scanners_and_beacons = {
        0: scanners_and_beacons[0]
    }

    tested_pair = set()

    prior_len = 0

    while len(zero_based_scanners_and_beacons) < len(scanners_and_beacons):
        if prior_len == len(zero_based_scanners_and_beacons):
            print(len(scanners_and_beacons))
            print(len(zero_based_scanners_and_beacons))
            raise Exception("Not got smaller")
        prior_len = len(zero_based_scanners_and_beacons)
        for scanner_number, beacons in enumerate(scanners_and_beacons):
            if scanner_number in zero_based_scanners_and_beacons.keys():
                pass
            else:
                try:
                    for comparison_scanner_number, beacon_details in zero_based_scanners_and_beacons.items():
                        if (scanner_number, comparison_scanner_number) in tested_pair:
                            pass
                        else:
                            for coord_index in itertools.permutations(range(3)):
                                for x_rotate in [1, -1]:
                                    for y_rotate in [1, -1]:
                                        for z_rotate in [1, -1]:
                                            for base_beacon in beacon_details:
                                                for non_base_beacon in beacons:
                                                    x_difference = base_beacon[0] - non_base_beacon[coord_index[0]] * x_rotate
                                                    y_difference = base_beacon[1] - non_base_beacon[coord_index[1]] * y_rotate
                                                    z_difference = base_beacon[2] - non_base_beacon[coord_index[2]] * z_rotate

                                                    beacons_adjusted = set()
                                                    for non_base_beacon_2 in beacons:
                                                        beacons_adjusted.add((
                                                            x_difference + non_base_beacon_2[coord_index[0]] * x_rotate,
                                                            y_difference + non_base_beacon_2[coord_index[1]] * y_rotate,
                                                            z_difference + non_base_beacon_2[coord_index[2]] * z_rotate
                                                        ))
                                                    if len(beacons_adjusted) != len(beacons):
                                                        raise Exception("Shouldnt be here")


                                                    if len(beacon_details.intersection(beacons_adjusted)) >= 12:
                                                        zero_based_scanners_and_beacons[scanner_number] = beacons_adjusted
                                                        raise FoundBeaconMatch
                            tested_pair.add((scanner_number, comparison_scanner_number))
                            tested_pair.add((comparison_scanner_number, scanner_number))
                except FoundBeaconMatch:
                    pass
    
    all_beacons = set()

    for base_beacons in zero_based_scanners_and_beacons.values():
        all_beacons = all_beacons.union(base_beacons)

    return len(all_beacons)

@register(19, 2021, 2)
def scanners_2(text):
    scanners_and_beacons = []
    for line in text.split("\n"):
        if len(line) == 0:
            pass
        elif line[0:3] == "---":
            scanners_and_beacons.append(set())
        else:
            parsed = re.match(r"(-{0,1}\d+),(-{0,1}\d+),(-{0,1}\d+)", line)

            scanners_and_beacons[-1].add((
                int(parsed.group(1)),
                int(parsed.group(2)),
                int(parsed.group(3))
            ))

    zero_based_scanners_and_beacons = {
        0: scanners_and_beacons[0]
    }

    tested_pair = set()

    prior_len = 0

    scanner_positions = []

    while len(zero_based_scanners_and_beacons) < len(scanners_and_beacons):
        if prior_len == len(zero_based_scanners_and_beacons):
            print(len(scanners_and_beacons))
            print(len(zero_based_scanners_and_beacons))
            raise Exception("Not got smaller")
        prior_len = len(zero_based_scanners_and_beacons)
        for scanner_number, beacons in enumerate(scanners_and_beacons):
            if scanner_number in zero_based_scanners_and_beacons.keys():
                pass
            else:
                try:
                    for comparison_scanner_number, beacon_details in zero_based_scanners_and_beacons.items():
                        if (scanner_number, comparison_scanner_number) in tested_pair:
                            pass
                        else:
                            for coord_index in itertools.permutations(range(3)):
                                for x_rotate in [1, -1]:
                                    for y_rotate in [1, -1]:
                                        for z_rotate in [1, -1]:
                                            for base_beacon in beacon_details:
                                                for non_base_beacon in beacons:
                                                    x_difference = base_beacon[0] - non_base_beacon[coord_index[0]] * x_rotate
                                                    y_difference = base_beacon[1] - non_base_beacon[coord_index[1]] * y_rotate
                                                    z_difference = base_beacon[2] - non_base_beacon[coord_index[2]] * z_rotate

                                                    beacons_adjusted = set()
                                                    for non_base_beacon_2 in beacons:
                                                        beacons_adjusted.add((
                                                            x_difference + non_base_beacon_2[coord_index[0]] * x_rotate,
                                                            y_difference + non_base_beacon_2[coord_index[1]] * y_rotate,
                                                            z_difference + non_base_beacon_2[coord_index[2]] * z_rotate
                                                        ))
                                                    if len(beacons_adjusted) != len(beacons):
                                                        raise Exception("Shouldnt be here")


                                                    if len(beacon_details.intersection(beacons_adjusted)) >= 12:
                                                        zero_based_scanners_and_beacons[scanner_number] = beacons_adjusted
                                                        scanner_positions.append((x_difference, y_difference, z_difference))
                                                        raise FoundBeaconMatch
                            tested_pair.add((scanner_number, comparison_scanner_number))
                            tested_pair.add((comparison_scanner_number, scanner_number))
                except FoundBeaconMatch:
                    pass
    
    max_distance = 0

    for combo in itertools.combinations(scanner_positions, 2):
        this_distance = abs(combo[0][0] - combo[1][0]) + abs(combo[0][1] - combo[1][1]) + abs(combo[0][2] - combo[1][2])

        if this_distance > max_distance:
            max_distance = this_distance
    
    return max_distance
