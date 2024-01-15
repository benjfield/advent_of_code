import math
from advent.runner import register

@register(10, 2019, 1)
def asteroids_1(text):
    asteroid_coordinates = []

    for y, row in enumerate(text.split("\n")):
        for x, char in enumerate(row):
            if char == "#":
                asteroid_coordinates.append({
                    "x": x,
                    "y": y
                })

    max_asteroids = 0
    for asteroid in asteroid_coordinates:
        distances = {}

        for comparison_asteroid in asteroid_coordinates:
            x_distance = comparison_asteroid["x"] - asteroid["x"]
            y_distance = comparison_asteroid["y"] - asteroid["y"]

            if x_distance != 0 or y_distance != 0:
                divisor = math.gcd(x_distance, y_distance)
                x_distance = int(x_distance/divisor)
                y_distance = int(y_distance/divisor)

                distances[(x_distance, y_distance)] = True

        max_asteroids = max(max_asteroids, len(distances))

    return max_asteroids

@register(10, 2019, 2)
def asteroids_2(text):
    asteroid_coordinates = []

    for y, row in enumerate(text.split("\n")):
        for x, char in enumerate(row):
            if char == "#":
                asteroid_coordinates.append({
                    "x": x,
                    "y": y
                })

    max_asteroids = 0
    distances_for_best = None
    for asteroid in asteroid_coordinates:
        distances = {}

        for comparison_asteroid in asteroid_coordinates:
            initial_x_distance = comparison_asteroid["x"] - asteroid["x"]
            initial_y_distance = comparison_asteroid["y"] - asteroid["y"]

            if initial_x_distance != 0 or initial_y_distance != 0:
                divisor = math.gcd(initial_x_distance, initial_y_distance)
                x_distance = int(initial_x_distance/divisor)
                y_distance = int(initial_y_distance/divisor)

                if (x_distance, y_distance) in distances:
                    distances[(x_distance, y_distance)].append({
                        "distance": abs(x_distance) + abs(y_distance),
                        "coordinate": comparison_asteroid
                    })
                else:
                    distances[(x_distance, y_distance)] = [{
                        "distance": abs(x_distance) + abs(y_distance),
                        "coordinate": comparison_asteroid
                    }]

        if len(distances) > max_asteroids:
            max_asteroids = len(distances)
            distances_for_best = distances

    sorted_asteroids = []
        
    def sort_by_distance(map):
        return map["distance"]
            
    def sort_by_angle(map):
        return map["angle"]
    
    for angle_details, asteroid_distances in distances_for_best.items():
        x = angle_details[0]
        y = angle_details[1]
        if x > 0 and y < 0:
            angle = math.atan(abs(x/y))
        elif x > 0 and y == 0:
            angle = math.pi / 2
        elif x > 0 and y > 0:
            angle = math.atan(y/x) + math.pi / 2
        elif x == 0 and y > 0:
            angle = math.pi
        elif x < 0 and y > 0:
            angle = math.atan(abs(x/y)) + math.pi
        elif x < 0 and y == 0:
            angle = math.pi * 3 / 2
        elif x < 0 and y < 0:
            angle = math.atan(y/x) + math.pi * 3 / 2
        elif x == 0 and y < 0:
            angle = 0
        else:
            raise Exception("Shouldnt be here")

        asteroid_distances.sort(key=sort_by_distance)

        sorted_asteroids.append({
            "angle": angle,
            "asteroid_distances": asteroid_distances
        })

    sorted_asteroids.sort(key=sort_by_angle)

    laser_count = 0

    while laser_count < 200:
        for direction in sorted_asteroids:
            if len(direction["asteroid_distances"]) > 0:
                if laser_count == 199:
                    return direction["asteroid_distances"][0]["coordinate"]["x"] * 100 + direction["asteroid_distances"][0]["coordinate"]["y"]
                direction["asteroid_distances"] = direction["asteroid_distances"][1:]
                laser_count += 1