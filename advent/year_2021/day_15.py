from advent.runner import register
from advent.utils.path_finding import djikstra, Node, is_final_node_function

class RiskNode(Node):
    def get_neighbours(self, map, cost):
        neighbours = []

        for x, y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if self.check_valid_neighbour(x, y, len(map[0]) - 1, len(map) - 1):
                possible_neighbour = type(self)(
                    x=x,
                    y=y,
                )
                self.append_neighbours(neighbours, possible_neighbour, cost, map[y][x])
        return neighbours

@register(15, 2021, 1)
def chiton_1(text):
    map = []
    for row in text.split("\n"):
        map.append([ int(tile) for tile in row ])
    
    start_x = 0
    start_y = 0
    final_x = len(map[0]) - 1
    final_y = len(map) - 1

    final_node_function = is_final_node_function(RiskNode(final_x, final_y))

    return djikstra(map, RiskNode(start_x, start_y), terminate_function=final_node_function)


@register(15, 2021, 2)
def chiton_2(text):
    single_map = []
    for row in text.split("\n"):
        single_map.append([ int(tile) for tile in row ])
    
    map = []

    for i in range(5):
        for row in single_map:
            map.append([])
            for j in range(5):
                for tile in row:
                    new_tile = tile + i + j

                    if new_tile >= 10:
                        new_tile -= 9

                    map[-1].append(new_tile)
        
    start_x = 0
    start_y = 0
    final_x = len(map[0]) - 1
    final_y = len(map) - 1

    final_node_function = is_final_node_function(RiskNode(final_x, final_y))

    return djikstra(map, RiskNode(start_x, start_y), terminate_function=final_node_function)