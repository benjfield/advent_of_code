import re
from advent.runner import register
class Rule:
    def __init__(
    self,
    property,
    comparison,
    count,
    positive_destination,
    negative_destination):
        self.property = property
        self.comparison = comparison
        self.count = count
        self.positive_destination = positive_destination
        self.negative_destination = negative_destination

    def __str__(self):
        return f'{self.property}{self.comparison}{self.count} {self.positive_destination} {self.negative_destination}'

    def process(self, part):
        object_count = part[self.property]

        if self.comparison == ">":
            if object_count > self.count:
                return self.positive_destination
            else:
                return self.negative_destination
        elif self.comparison == "<":
            if object_count < self.count:
                return self.positive_destination
            else:
                return self.negative_destination

    def process_recursively(self, part, rules):
        destination = self.process(part)

        if destination == "A" or destination == "R":
            return destination
        else:
            return rules[destination].process_recursively(part, rules)

    def compile_rule(self, rules):
        rules_to_return = []

        if self.positive_destination == "A":
            new_rule = CompiledRule()
            new_rule.add_rule(self)
            rules_to_return.append(new_rule)
        elif self.positive_destination == "R":
            pass
        else:
            underlying_compiled_rules = rules[self.positive_destination].compile_rule(rules)
            for compiled_rule in underlying_compiled_rules:
                compiled_rule.add_rule(self)
            rules_to_return += underlying_compiled_rules

        if self.negative_destination == "A":
            new_rule = CompiledRule()
            new_rule.add_rule(self, False)
            rules_to_return.append(new_rule)
        elif self.negative_destination == "R":
            pass
        else:
            underlying_compiled_rules = rules[self.negative_destination].compile_rule(rules)
            for compiled_rule in underlying_compiled_rules:
                compiled_rule.add_rule(self, False)
            rules_to_return += underlying_compiled_rules
        
        return rules_to_return


class CompiledRule:
    def __init__(self):
        self.x_min = 1
        self.x_max = 4000
        self.m_min = 1
        self.m_max = 4000
        self.a_min = 1
        self.a_max = 4000
        self.s_min = 1
        self.s_max = 4000

    def __str__(self):
        return f"{self.x_min}<=x<={self.x_max},{self.m_min}<=m<={self.m_max},{self.a_min}<=a<={self.a_max},{self.s_min}<=s<={self.s_max}"

    def add_rule(self, rule, positive = True):
        if rule.comparison == ">":
            if positive:
                property_name = f"{rule.property}_min"
                setattr(self, property_name, max(getattr(self,property_name), rule.count + 1))
            else:
                property_name = f"{rule.property}_max"
                setattr(self, property_name, min(getattr(self,property_name), rule.count))
        else:
            if positive:
                property_name = f"{rule.property}_max"
                setattr(self, property_name, min(getattr(self,property_name), rule.count - 1))
            else:
                property_name = f"{rule.property}_min"
                setattr(self, property_name, max(getattr(self,property_name), rule.count ))

    def is_valid(self):
        return (self.x_max > self.x_min) and (self.m_max > self.m_min) and (self.a_max > self.a_min) and (self.s_max > self.s_min)

    def total_possibilities(self):
        return (self.x_max - self.x_min + 1) * (self.m_max - self.m_min + 1) * (self.a_max - self.a_min + 1) * (self.s_max - self.s_min + 1) 

    def share_pool_size(self, other_rule):
        shared_x_min = max(self.x_min, other_rule.x_min)
        shared_x_max = min(self.x_max, other_rule.x_max)
        shared_m_min = max(self.m_min, other_rule.m_min)
        shared_m_max = min(self.m_max, other_rule.m_max)
        shared_a_min = max(self.a_min, other_rule.a_min)
        shared_a_max = min(self.a_max, other_rule.a_max)
        shared_s_min = max(self.s_min, other_rule.s_min)
        shared_s_max = min(self.s_max, other_rule.s_max)
        if (shared_x_min <= shared_x_max) and (shared_m_min <= shared_m_max) and (shared_a_min <= shared_a_max) and (shared_s_min <= shared_s_max):
            return True

def generate_parts_and_rules(text):
    parts = []

    rules = {}

    finished_workflows = False

    for line in text.split("\n"):
        if line == "":
            finished_workflows = True
        elif finished_workflows:
            regexed_part = re.search(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)", line)
            print(line)
            parts.append({
                "x": int(regexed_part.group(1)),
                "m": int(regexed_part.group(2)),
                "a": int(regexed_part.group(3)),
                "s": int(regexed_part.group(4)),
            })
        else:
            regex_workflow = re.match(r"(\w+)\{(.*)\,(\w+)}", line)
            workflow_name = regex_workflow.group(1)

            split_rules = regex_workflow.group(2).split(',')

            final_destination = regex_workflow.group(3)

            for i, split_rule in enumerate(split_rules):
                regex_rule = re.match(r"([amsx])([<>])(\d+):(\w+)", split_rule)

                if i == 0:
                    rule_name = f"{workflow_name}"
                else:
                    rule_name = f"{workflow_name}_{i}"
                
                if i == len(split_rules) - 1:
                    negative_destination = final_destination
                else:
                    negative_destination = f"{workflow_name}_{i + 1}"

                rules[rule_name] = Rule(
                        regex_rule.group(1),
                        regex_rule.group(2),
                        int(regex_rule.group(3)),
                        regex_rule.group(4),
                        negative_destination
                    )
    return parts, rules

@register(19, 2023, 1)
def workflow_1(text):
    parts, rules = generate_parts_and_rules(text)

    total = 0

    for part in parts:        
        workflow = rules["in"].process_recursively(part, rules)

        if workflow == "A":
            total += part["x"] + part["m"] + part["a"] + part["s"]
 
    return total

@register(19, 2023, 2)
def workflow_2(text):
    parts, rules = generate_parts_and_rules(text)

    total = 0

    compiled_rules = rules["in"].compile_rule(rules)

    valid_rules = [] 

    for compiled_rule in compiled_rules:
        if compiled_rule.is_valid():
            valid_rules.append(compiled_rule)
    
    for compiled_rule in valid_rules:
        total += compiled_rule.total_possibilities()
 
    for i in range(len(valid_rules)):
        for j in range(i + 1, len(valid_rules)):
          if valid_rules[i].share_pool_size(valid_rules[j]):
              print(valid_rules[i])
              print(valid_rules[j])
              raise Exception("blah")

    return total