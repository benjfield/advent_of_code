import heapq
from advent.runner import register
import re
import math

class Blueprint:
    def __init__(
        self,
        ore_cost,
        clay_cost,
        obsidian_cost,
        geode_cost,
        max_minutes = 24
    ):
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost
        self.geode_cost = geode_cost
        self.max_minutes = max_minutes

        self.max_robots = []
        for i in range(3):
            max_value = 0
            for cost in [
                self.ore_cost,
                self.clay_cost,
                self.obsidian_cost,
                self.geode_cost
            ]:
                if cost[i] > max_value:
                    max_value = cost[i]
            self.max_robots.append(max_value)

    def get_first_state(
        self
    ):
        return BlueprintState(
            self,
            0,
            (1, 0, 0, 0),
            (0, 0, 0, 0)
        )

class BlueprintState:
    def __init__(
        self,
        blueprint,
        minute,
        robots,
        resources
    ):
        self.blueprint = blueprint
        self.minute = minute
        self.robots = robots
        self.resources = resources

    def build_robot_and_add_to_heap(
        self,
        cost,
        robot_index,
        heap
    ):
        enough_resources = True
        for i in range(len(cost)):
            if cost[i] > self.resources[i] and self.robots[i] == 0:
                enough_resources = False
                break

        if enough_resources:
            number_of_turns_needed = 0

            for i in range(len(cost)):
                resources_remaining_to_produce = cost[i] - self.resources[i]
                if resources_remaining_to_produce > 0:
                    turns_remaining_to_produce = math.ceil(resources_remaining_to_produce / self.robots[i])

                    if turns_remaining_to_produce > number_of_turns_needed:
                        number_of_turns_needed = turns_remaining_to_produce

            #For the building itself
            number_of_turns_needed += 1

            next_robot_minute = self.minute + number_of_turns_needed
            if next_robot_minute < self.blueprint.max_minutes:
                heap.store_state(
                    BlueprintState(
                        self.blueprint,
                        next_robot_minute,
                        (
                            self.robots[0] + int(0 == robot_index),
                            self.robots[1] + int(1 == robot_index),
                            self.robots[2] + int(2 == robot_index),
                            self.robots[3] + int(3 == robot_index),
                        ),
                        (
                            self.resources[0] - cost[0] + self.robots[0] * number_of_turns_needed, 
                            self.resources[1] - cost[1] + self.robots[1] * number_of_turns_needed, 
                            self.resources[2] - cost[2] + self.robots[2] * number_of_turns_needed, 
                            self.resources[3] + self.robots[3] * number_of_turns_needed
                        )
                    )
                )

    def add_next_states_to_heap(
        self,
        heap
    ):
        if self.robots[0] < self.blueprint.max_robots[0]:
            self.build_robot_and_add_to_heap(self.blueprint.ore_cost, 0, heap)

        if self.robots[1] < self.blueprint.max_robots[1]:
            self.build_robot_and_add_to_heap(self.blueprint.clay_cost, 1, heap)
            
        if self.robots[2] < self.blueprint.max_robots[2]:
            self.build_robot_and_add_to_heap(self.blueprint.obsidian_cost, 2, heap)

        self.build_robot_and_add_to_heap(self.blueprint.geode_cost, 3, heap)

        number_of_minutes_remaining = self.blueprint.max_minutes - self.minute

        return self.resources[3] + self.robots[3] * number_of_minutes_remaining
    
    def possible_max_geodes(
        self
    ):
        current_geode_robots = self.robots[3]
        current_geodes = self.resources[3]

        minutes_remaining = self.blueprint.max_minutes - self.minute

        return minutes_remaining * current_geode_robots + current_geodes + ((minutes_remaining * (minutes_remaining + 1)) // 2)
    
    def __hash__(self):
        return hash(
            (
                self.robots[0],
                self.robots[1],
                self.robots[2],
                self.robots[3],
                self.resources[0], 
                self.resources[1], 
                self.resources[2], 
                self.resources[3]
            )
        )
    

class BlueprintStateQueue:
    def __init__(self):
        self.queue = []
        self.count = 0
        self.max_value = 0
        self.processed = {}

    def store_initial_value(self, state):
        self.max_value = state.possible_max_geodes()

        self.store_state(state)    

    def store_state(self, state):
        cost = state.possible_max_geodes()
        new_entry = (self.max_value - cost, self.count, state)

        heapq.heappush(self.queue, new_entry)
        self.count += 1

    def get_highest_estimate_node(self):
        while len(self.queue) > 0:
            cost, count, state = heapq.heappop(self.queue)
            if state not in self.processed or state.minute < self.processed[state]:
                self.processed[state] = state.minute
                
                return self.max_value - cost, state
        return 0, None
    
def get_costs_from_line(line):
    costs = []
    for cost_section in line.split(". "):
        ore_cost_parse = re.search(r"(\d+) ore", cost_section)
        if ore_cost_parse is None:
            ore_cost = 0
        else:
            ore_cost = int(ore_cost_parse.group(1))
            
        clay_cost_parse = re.search(r"(\d+) clay", cost_section)
        if clay_cost_parse is None:
            clay_cost = 0
        else:
            clay_cost = int(clay_cost_parse.group(1))
            
        obsidian_cost_parse = re.search(r"(\d+) obsidian", cost_section)
        if obsidian_cost_parse is None:
            obsidian_cost = 0
        else:
            obsidian_cost = int(obsidian_cost_parse.group(1))

        costs.append((ore_cost, clay_cost, obsidian_cost))

    return costs

@register(19, 2022, 1, True)
def not_enough_minerals_1(split_text):
    total_quality_level = 0
    for i, line in enumerate(split_text):
        blueprint_number = int(i) + 1

        costs = get_costs_from_line(line)
        
        blueprint = Blueprint(
            *costs
        )

        queue = BlueprintStateQueue()

        queue.store_initial_value(
            blueprint.get_first_state()
        )

        max_geode_count = 0

        while len(queue.queue) > 0:
            possible_max_geodes, this_blueprint = queue.get_highest_estimate_node()

            if possible_max_geodes < max_geode_count:
                break

            geode_count = this_blueprint.add_next_states_to_heap(
                queue
            )
            
            if geode_count > max_geode_count:
                max_geode_count = geode_count
        
        total_quality_level += max_geode_count * blueprint_number
    
    return total_quality_level


@register(19, 2022, 2, True)
def not_enough_minerals_2(split_text):
    total_geode_count = 1
    for line in split_text[:3]:
        costs = get_costs_from_line(line)
        
        blueprint = Blueprint(
            *costs,
            32
        )

        queue = BlueprintStateQueue()

        queue.store_initial_value(
            blueprint.get_first_state()
        )

        max_geode_count = 0

        while len(queue.queue) > 0:
            possible_max_geodes, this_blueprint = queue.get_highest_estimate_node()

            if possible_max_geodes < max_geode_count:
                break

            geode_count = this_blueprint.add_next_states_to_heap(
                queue
            )
            
            if geode_count > max_geode_count:
                max_geode_count = geode_count
        
        total_geode_count *= max_geode_count
    
    return total_geode_count