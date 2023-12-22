from aocd import get_data
class NodeStore:
    def __init__(self):
        self.store = {}

    def store_node(self, node, cost):
        if cost < self.store.get(node, 1000000):
            self.store[node] = cost

    def get_node_and_costs(self, node):
        return node, self.store.get(node, 1000000)

    def remove_node(self, node):
        self.store.pop(node)
    
    def get_lowest_cost_node(self):
        lowest_cost = 1000000
        for key, value in self.store.items():
            if value < lowest_cost:
                lowest_cost = value
                lowest_cost_node = key
        return lowest_cost_node, lowest_cost

    def get_odd_and_even_count(self, max_distance=1000000):
        odd_count = 0
        even_count = 0
        for distance in self.store.values():
            if distance <= max_distance:
                if distance%2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
        return odd_count, even_count

    def get_even_nodes_count_less_than_max(self, max):
        count = 0
        for distance in self.store.values():
            if distance <= max and distance%2 == 0:
                count += 1
        return count

class Node:
    def __init__(self, x, y):
       self.x = x
       self.y = y

    def get_neighbours(self, final_x, final_y, map):
        neighbours = []

        for x, y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if x >= 0 and x <= final_x and y >= 0 and y <= final_y:
                if map[y][x] == ".":
                    possible_neighbour = Node(
                        x=x,
                        y=y,
                    )
                    neighbours.append(possible_neighbour)
        return neighbours
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return f"x {self.x} y {self.y}"

def djikstra(map, start_x, start_y):
    start_point = Node(start_x, start_y)

    open_list = NodeStore()

    closed_list = NodeStore()

    final_x = len(map[0]) - 1
    final_y = len(map) - 1
    
    open_list.store_node(start_point, 0)

    while len(open_list.store) > 0:
        current_square, current_square_cost = open_list.get_lowest_cost_node()

        open_list.remove_node(current_square)

        closed_list.store_node(current_square, current_square_cost)

        neighbours = current_square.get_neighbours(final_x, final_y, map)
        for neighbour in neighbours:
            if neighbour in closed_list.store:
                pass
            else:
                open_list.store_node(neighbour, current_square_cost + 1)

    return closed_list

def garden_1(text, max=64):
    map = []
    start_x = 0
    start_y = 0
    for i, row in enumerate(text.split("\n")):
        map.append([])
        for j, tile in enumerate(row):
            if tile == "S":
                start_x = j
                start_y = i
                map[-1].append(".")
            else:
                map[-1].append(tile)

    closed_list = djikstra(map, start_x, start_y)
    
    return closed_list.get_even_nodes_count_less_than_max(max)

def garden_2(text, max_distance=64):
    map = []
    start_x = 0
    start_y = 0
    for i, row in enumerate(text.split("\n")):
        map.append([])
        for j, tile in enumerate(row):
            if tile == "S":
                start_x = j
                start_y = i
                map[-1].append(".")
            else:
                map[-1].append(tile)

    closed_list = djikstra(map, start_x, start_y)

    max_x = len(map[0]) - 1
    max_y = len(map) - 1

    corner_lengths = []

    closed_list = djikstra(map, start_x, start_y)

    max_odd = True
    if max_distance%2 == 0:
        max_odd = False

    odd_count, even_count = closed_list.get_odd_and_even_count(max_distance)

    if max_odd:
        total_count = odd_count
    else:
        total_count = even_count

    for x in [0, max_x]:
        for y in [0, max_y]:
    #for x in [0]:
    #    for y in [0]:
            node = Node(x, y)

            corner_distance = closed_list.store[node] + 2

            if corner_distance%2 != 0:
                raise Exception("Assumes corners are always even")

            number_of_square_rows = int((max_distance-corner_distance)/(max_x + 1)) - 1

            if x == 0:
                reverse_x = max_x
            else:
                reverse_x = 0
            if y == 0:
                reverse_y = max_y
            else:
                reverse_y = 0        
            corner_closed_list = djikstra(map, reverse_x, reverse_y)

            odd_count, even_count = corner_closed_list.get_odd_and_even_count(max_x + max_y)
            
            if len(corner_closed_list.store) > odd_count + even_count:
                raise Exception("Simple corner solution doesnt work")
            
            number_of_even_rows = int(number_of_square_rows/2)
            number_of_odd_rows = number_of_even_rows

            if number_of_square_rows%2 != 0:
                number_of_even_rows += 1
                next_row_even = False
                highest_even = number_of_square_rows 
                highest_odd = number_of_square_rows - 1
            else:
                next_row_even=True
                highest_even = number_of_square_rows - 1
                highest_odd = number_of_square_rows

            number_of_even_squares = int(((1 + highest_even) * number_of_even_rows)/2)

            number_of_odd_squares = int(((2 + highest_odd) * number_of_odd_rows)/2) 

            if max_odd:
                corner_count = number_of_even_squares * odd_count + number_of_odd_squares * even_count
            else:
                corner_count = number_of_even_squares * even_count + number_of_odd_squares * odd_count

            remainder = max_distance - corner_distance - number_of_square_rows * (max_x + 1)

            if remainder >= 0:
                odd_count, even_count = corner_closed_list.get_odd_and_even_count(remainder)
                remainder_2 = max(0, remainder - (max_x + 1))
                if remainder_2 > (max_x + 1):
                    raise Exception("Miscalc somewhere")
                odd_count_2, even_count_2 = corner_closed_list.get_odd_and_even_count(remainder_2)

                if max_odd:
                    if next_row_even:
                        corner_count += odd_count * (number_of_square_rows + 1) + even_count_2 * (number_of_square_rows + 2)
                    else:
                        corner_count += even_count * (number_of_square_rows + 1) + odd_count_2 * (number_of_square_rows + 2)
                else:
                    if next_row_even:
                        corner_count += even_count * (number_of_square_rows + 1) + odd_count_2 * (number_of_square_rows + 2)
                    else:
                        corner_count += odd_count * (number_of_square_rows + 1) + even_count_2 * (number_of_square_rows + 2)

            total_count += corner_count
                        
    #print(total_count)
    #for x in [0, max_x]:
    #for x, y in [(0, start_y)]:
    for x, y in [(0, start_y), (start_x, 0), (max_x, start_y), (start_x, max_y)]:

        node = Node(x, y)

        side_distance = closed_list.store[node] + 1

        if x == 0:
            reverse_x = max_x
        elif x == max_x:
            reverse_x = 0
        else:
            reverse_x = start_x

        if y == 0:
            reverse_y = max_y
        elif y == max_y:
            reverse_y = 0
        else:
            reverse_y = start_y

        horizontal_closed_list = djikstra(map, reverse_x, reverse_y)

        odd_count, even_count = horizontal_closed_list.get_odd_and_even_count(2*max_x)

        if len(horizontal_closed_list.store) > odd_count + even_count:
            raise Exception("2 multiplier doesnt work")
    
        number_of_squares = int((max_distance-side_distance)/(max_x + 1)) - 1
            
        number_of_even_squares = int(number_of_squares/2)
        number_of_odd_squares = number_of_even_squares


        if number_of_squares%2 != 0:
            number_of_even_squares += 1
            next_row_even = False
        else:
            next_row_even=True

        if max_odd:
            side_count = number_of_even_squares * odd_count + number_of_odd_squares * even_count
        else:
            side_count = number_of_even_squares * even_count + number_of_odd_squares * odd_count

        remainder = max_distance - side_distance - number_of_squares * (max_x + 1)

        if remainder >= 0:
            odd_count, even_count = horizontal_closed_list.get_odd_and_even_count(remainder)
            remainder_2 = max(0, remainder - (max_x + 1))
            if remainder_2 > (max_x + 1):
                raise Exception("Miscalc somewhere")
            odd_count_2, even_count_2 = horizontal_closed_list.get_odd_and_even_count(remainder_2)

            if max_odd:
                if next_row_even:
                    side_count += odd_count + even_count_2
                else:
                    side_count += even_count + odd_count_2
            else:
                if next_row_even:
                    side_count += even_count + odd_count_2
                else:
                    side_count += odd_count + even_count_2

        total_count += side_count

    return total_count
    
def top_left_corner_tester(map, start_x, start_y):
    rock_row = []
    for i in range(len(map[0])):
        rock_row.append("#")
    
    total_map = []

   # for i in range(0, 7):
   #     for row in map:
   #         total_map.append(row+row+row+row+row+row+row+row+rock_row)    

    for i in range(0, 3):
        for row in map:
            total_map.append(rock_row+rock_row+rock_row+rock_row+rock_row+rock_row+rock_row+rock_row+rock_row)

    for i in range(0, 5):
        for row in map:
            total_map.append(rock_row+rock_row+rock_row+rock_row+rock_row+rock_row+rock_row+rock_row+row)

    for row in map:
        total_map.append(rock_row+rock_row+rock_row+row+row+row+row+row+row)


    #return total_map, start_x + 8 * len(map[0]), start_y + 8 *len(map)

    #for i in range(0, 9):
    #    for row in map:
    #        total_map.append(row)    

    return total_map, start_x + 8 *len(map[0]), start_y+ 8 *len(map) 

def garden_2_naive(text, max_distance=963):
    map = []
    start_x = 0
    start_y = 0
    for i, row in enumerate(text.split("\n")):
        map.append([])
        for j, tile in enumerate(row):
            if tile == "S":
                start_x = j
                start_y = i
                map[-1].append(".")
            else:
                map[-1].append(tile)

    total_map, start_x, start_y = top_left_corner_tester(map, start_x, start_y)

    closed_list = djikstra(total_map, start_x, start_y)

    odd_count, even_count = closed_list.get_odd_and_even_count(max_distance)
    if max_distance%2 == 0:
        return even_count
    else:
        return odd_count

garden_text = get_data(day=21, year=2023)
#top left 963: 180756
#top_left_with_horizontal_missing_4: 204121
#top_left_with_horizontal_missing_3: 211912
#top_left_horizontal_only_missing_3: 46734
#top_left_with_horizontal_missing_2: 219699
#top_left_with_horizontal: 224443
#tl_with_hor_and_ver: 268112
#tl_with_ver_only: 59247
#tl_with_hor_only: 59265
#tl_with_hor_and_ver_only:110725 
#tl_with_hor_and_ver_only_missing_3: 85681
#print(garden_2(garden_text, 26501365))  