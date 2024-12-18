import heapq
from functools import partial

from advent.utils.direction import Direction

from dataclasses import dataclass

from typing import Self

from advent.utils.grid import check_inbounds

@dataclass
class Cost:
    cost: int

    def get_cost(self) -> int:
        return self.cost
    
    def merge(self, other_cost: Self):
        return self

    def next_cost(
        self, 
        possible_neighbour,
        additional_node_cost: int = 1):        
        return type(self)(
            self.cost + additional_node_cost,
        )
    
    @classmethod
    def initial(cls, node):
        return cls(
            0,
        )
    
    def __str__(self):
        return f"cost {self.get_cost()}"
    
class CostWithVisited(Cost):
    path: set[tuple[int, int]]
    cost: int
    
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost

    def merge(self, other_cost: Self):
        self.path.update(other_cost.path)

        return self

    def next_cost(
        self, 
        possible_neighbour,
        additional_node_cost: int = 1):        
        this_path = self.path.copy()
        this_path.add(possible_neighbour.coord)

        return type(self)(
            this_path,
            self.cost + additional_node_cost,
        )
    
    @classmethod
    def initial(cls, node):
        initial_path = set()
        initial_path.add(node.coord)
        return cls(
            initial_path,
            0,
        )

@dataclass  
class Node:
    def __init__(self, coord):
       self.coord = coord

    def get_neighbours(self, map, cost_to_arrive):
        neighbours = []

        for direction in Direction:
            neighbour_coord = direction.move_forward(self.coord)
            if self.check_valid_neighbour(map, direction, neighbour_coord):
                possible_neighbour = self.get_neighbour(map, direction, neighbour_coord)
                possible_cost = cost_to_arrive.next_cost(
                    possible_neighbour,
                    self.get_additional_cost(map, direction, neighbour_coord)
                )
                neighbours.append((possible_neighbour, possible_cost))
        return neighbours

    def check_valid_neighbour(self, map, direction, neighbour_coord):
        x = neighbour_coord[0]
        y = neighbour_coord[1]
        return check_inbounds(map, x, y) and map[neighbour_coord] == "."
    
    def get_additional_cost(self, map, direction, neighbour_coord):
        return 1
    
    def get_neighbour(self, map, direction, neighbour_coord):
        return type(self)(
            neighbour_coord
        )
    
    #Obvious improvement here is to move to a numeeric hash - max_y * x + x would work fine
    def __hash__(self):
        return hash(self.coord)
    
    def __eq__(self, other: Self):
        return self.coord == other.coord

    def __str__(self):
        return f"x {self.coord[0]} y {self.coord[1]}"

class ClosedList:
    def __init__(self):
        self.store = {}

    def store_node(self, node: Node, cost: Cost):
        if node in self.store:
            prior_cost = self.store[node]
            if cost.get_cost() < prior_cost.get_cost():
                self.store[node] = cost
                return cost
            elif cost.get_cost() == prior_cost.get_cost():
                prior_cost.merge(cost)
                return prior_cost
            else:
                return prior_cost
        else:
            self.store[node] = cost
            return cost
        
    def is_empty(self):
        if len(self.store) == 0:
            return True
            
class OpenList:
    def __init__(self):
        self.priority_store = []
        self.processed = set()
        self.costs = {}
        self.count = 0
        self.cost_type = Cost

    def store_initial_node(self, node):
        self.store_node(node, self.cost_type.initial(node))

    def store_node(self, node, cost):
        new_entry = (cost.get_cost(), self.count, node)

        heapq.heappush(self.priority_store, new_entry)
        self.costs[(node, self.count)] = cost

        self.count += 1

    def get_lowest_cost_node(self) -> tuple[Node, Cost]:
        while self.priority_store:
            _, count, node = heapq.heappop(self.priority_store)
            if node not in self.processed:
                self.processed.add(node)
                cost_object = self.costs[(node, count)]
                return node, cost_object
        return None, 1000000
    
    def is_empty(self):
        if len(self.priority_store) == 0:
            return True

class OpenListRunEqual(OpenList):
    def __init__(self):
        self.priority_store = []
        self.processed = {}
        self.costs = {}
        self.count = 0
        self.cost_type = CostWithVisited

    def get_lowest_cost_node(self) -> tuple[Node, Cost]:
        while self.priority_store:
            cost, count, node = heapq.heappop(self.priority_store)
            if node not in self.processed or self.processed[node] == cost:
                self.processed[node] = cost
                cost_object = self.costs[(node, count)]
                return node, cost_object
        return None, 1000000
        
def has_final_coords(final_coords, this_node):
    if final_coords == this_node.coord:
        return True
    else:
        return False

def has_final_coords_function(final_node):
    return partial(has_final_coords, final_node)

def is_final_node(final_node, this_node):
    if final_node == this_node:
        return True
    else:
        return False

def is_final_node_function(final_node):
    return partial(is_final_node, final_node)

def djikstra(map, start_point, terminate_function=None, run_equal_options=True):
    closed_list = ClosedList()
    
    if run_equal_options:
        open_list = OpenListRunEqual()
    else:
        open_list = OpenList()
    
    open_list.store_initial_node(start_point)

    while not open_list.is_empty():
        current_node, current_node_cost = open_list.get_lowest_cost_node()
        if current_node is None:
            #Means this is finished
            break
        if terminate_function is not None:
            if terminate_function(current_node):
                return current_node_cost

        current_node_cost = closed_list.store_node(current_node, current_node_cost)

        neighbours_with_costs = current_node.get_neighbours(map, current_node_cost)

        for neighbour_with_cost in neighbours_with_costs:
            if neighbour_with_cost[0] in closed_list.store:
                pass
            else:
                open_list.store_node(*neighbour_with_cost)

    return closed_list