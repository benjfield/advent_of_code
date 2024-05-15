import heapq
from functools import partial

class NodeStore:
    def __init__(self):
        self.store = {}

    def store_initial_node(self, node):
        self.store[node] = 0

    def store_node(self, node, cost):
        if cost < self.store.get(node, 1000000):
            self.dummy_method()
            self.store[node] = cost

    def get_node_and_costs(self, node):
        return node, self.store.get(node, 1000000)

    def remove_node(self, node):
        self.store.pop(node)
    
    def dummy_method(self):
        pass
    def get_lowest_cost_node(self):
        lowest_cost = 1000000
        for key, value in self.store.items():
            if value < lowest_cost:
                lowest_cost = value
                lowest_cost_node = key
        self.remove_node(lowest_cost_node)
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
        
    def is_empty(self):
        if len(self.store) == 0:
            return True

class HugeLengthArray:
    def __len__(self):
        return 1000000

class NodeStoreWithPath(NodeStore):
    def store_initial_node(self, node):
        self.store[node] = []

    def store_node(self, node, path):
        current_path = self.store.get(node, HugeLengthArray())
        if len(path) < len(current_path):
            self.store[node] = path

    def get_node_and_path(self, node):
        return node, self.store.get(node, None)
    
    def get_lowest_cost_node(self):
        lowest_cost_path = HugeLengthArray()
        for node, path in self.store.items():
            if len(path) < len(lowest_cost_path):
                lowest_cost_path = path
                lowest_cost_node = node
        self.remove_node(lowest_cost_node)
        return lowest_cost_node, lowest_cost_path

class NodeQueue:
    def __init__(self):
        self.priority_store = []
        self.processed = set()
        self.count = 0

    def store_initial_node(self, node):
        self.store_node(node, 0)

    def store_node(self, node, cost):
        new_entry = (cost, self.count, node)

        heapq.heappush(self.priority_store, new_entry)
        self.count += 1

    def get_lowest_cost_node(self):
        while self.priority_store:
            cost, count, node = heapq.heappop(self.priority_store)
            if node not in self.processed:
                self.processed.add(node)
                return node, cost
        return None, 1000000
    
    def is_empty(self):
        if len(self.priority_store) == 0:
            return True

class Node:
    def __init__(self, x, y):
       self.x = x
       self.y = y

    def get_neighbours(self, map, cost):
        neighbours = []

        for x, y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if self.check_valid_neighbour(x, y, len(map[0]) - 1, len(map) - 1):
                if map[y][x] == ".":
                    possible_neighbour = type(self)(
                        x=x,
                        y=y,
                    )
                    self.append_neighbours(neighbours, possible_neighbour, cost)
        return neighbours
    
    @classmethod
    def append_neighbours(cls, neighbours, possible_neighbour, cost, additional_node_cost=1):
        neighbours.append({
            "neighbour": possible_neighbour,
            "cost": cost + additional_node_cost
        })

    @classmethod
    def check_valid_neighbour(cls, x, y, final_x, final_y):
        return x >= 0 and x <= final_x and y >= 0 and y <= final_y
    
    #Obvious improvement here is to move to a numeeric hash - max_y * x + x would work fine
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return f"x {self.x} y {self.y}"

class NodeWithPath(Node):
    @classmethod
    def append_neighbours(cls, neighbours, possible_neighbour, cost):
        this_cost = cost.copy()
        this_cost.append({
            "x": possible_neighbour.x,
            "y": possible_neighbour.y
        })

        neighbours.append({
            "neighbour":possible_neighbour,
            "cost": this_cost
        })

def is_final_node(final_node, this_node):
    if final_node == this_node:
        return True
    else:
        return False

def is_final_node_function(final_node):
    return partial(is_final_node, final_node)

def djikstra(map, start_point, store_with_path=False, terminate_function=None):
    if store_with_path:
        open_list = NodeStoreWithPath()

        closed_list = NodeStoreWithPath()
    else:
        closed_list = NodeStore()
        
        open_list = NodeQueue()
    
    open_list.store_initial_node(start_point)

    while not open_list.is_empty():
        current_square, current_square_cost = open_list.get_lowest_cost_node()
        if current_square is None:
            #Means this is finished
            break
        if terminate_function is not None:
            if terminate_function(current_square):
                return current_square_cost

        closed_list.store_node(current_square, current_square_cost)

        neighbours_with_costs = current_square.get_neighbours(map, current_square_cost)

        for neighbour_with_cost in neighbours_with_costs:
            if neighbour_with_cost["neighbour"] in closed_list.store:
                pass
            else:
                open_list.store_node(neighbour_with_cost["neighbour"], neighbour_with_cost["cost"])

    return closed_list