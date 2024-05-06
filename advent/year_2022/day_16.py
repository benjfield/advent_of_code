import re
import heapq
from advent.runner import register

def parse_valves(split_text):
    paths = {}
    valve_rates = {}

    for line in split_text:
        parsed_line = re.search(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line)

        valve_rate = int(parsed_line.group(2))

        if valve_rate > 0:
            valve_rates[parsed_line.group(1)] = int(parsed_line.group(2))

        paths[parsed_line.group(1)] = parsed_line.group(3).split(", ")

    valve_index = {}
    for i, valve in enumerate(valve_rates.keys()):
        valve_index[valve] = 2 ** i

    return paths, valve_rates, valve_index


class ValveStateQueue:
    def __init__(self):
        self.queue = []
        self.count = 0
        self.max_value = 0
        self.processed = {}

    def store_initial_value(self, state, cost):
        self.max_value = cost

        self.store_state(state, cost)    

    def store_state(self, state, cost):
        new_entry = (self.max_value - cost, self.count, state)

        heapq.heappush(self.queue, new_entry)
        self.count += 1

    def get_highest_estimate_node(self):
        while len(self.queue) > 0:
            cost, count, state = heapq.heappop(self.queue)

            if state not in self.processed or state.time_remaining < self.processed[state]:
                self.processed[state] = state.time_remaining
                
                return self.max_value - cost, state
        return 0, None
    
class ValveState:
    def __init__(
        self,
        location,
        on_valves,
        time_remaining,
        flow_count,
        valve_indexes
        ):
        self.location = location
        self.on_valves = on_valves
        self.time_remaining = time_remaining
        self.flow_count = flow_count

        on_valve_bitmask = 0
        for valve in self.on_valves:
            on_valve_bitmask += valve_indexes[valve]

        self.on_valve_bitmask = on_valve_bitmask

    def add_neighbours_to_queue(
            self,
            queue,
            valve_rates,
            paths,
            valve_indexes):
        time_remaining_next = self.time_remaining - 1
        if self.location not in self.on_valves and self.location in valve_rates:
            destinations = [self.location] + paths[self.location]
        else:
            destinations = paths[self.location]
        
        for destination in destinations:
            if destination == self.location:
                next_on_valves = self.on_valves.copy()
                next_on_valves.add(self.location)

                next_flow_count = self.flow_count + valve_rates[self.location] * time_remaining_next
            else:
                next_on_valves = self.on_valves

                next_flow_count = self.flow_count

            neighbour = ValveState(
                destination,
                next_on_valves,
                time_remaining_next,
                next_flow_count,
                valve_indexes
            )

            possible_remaining = neighbour.give_max_possible_flow_count(valve_rates)

            queue.store_state(
                neighbour,
                next_flow_count + possible_remaining,
            )

    def give_max_possible_flow_count(
            self,
            valve_rates,
        ):
        if self.time_remaining != 0:
            closed_valve_rates = []
            if self.location not in self.on_valves and self.location in valve_rates:
                total_remaining = valve_rates[self.location] * self.time_remaining
            else:
                total_remaining = 0
                
            for valve, rate in valve_rates.items():
                if valve not in self.on_valves and valve != self.location:
                    closed_valve_rates.append(rate)

            closed_valve_rates.sort(reverse=True)

            for i, rate in enumerate(closed_valve_rates):
                time_remaining_for_rate = (self.time_remaining - 2 * (i + 1))

                if time_remaining_for_rate > 0:
                    total_remaining += rate * time_remaining_for_rate
        
            return total_remaining
        else:
            return 0
        
    def __hash__(self):
        return hash((self.location, self.on_valve_bitmask, self.flow_count))

    def __eq__(self, other):
        if self.location == other.location and self.on_valve_bitmask == other.on_valve_bitmask and self.flow_count == other.flow_count:
            return True
        return False

@register(16, 2022, 1, True)
def proboscidea_volcanium_1(split_text):
    paths, valve_rates, valve_indexes = parse_valves(split_text)

    initial_state = ValveState(
        "AA",
        set(),
        30,
        0,
        valve_indexes
    )

    max_intital_estimate = initial_state.give_max_possible_flow_count(valve_rates)

    state_queue = ValveStateQueue()

    state_queue.store_initial_value(initial_state, max_intital_estimate)

    max_flow = 0

    while len(state_queue.queue) > 0:
        estimated_flow, state = state_queue.get_highest_estimate_node()

        if estimated_flow < max_flow:
            return max_flow
        
        if state.flow_count > max_flow:
            max_flow = state.flow_count

        if len(state.on_valves) != len(valve_rates) and state.time_remaining > 0:
            state.add_neighbours_to_queue(
                state_queue,
                valve_rates,
                paths,
                valve_indexes
            )

    return max_flow

class ValveElephantState:
    def __init__(
        self,
        your_location,
        elephant_location,
        on_valves,
        time_remaining,
        flow_count,
        valve_indexes
        ):

        locations = [your_location, elephant_location]

        locations.sort()

        self.your_location = locations[0]
        self.elephant_location = locations[1]
        self.on_valves = on_valves
        self.time_remaining = time_remaining
        self.flow_count = flow_count

        on_valve_bitmask = 0
        for valve in self.on_valves:
            on_valve_bitmask += valve_indexes[valve]

        self.on_valve_bitmask = on_valve_bitmask

    def add_neighbours_to_queue(
            self,
            queue,
            valve_rates,
            paths,
            valve_indexes):
        time_remaining_next = self.time_remaining - 1

        if self.your_location not in self.on_valves and self.your_location in valve_rates:
            your_destinations = [self.your_location] + paths[self.your_location]
        else:
            your_destinations = paths[self.your_location]

        if self.elephant_location not in self.on_valves and self.elephant_location in valve_rates and self.elephant_location != self.your_location:
            elephant_destinations = [self.elephant_location] + paths[self.elephant_location]
        else:
            elephant_destinations = paths[self.elephant_location]


        for your_destination in your_destinations:
            for elephant_destination in elephant_destinations:
                if your_destination == self.your_location:
                    your_on_valves = self.on_valves.copy()
                    your_on_valves.add(your_destination)
            
                    your_flow_count = self.flow_count + valve_rates[your_destination] * time_remaining_next
                else:
                    your_on_valves = self.on_valves
                    your_flow_count = self.flow_count

                if elephant_destination == self.elephant_location:
                    next_on_valves = your_on_valves.copy()
                    next_on_valves.add(elephant_destination)

                    next_flow_count = your_flow_count + valve_rates[elephant_destination] * time_remaining_next
                else:
                    next_on_valves = your_on_valves
                    next_flow_count = your_flow_count

                neighbour = ValveElephantState(
                    your_destination,
                    elephant_destination,
                    next_on_valves,
                    time_remaining_next,
                    next_flow_count,
                    valve_indexes
                )

                possible_remaining = neighbour.give_max_possible_flow_count(valve_rates)

                queue.store_state(
                    neighbour,
                    next_flow_count + possible_remaining,
                )

    def give_max_possible_flow_count(
            self,
            valve_rates,
        ):
        if self.time_remaining != 0:
            closed_valve_rates = []
            if self.your_location not in self.on_valves and self.your_location in valve_rates:
                total_remaining = valve_rates[self.your_location] * self.time_remaining
            else:
                total_remaining = 0

            if self.elephant_location not in self.on_valves and self.elephant_location in valve_rates and self.your_location != self.elephant_location:
                total_remaining += valve_rates[self.elephant_location] * self.time_remaining
                
            for valve, rate in valve_rates.items():
                if valve not in self.on_valves and valve != self.your_location and valve != self.elephant_location:
                    closed_valve_rates.append(rate)

            closed_valve_rates.sort(reverse=True)

            for i, rate in enumerate(closed_valve_rates):
                #time_remaining_for_rate = self.time_remaining
                time_remaining_for_rate = (self.time_remaining - 2 * ((i // 2) + 1))

                if time_remaining_for_rate > 0:
                    total_remaining += rate * time_remaining_for_rate
        
            return total_remaining
        else:
            return 0
             
    def __hash__(self):
        return hash((self.your_location, self.elephant_location, self.on_valve_bitmask, self.flow_count))

    def __eq__(self, other):
        if self.your_location == other.your_location and self.elephant_location == other.elephant_location and self.on_valve_bitmask == other.on_valve_bitmask and self.flow_count == other.flow_count:
            return True
        return False
      
@register(16, 2022, 2, True)
def proboscidea_volcanium_2(split_text):
    paths, valve_rates, valve_indexes = parse_valves(split_text)

    initial_state = ValveElephantState(
        "AA",
        "AA",
        set(),
        26,
        0,
        valve_indexes
    )

    max_intital_estimate = initial_state.give_max_possible_flow_count(valve_rates)

    state_queue = ValveStateQueue()

    state_queue.store_initial_value(initial_state, max_intital_estimate)

    max_flow = 0

    while len(state_queue.queue) > 0:
        estimated_flow, state = state_queue.get_highest_estimate_node()

        if estimated_flow < max_flow:
            return max_flow
        
        if state.flow_count > max_flow:
            max_flow = state.flow_count

        if len(state.on_valves) != len(valve_rates) and state.time_remaining > 0:
            state.add_neighbours_to_queue(
                state_queue,
                valve_rates,
                paths,
                valve_indexes
            )

    return max_flow