from advent.runner import register
from advent.utils.path_finding import Node, NodeStore
from advent.year_2019.computer import Computer
from advent.utils.direction import Direction

def get_direction_number(direction):
    if direction == Direction.UP:
        return 1
    elif direction == Direction.RIGHT:
        return 3
    elif direction == Direction.DOWN:
        return 2
    else:
        return 4

class OxygenNode(Node):
    def get_neighbours(self, computer, node_state_cache):
        neighbours = []
        end_node = None

        intial_state = node_state_cache[self]

        for direction in Direction:
            x, y = direction.move_forward(self.x, self.y)
            possible_neighbour = OxygenNode(
                x=x,
                y=y,
            )
            
            if possible_neighbour in node_state_cache:
                if node_state_cache[possible_neighbour] is not None:
                    neighbours.append(possible_neighbour)
            else:
                computer.reset_to_total_state(intial_state)

                finished, output = computer.process([get_direction_number(direction)])
                
                if output[-1] != 0:
                    neighbours.append(possible_neighbour)

                    node_state_cache[possible_neighbour] = computer.get_total_state()

                    if output[-1] == 2:
                        end_node = possible_neighbour
                else:
                    node_state_cache[possible_neighbour] = None
        return neighbours, end_node

def djikstra_to_oxygen(initial_computer):
    start_point = OxygenNode(0, 0)

    end_node = None

    node_state_cache = {start_point: initial_computer.get_total_state()}

    open_list = NodeStore()

    closed_list = NodeStore()
    
    open_list.store_node(start_point, 0)

    while len(open_list.store) > 0:
        current_square, current_square_cost = open_list.get_lowest_cost_node()

        if end_node is not None and end_node == current_square:
            return current_square_cost, end_node, node_state_cache

        open_list.remove_node(current_square)

        closed_list.store_node(current_square, current_square_cost)

        neighbours, possible_end_node = current_square.get_neighbours(initial_computer, node_state_cache)

        if possible_end_node is not None:
            end_node = possible_end_node

        for neighbour in neighbours:
            if neighbour in closed_list.store:
                pass
            else:
                open_list.store_node(neighbour, current_square_cost + 1)

    raise Exception("Should have returned earlier")

def djikstra_from_point_furthest_distance(initial_computer, initial_node, node_state_cache):
    open_list = NodeStore()

    closed_list = NodeStore()
    
    open_list.store_node(initial_node, 0)

    while len(open_list.store) > 0:
        current_square, current_square_cost = open_list.get_lowest_cost_node()

        open_list.remove_node(current_square)

        closed_list.store_node(current_square, current_square_cost)

        neighbours, possible_end_node = current_square.get_neighbours(initial_computer, node_state_cache)

        for neighbour in neighbours:
            if neighbour in closed_list.store:
                pass
            else:
                open_list.store_node(neighbour, current_square_cost + 1)

    highest_cost_node, highest_cost = closed_list.get_highest_cost_node()

    return highest_cost

@register(15, 2019, 1)
def oxygen_1(text):
    computer = Computer(text)

    end_node_cost, end_node, node_state_cache = djikstra_to_oxygen(computer)

    return end_node_cost

@register(15, 2019, 2)
def oxygen_2(text):
    computer = Computer(text)

    end_node_cost, end_node, node_state_cache = djikstra_to_oxygen(computer)

    return djikstra_from_point_furthest_distance(computer, end_node, node_state_cache)