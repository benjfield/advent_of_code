from advent.utils.path_finding import Node, djikstra, is_final_node_function
from advent.runner import register

class MountainNode(Node):
    def get_neighbours(self, map, cost):
        neighbours = []

        max_letter_number = ord(map[self.y][self.x]) + 1 

        for x, y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if self.check_valid_neighbour(x, y, len(map[0]) - 1, len(map) - 1):
                if ord(map[y][x]) <=  max_letter_number:
                    possible_neighbour = type(self)(
                        x=x,
                        y=y
                    )
                    self.append_neighbours(neighbours, possible_neighbour, cost)
        return neighbours
    
@register(12, 2022, 1, True)
def hill_climbing_1(split_text):
    map = []
    for y, line in enumerate(split_text):
        map.append([]) 
        for x, char in enumerate(line): 
            if char == "S":
                char = "a"
                
                start_point = MountainNode(x, y)
            elif char == "E":
                char = "z"
                
                final_point = MountainNode(x, y)

            map[-1].append(char)
            
    final_node_function = is_final_node_function(final_point)

    result = djikstra(map, start_point, terminate_function=final_node_function)

    return result
    
class MountainNodeDown(Node):
    def __init__(
        self,
        x,
        y,
        letter):
        super().__init__(x, y)
        self.letter = letter

    def get_neighbours(self, map, cost):
        neighbours = []

        min_letter_number = ord(self.letter) - 1 

        for x, y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if self.check_valid_neighbour(x, y, len(map[0]) - 1, len(map) - 1):
                if ord(map[y][x]) >= min_letter_number:
                    possible_neighbour = type(self)(
                        x=x,
                        y=y,
                        letter=map[y][x]
                    )
                    self.append_neighbours(neighbours, possible_neighbour, cost)
        return neighbours

def hill_climbing_final_node(this_node):
    if this_node.letter == "a":
        return True
    else:
        return False

@register(12, 2022, 2, True)
def hill_climbing_2(split_text):
    map = []
    for y, line in enumerate(split_text):
        map.append([]) 
        for x, char in enumerate(line): 
            if char == "S":
                char = "a"
            elif char == "E":
                char = "z"
                
                start_point = MountainNodeDown(x, y, char)

            map[-1].append(char)

    result = djikstra(map, start_point, terminate_function=hill_climbing_final_node)

    return result