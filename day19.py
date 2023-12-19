from aocd import get_data
import re
class Rule:
    def __init__(
    self,
    property,
    comparison,
    count,
    destination):
        self.property = property
        self.comparison = comparison
        self.count = count
        self.destination = destination

    def process(self, part):
        object_count = part[self.property]

        if self.comparison == ">":
            if object_count > self.count:
                return self.destination
            else:
                return None
        elif self.comparison == "<":
            if object_count < self.count:
                return self.destination
            else:
                return None

class Workflow:
    def __init__(
        self,
        rules,
        final_destination):
        self.rules = rules
        self.final_destination = final_destination
        
    def process_rules(self, part):
        for rule in self.rules:
            result = rule.process(part)
            if result is not None:
                return result
        return self.final_destination
            

def workflow_1(text):
    workflows = {}

    parts = []

    finished_workflows = False

    for line in text.split("\n"):
        if line == "":
            finished_workflows = True
        elif finished_workflows:
            regexed_part = re.search(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)", line)

            parts.append({
                "x": int(regexed_part.group(1)),
                "m": int(regexed_part.group(2)),
                "a": int(regexed_part.group(3)),
                "s": int(regexed_part.group(4)),
            })
        else:
            regex_workflow = re.match(r"(\w+)\{(.*)\}", line)
            workflow_name = regex_workflow.group(1)

            split_rules = regex_workflow.group(2).split(',')

            rules = []

            for i in range(len(split_rules) - 1):
                regex_rule = re.match(r"([amsx])([<>])(\d+):(\w+)", split_rules[i])

                rules.append(Rule(
                    regex_rule.group(1),
                    regex_rule.group(2),
                    int(regex_rule.group(3)),
                    regex_rule.group(4),

                ))

            final_destination = re.match(r"(\w+)", split_rules[-1]).group(1)

            workflows[workflow_name] = Workflow(
                rules,
                final_destination)

    total = 0

    for part in parts:
        workflow = "in"
        while (workflow != "A" and workflow != "R"):
            workflow = workflows[workflow].process_rules(part)

        if workflow == "A":
            total += part["x"] + part["m"] + part["a"] + part["s"]
 
    return total

workflow_text = get_data(day=19, year=2023)  
print(workflow_1(workflow_text))