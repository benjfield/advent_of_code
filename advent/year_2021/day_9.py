from advent.runner import register
@register(9, 2021, 1)
def smoke_basin_1(text):
    smoke_array = []

    for line in text.split("\n"):
        smoke_array.append(
            [ int(x) for x in line ]
        )

    low_point_total = 0

    for y, row in enumerate(smoke_array):
        for x, height in enumerate(row):
            if x == 0 or smoke_array[y][x - 1] > height:
                if y == 0 or smoke_array[y - 1][x] > height:
                    if y == len(smoke_array) - 1 or smoke_array[y + 1][x] > height:
                        if x == len(row) - 1 or smoke_array[y][x + 1] > height:
                            low_point_total += 1 + height

    return low_point_total

@register(9, 2021, 2)
def smoke_basin_2(text):
    smoke_array = []

    for line in text.split("\n"):
        smoke_array.append(
            [ int(x) for x in line ]
        )

    low_points = {}

    for y, row in enumerate(smoke_array):
        for x, height in enumerate(row):
            if x == 0 or smoke_array[y][x - 1] > height:
                if y == 0 or smoke_array[y - 1][x] > height:
                    if y == len(smoke_array) - 1 or smoke_array[y + 1][x] > height:
                        if x == len(row) - 1 or smoke_array[y][x + 1] > height:
                            low_points[(x, y)] = 0

    checked_points = set()
    for low_point in low_points.keys():
        points_to_check = [low_point]
        while len(points_to_check) > 0:
            next_points = []
            for point in points_to_check:
                for next_point in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)]:
                    if next_point[0] >= 0 and next_point[0] < len(smoke_array[0]) and next_point[1] >= 0 and next_point[1] < len(smoke_array):
                        if next_point not in checked_points and smoke_array[next_point[1]][next_point[0]] < 9:
                            checked_points.add(next_point)
                            next_points.append(next_point)
                            low_points[low_point] += 1
            points_to_check = next_points

    sizes = list(low_points.values())

    sizes.sort(reverse=True)                  

    return sizes[0] * sizes[1] * sizes[2]