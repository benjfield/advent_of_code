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
    
    def get_highest_cost_node(self):
        highest_cost = 0
        for key, value in self.store.items():
            if value > highest_cost:
                highest_cost = value
                highest_cost_node = key
        return highest_cost_node, highest_cost
    
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
            if self.check_valid_neighbour(x, y, final_x, final_y):
                if map[y][x] == ".":
                    possible_neighbour = Node(
                        x=x,
                        y=y,
                    )
                    neighbours.append(possible_neighbour)
        return neighbours
    
    @classmethod
    def check_valid_neighbour(cls, x, y, final_x, final_y):
        return x >= 0 and x <= final_x and y >= 0 and y <= final_y
    
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