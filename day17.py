from direction import Direction
from aocd import get_data

class NodeStore:
    def __init__(self):
        self.store = {}

    def store_node(self, node, cost, final_x, final_y, current_g):
        h = node.calculate_estimated_cost(final_x, final_y)
        self.store[node] = {
            "movement_cost": cost,
            "h": h,
            "g": current_g + cost,
            "f": h + cost + current_g
        }

    def store_node_with_costs(self, node, costs):
        self.store[node] = costs

    def update_costs(self, node, new_g):
        current_costs = self.store[node]
        if new_g + current_costs["movement_cost"]  < current_costs["g"]:
            self.store[node]["g"] = new_g + current_costs["movement_cost"]
            self.store[node]["f"] = new_g + current_costs["movement_cost"] + current_costs["h"]

    def get_node_and_costs(self, node):
        return node, self.store[node]

    def remove_node(self, node):
        self.store.pop(node)
    
    def get_lowest_cost_node(self):
        lowest_cost = {"f": 10000000}
        lowest_cost_node = None
        for key, value in self.store.items():
            if value["f"] < lowest_cost["f"]:
                lowest_cost = value
                lowest_cost_node = key
        return lowest_cost_node, lowest_cost

class Node:
    def __init__(self, x, y, direction, move_count):
       self.x = x
       self.y = y
       self.direction = direction
       self.move_count = move_count

    def calculate_estimated_cost(self, final_x, final_y):
        return final_x - self.x + final_y - self.y

    def get_neighbours(self, final_x, final_y):
        neighbours = []
        if self.move_count < 3:
            x, y = self.direction.move_forward(self.x, self.y)
            if x >= 0 and x <= final_x and y >= 0 and y <= final_y:
                possible_neighbour = Node(
                    x=x,
                    y=y,
                    direction=self.direction,
                    move_count=self.move_count + 1,
                )
                neighbours.append(possible_neighbour)
        for clockwise in [False, True]:
            direction = self.direction.rotate(clockwise)
            x, y = direction.move_forward(self.x, self.y)
            if x >= 0 and x <= final_x and y >= 0 and y <= final_y:
                possible_neighbour = Node(
                    x=x,
                    y=y,
                    direction=direction,
                    move_count=1,
                )
                neighbours.append(possible_neighbour)
        return neighbours
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.direction == other.direction and self.move_count == other.move_count:
            return True
        return False

    def __str__(self):
        return f"x {self.x} y {self.y} direction {self.direction} move_count {self.move_count}"

class Ultra_Node(Node):
    def get_neighbours(self, final_x, final_y):
        neighbours = []
        if self.move_count < 10:
            x, y = self.direction.move_forward(self.x, self.y)
            if x >= 0 and x <= final_x and y >= 0 and y <= final_y:
                possible_neighbour = Ultra_Node(
                    x=x,
                    y=y,
                    direction=self.direction,
                    move_count=self.move_count + 1,
                )
                neighbours.append(possible_neighbour)
        if self.move_count >= 4:
            for clockwise in [False, True]:
                direction = self.direction.rotate(clockwise)
                x, y = direction.move_forward(self.x, self.y)
                if x >= 0 and x <= final_x and y >= 0 and y <= final_y:
                    possible_neighbour = Ultra_Node(
                        x=x,
                        y=y,
                        direction=direction,
                        move_count=1,
                    )
                    neighbours.append(possible_neighbour)
        return neighbours

def a_star(costs_matrix, start_direction, node_type=Node):
    start_point = node_type(0, 0, start_direction, 0)

    open_list = NodeStore()

    closed_list = NodeStore()

    final_x = len(costs_matrix[0]) - 1
    final_y = len(costs_matrix) - 1
    
    open_list.store_node(start_point, costs_matrix[start_point.y][start_point.x], final_x, final_y, - costs_matrix[start_point.y][start_point.x])

    while True:
        current_square, current_square_costs = open_list.get_lowest_cost_node()
        if current_square.x == final_x and current_square.y == final_y:
            return current_square_costs["f"]
        open_list.remove_node(current_square)
        closed_list.store_node_with_costs(current_square, current_square_costs)

        neighbours = current_square.get_neighbours(final_x, final_y)
        for neighbour in neighbours:
            if neighbour in closed_list.store:
                pass
            else:
                if neighbour not in open_list.store:
                    open_list.store_node(neighbour, costs_matrix[neighbour.y][neighbour.x], final_x, final_y, current_square_costs["g"])
                else:
                    open_list.update_costs(neighbour, current_square_costs["g"])

def path_1(text):
    costs_matrix = []
    for costs in text.split("\n"):
        costs_matrix.append([])
        for cost in costs:  
            costs_matrix[-1].append(int(cost))

    down_cost = a_star(costs_matrix, Direction.DOWN)
    right_cost = a_star(costs_matrix, Direction.RIGHT)

    return min(down_cost, right_cost)

def path_2(text):
    costs_matrix = []
    for costs in text.split("\n"):
        costs_matrix.append([])
        for cost in costs:  
            costs_matrix[-1].append(int(cost))

    down_cost = a_star(costs_matrix, Direction.DOWN, Ultra_Node)
    right_cost = a_star(costs_matrix, Direction.RIGHT, Ultra_Node)

    return min(down_cost, right_cost)

path_text = get_data(day=17, year=2023)
#print(path_2(path_text))