from advent.runner import register
import re

@register(15, 2022, 1, True)
def beacon_exclusion_zone_1(split_text, row=2000000):
    impossible_beacons = set()
    beacons = set()

    for line in split_text:
        parsed_line = re.search(r"Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)", line)

        sensor_x = int(parsed_line.group(1))
        sensor_y = int(parsed_line.group(2))
        beacon_x = int(parsed_line.group(3))
        beacon_y = int(parsed_line.group(4))

        beacons.add((beacon_x, beacon_y))

        distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        vertical_distance = abs(row - sensor_y)

        horizontal_distance = distance - vertical_distance

        for i in range(horizontal_distance + 1):
            impossible_beacons.add((sensor_x + i, row))
            impossible_beacons.add((sensor_x - i, row))

    return len(impossible_beacons.difference(beacons))


@register(15, 2022, 2, True)
def beacon_exclusion_zone_2(split_text, max_value=4000000):
    rules = []
    
    for line in split_text:
        parsed_line = re.search(r"Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)", line)

        sensor_x = int(parsed_line.group(1))
        sensor_y = int(parsed_line.group(2))
        beacon_x = int(parsed_line.group(3))
        beacon_y = int(parsed_line.group(4))

        distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        rules.append({
            "line": line,
            "distance": distance,
            "sensor_x": sensor_x,
            "sensor_y": sensor_y
        })

    for rule in rules:
        for x in range(max_value + 1):
            for abs_sign in [-1, 1]:
                y = abs_sign * (rule["distance"] + 1 - abs(x - rule["sensor_x"])) + rule["sensor_y"]
                if y >= 0 and y <= max_value:
                    valid_coord = True
                    for next_rule in rules:
                        if abs(x - next_rule["sensor_x"]) + abs(y - next_rule["sensor_y"]) <= next_rule["distance"]:
                            valid_coord = False
                            break
                    if valid_coord:
                        return x * 4000000 + y