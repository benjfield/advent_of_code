import graphviz
import re
from aocd import get_data

class Node:
    def __init__(self, name):
        self.name = name
        self.target_labels = []
        self.targets = []


    def __str__(self):
        return f"{self.name}"
    
    def set_targets(self, node_dict):
        for label in self.target_labels:
            target = node_dict[label]
            self.targets.append(node_dict[label])

            target.targets.append(self)

    def get_target_chain(self, target_chain=[]):
        if self.name in target_chain:
            return target_chain
        else:
            target_chain.append(self.name)
            if len(self.targets) == 0:
                return target_chain
            else:
                for target in self.targets:
                    target_chain += target.get_target_chain(target_chain)
                    target_chain = list(set(target_chain))
                return target_chain

def overload_1(text):
    node_dict = {}
    dot = graphviz.Graph(engine="neato")
    for line in text.split("\n"):
        parsed_line = re.match(r"(\w+): (.*)", line)
        base = parsed_line.group(1)
        dot.node(base)

        base_node = Node(base)
        
        if base not in node_dict:
            base_node = Node(base)
            node_dict[base] = base_node
        else:
            base_node = node_dict[base]

        for link in re.findall(r"(\w+)", parsed_line.group(2)):
            dot.node(link)

            if (base == "qns" and link == "jxm") or (link == "qns" and base == "jxm") or (base == "tjd" and link == "dbt") or (link == "tjd" and base == "dbt") or (base == "mgb" and link == "plt") or (link == "mgb" and base == "plt"):
                pass
            else:
                dot.edge(base, link)

                if link not in node_dict:
                    link_node = Node(link)
                    node_dict[link] = link_node
                else:
                    link_node = node_dict[link]

                base_node.targets.append(link_node)
                link_node.targets.append(base_node)

    #dot.render('doctest-output/day25.gv', view=True)
                
    cluster_size = len(node_dict["qns"].get_target_chain())

    total_size = len(node_dict.values())

    return (total_size - cluster_size) * cluster_size

overload_text = get_data(day=25, year=2023)
print(overload_1(overload_text))    
