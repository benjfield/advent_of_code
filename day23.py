from aocd import get_data
from direction import Direction
class Node:
    def __init__(self, x, y, direction=None, end_point=False, start_point=False):
        self.x = x
        self.y = y
        self.direction = direction
        self.neighbours = []
        self.junction_neighbours = []
        if end_point:
            self.junction = True
            self.end_point = True
            self.start_point = False
        elif start_point:
            self.junction = True
            self.start_point = True
            self.end_point = False    
        else:
            self.junction = False
            self.end_point = False
            self.start_point = False

    def populate_neighbours(self, nodes):
        if self.direction is None:
            directions = Direction
            #for direction in Direction:
            #    directions.append(direction)
        else: 
            directions = [self.direction]
        
        entrance_and_exit_nodes = 0

        for direction in directions:
            x, y = direction.move_forward(self.x, self.y)
            node_string = f"x {x} y {y}"
            if node_string in nodes:
                entrance_and_exit_nodes += 1
                neighbour_node = nodes[node_string]
                if neighbour_node.direction is not None and neighbour_node.direction == direction.flip():
                    pass
                else:
                    self.neighbours.append(neighbour_node)

        if entrance_and_exit_nodes > 2:
            self.junction = True
        
        return self.junction
    
    def populate_junction(self):
        for neighbour in self.neighbours:
            journey_result = neighbour.test_journey(self, 0)
            if journey_result is not None:
                self.junction_neighbours.append({
                    "neighbour": journey_result[0],
                    "cost": journey_result[1]
                })
            
    def test_journey(self, prior, count):
        count += 1
        if self.junction or self.end_point:
            return self, count
        else:
            for neighbour in self.neighbours:
                if neighbour != prior:
                    return neighbour.test_journey(self, count)
            return None
        
    def journey_to_end(self, visited_nodes = {}, cost = 0):
        if self.end_point:
            return cost
        
        if self in visited_nodes:
            return None
        
        visited_nodes[self] = True
        costs = []
        for neighbour in self.junction_neighbours:
            nodes = visited_nodes.copy()
            neighbour_cost = neighbour["neighbour"].journey_to_end(nodes, cost + neighbour["cost"])
            if neighbour_cost is not None:
                costs.append(neighbour_cost)
        
        if len(costs) == 0:
            return None
        return max(costs)

        
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return f"x {self.x} y {self.y}"

def journey_1(text):
    nodes = {}

    start_x = 1
    start_y = 0
    split_text = text.split("\n")
    end_x = len(split_text[0]) - 2
    end_y = len(split_text) - 1 

    start_point = None

    for y, row in enumerate(text.split("\n")):
        for x, tile in enumerate(row):
            if tile == "#":
                pass
            elif tile == ".":
                if x == start_x and y == start_y:
                    node = Node(x, y, None, False, True)
                    start_point = node
                elif x == end_x and y == end_y:
                    node = Node(x, y, None, True, False)
                else:
                    node = Node(x, y)
                nodes[str(node)] = node
            else:
                direction = Direction.direction_from_arrow(tile)
                node = Node(x, y, direction)
                nodes[str(node)] = node

    junctions = []

    for node in nodes.values():
        is_junction = node.populate_neighbours(nodes)
        if is_junction:
            junctions.append(node)

    for junction in junctions:
        junction.populate_junction()
    
    return start_point.journey_to_end()

def journey_2(text):
    nodes = {}

    start_x = 1
    start_y = 0
    split_text = text.split("\n")
    end_x = len(split_text[0]) - 2
    end_y = len(split_text) - 1 

    start_point = None

    for y, row in enumerate(text.split("\n")):
        for x, tile in enumerate(row):
            if tile == "#":
                pass
            else:
                if x == start_x and y == start_y:
                    node = Node(x, y, None, False, True)
                    start_point = node
                elif x == end_x and y == end_y:
                    node = Node(x, y, None, True, False)
                else:
                    node = Node(x, y)
                nodes[str(node)] = node

    junctions = []

    for node in nodes.values():
        is_junction = node.populate_neighbours(nodes)
        if is_junction:
            junctions.append(node)

    for junction in junctions:
        junction.populate_junction()
    
    return start_point.journey_to_end()

journey_text = get_data(day=23, year=2023)
print(journey_2(journey_text))        
