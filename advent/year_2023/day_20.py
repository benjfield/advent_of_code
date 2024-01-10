from enum import Enum
import re
import math
from advent.runner import register

class Pulse(Enum):
    HIGH = 0
    LOW = 1

class Node:
    def __init__(self, name, target_labels):
        self.name = name
        self.target_labels = target_labels
        self.targets = []
        self.inputs = []
        self.input_chain = None
        self.input_state_storage = {}
        self.period = 0


    def __str__(self):
        return f"{self.name}"
    
    def populate_initial_pulses(self, input_labels, node_dict):
        for label in input_labels:
            self.inputs.append(node_dict[label])

    def set_targets(self, node_dict):
        for label in self.target_labels:
            self.targets.append(node_dict[label])

    def receive_pulse(self, sender_name, pulse):
        return None
    
    def number_of_states(self):
        return 1
    
    def get_input_chain(self, input_chain=[]):
        if self.input_chain != None:
            return list(set(self.input_chain + input_chain))
        if self.name in input_chain:
            return input_chain
        else:
            input_chain.append(self.name)
            if len(self.inputs) == 0:
                return input_chain
            else:
                for input in self.inputs:
                    input_chain += input.get_input_chain(input_chain)
                    input_chain = list(set(input_chain))
                return input_chain
    
    def store_input_chain(self):
        self.input_chain = self.get_input_chain([])

    def store_upwards_state(self, node_dict, run_count):
        if self.period != 0:
            return True
        else:
            states = []
            underlying_periods = []
            all_dependendents_calculated = True
            for node in self.input_chain:
                input_node = node_dict[node]
                states.append(str(node_dict[node]))
                if input_node.period == 0 and input_node.name != self.name:
                    all_dependendents_calculated = False
            
            if all_dependendents_calculated:
                periods = []
                for node in self.input_chain:
                    input_node = node_dict[node]
                    if input_node.name != self.name:
                        periods.append(input_node.period)
                
                if len(periods) == 0:
                    self.period = 1
                else:
                    self.period = math.lcm(*periods)
                return True
            else:
                states_tuple = tuple(states)
                if states_tuple in self.input_state_storage:
                    self.period = run_count - self.input_state_storage[states_tuple]
                    return True
                else:
                    self.input_state_storage[states_tuple] = run_count
                    return False

class FlipFlop(Node):
    def __init__(self, name, target_labels):
        super().__init__(name, target_labels)
        self.on = False

    def __str__(self):
        return f"{self.name}: {self.on}"


    def receive_pulse(self, sender_name, pulse):
        if pulse == Pulse.HIGH:
            return None
        else:              
            if self.on:
                self.on = False
                return self.targets, Pulse.LOW, self.name
            else:
                self.on = True
                return self.targets, Pulse.HIGH, self.name
            
    def number_of_states(self):
        return 2

class Conjunction(Node):
    def __init__(self, name, target_labels):
        super().__init__(name, target_labels)
        self.last_pulses = {}

    def __str__(self):
        self_string = f"{self.name}:"

        for input, pulse in self.last_pulses.items():
            self_string += f" {input} {pulse}"
        
        return self_string

    def populate_initial_pulses(self, input_labels, node_dict):
        super().populate_initial_pulses(input_labels, node_dict)
        for input in input_labels:
            self.last_pulses[input] = Pulse.LOW

    def receive_pulse(self, sender_name, pulse):
        self.last_pulses[sender_name] = pulse

        all_high = True
        for last_pulse in self.last_pulses.values():
            if last_pulse == Pulse.LOW:
                all_high = False
                break

        if all_high:
            return self.targets, Pulse.LOW, self.name
        else:
            return self.targets, Pulse.HIGH, self.name
        
    def number_of_states(self):
        return 2 ** len(self.last_pulses)

def initial_node_creation(text):
    broadcaster = Node("broadcaster", [])
    node_dict = {"broadcaster": broadcaster}

    reverse_nodes = {}

    intial_targets = []

    for line in text.split("\n"):
        line_parse = re.match(r"(%\w+|&\w+|broadcaster) -> (.*)", line)

        target_labels = []

        for label in line_parse.group(2).split(","):
            target_labels.append(label.strip())

        node_description = line_parse.group(1)

        if node_description == "broadcaster":
            node_name = "broadcaster"
            intial_targets = target_labels
        else:
            node_name = node_description[1:]
            if node_description[0] =="%":
                node_dict[node_name] = FlipFlop(node_name, target_labels)
            else:
                node_dict[node_name] = Conjunction(node_name, target_labels)
            
        for target_label in target_labels:
            if target_label in reverse_nodes:
                reverse_nodes[target_label].append(node_name)
            else:
                reverse_nodes[target_label] = [node_name]

    return node_dict, reverse_nodes, intial_targets

@register(20, 2023, 1)
def pulse_1(text):
    node_dict, reverse_nodes, intial_targets = initial_node_creation(text)

    for node_name, inputs in reverse_nodes.items():
        if node_name not in node_dict:
            end_node = Node(node_name, [])
            node_dict[node_name] = end_node
        else:
            node_dict[node_name].populate_initial_pulses(inputs, node_dict)

    initial_signals = []

    for target in intial_targets:
        initial_signals.append(([node_dict[target]], Pulse.LOW, "broadcaster"))

    nodes = []

    for node in node_dict.values():
        node.set_targets(node_dict)
        nodes.append(node)

    signal_results = {}

    i = 0

    for i in range(1000):
        low_count = 1
        high_count = 0
        signals = initial_signals
        while len(signals) > 0:
            new_signals = []
            for signal in signals:
                for target in signal[0]:
                    if signal[1] == Pulse.LOW:
                        low_count += 1
                    else:
                        high_count += 1
                    #print(f"{signal[2]} -{signal[1]}-> {target.name}")
                    returned_signal = target.receive_pulse(signal[2], signal[1])
                    if returned_signal is not None:
                        new_signals.append(returned_signal)
            signals = new_signals

        node_strings = []
        for node in nodes:
            node_strings.append(str(node))
        
        node_strings_tuple = tuple(node_strings)

        if node_strings_tuple in signal_results:
            prior_count = signal_results[node_strings_tuple]["count"]
            low_prior_total = 0
            high_prior_total = 0

            low_cycle_total = 0
            high_cycle_total = 0

            cycle_length = i - prior_count

            extras = (1000 - prior_count)%cycle_length 
            cycle_count = int((1000 - prior_count)/cycle_length)

            extras_low_total = 0
            extras_high_total = 0

            for values in signal_results.values():
                if values["count"] >= prior_count:
                    low_cycle_total += values["low"]
                    high_cycle_total += values["high"]
                    if values["count"] < prior_count + extras:
                        extras_low_total += values["low"]
                        extras_high_total += values["high"]
                else: 
                    low_prior_total += values["low"]
                    high_prior_total += values["high"]

            low_total = low_prior_total + low_cycle_total*cycle_count + extras_low_total
            high_total = high_prior_total + high_cycle_total*cycle_count + extras_high_total

            return low_total * high_total
        else:
            signal_results[node_strings_tuple] = {
                "count": i,
                "low": low_count,
                "high": high_count
            }

            signals = new_signals

    low_total = 0
    high_total = 0

    for values in signal_results.values():
        low_total += values["low"]
        high_total += values["high"]

    return low_total * high_total

@register(20, 2023, 2)
def pulse_2(text):
    node_dict, reverse_nodes, intial_targets = initial_node_creation(text)

    for node_name, inputs in reverse_nodes.items():
        if node_name not in node_dict:
            end_node = Node(node_name, [])
            node_dict[node_name] = end_node

        node_dict[node_name].populate_initial_pulses(inputs, node_dict)

    initial_signals = []

    for target in intial_targets:
        initial_signals.append(([node_dict[target]], Pulse.LOW, "broadcaster"))


    i = 0

    for node in node_dict.values():
        node.set_targets(node_dict)
        node.store_input_chain()
        node.store_upwards_state(node_dict, i)

    while True:
        signals = initial_signals
        while len(signals) > 0:
            new_signals = []
            for signal in signals:
                for target in signal[0]:
                    #print(f"{signal[2]} -{signal[1]}-> {target.name}")
                    returned_signal = target.receive_pulse(signal[2], signal[1])
                    if returned_signal is not None:
                        new_signals.append(returned_signal)
            signals = new_signals
        i += 1
        found_all_periods = True
        for node in node_dict.values():
            found_period = node.store_upwards_state(node_dict, i)
            found_all_periods = found_period and found_all_periods
        if found_all_periods:
            for node in node_dict.values():
                print(f"{node.name} {node.period}")
            return node_dict["rx"].period
            