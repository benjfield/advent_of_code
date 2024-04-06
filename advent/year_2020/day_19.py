from advent.runner import register
import re
import math

class NotAllCompiledException(Exception):
    pass

class Rule:
    def __init__(
        self,
        rule_name,
        base_rule=None,
        underlying_rules_strings=None
    ):
        self.rule_name = rule_name
        self.underlying_rules_strings = underlying_rules_strings
        self.underlying_rules = []
        self.base_rule = base_rule

    def build_underlying_rules(self, rules_dict):
        if self.underlying_rules_strings is not None:
            for rule_set in self.underlying_rules_strings:
                self.underlying_rules.append([])
                for rule in rule_set:
                    self.underlying_rules[-1].append(rules_dict[rule])

    def test_message(self, messages):
        valid_next_messages = set()
        for message in messages:
            if self.base_rule is not None:
                if len(message) > 0 and message[0] == self.base_rule:
                    valid_next_messages.add(message[1:])
            else:
                for rule_set in self.underlying_rules:
                    messages_to_test = [message]
                    for rule in rule_set:
                        messages_to_test = rule.test_message(messages_to_test)
                        if len(messages_to_test) == 0:
                            break

                    for valid_message in messages_to_test:
                        valid_next_messages.add(valid_message)
        
        return valid_next_messages

def check_messages(split_text, rule_type):    
    rules_dict = {}
    building_rules = True
    messages = []
    for line in split_text:
        if len(line) == 0:
            building_rules = False
        elif building_rules:
            split_by_colon = line.split(":")
            rule_name = split_by_colon[0]
            rules = split_by_colon[1].strip()
            letter_match = re.match(r"\"(.+)\"", rules)
            if letter_match is not None:
                rules_dict[rule_name] = rule_type(rule_name=rule_name, base_rule=letter_match.group(1))
            else:
                underlying_rule_strings = [[]]
                for rule in rules.split(" "):
                    if rule == "|":
                        underlying_rule_strings.append([])
                    else:
                        underlying_rule_strings[-1].append(rule)
                rules_dict[rule_name] = rule_type(rule_name=rule_name, underlying_rules_strings=underlying_rule_strings)
        else:
            messages.append(line)

    for rule in rules_dict.values():
        rule.build_underlying_rules(rules_dict)

    valid_count = 0
    for message in messages:
        valid_messages = rules_dict["0"].test_message([message])
        if "" in valid_messages:
            valid_count += 1

    return valid_count

@register(19, 2020, 1, True)
def monster_messages_1(split_text):
    return check_messages(split_text, Rule)

class LoopingRule(Rule): 
    def test_message(self, messages):
        valid_next_messages = set()
        for message in messages:
            if self.base_rule is not None:
                if len(message) > 0 and message[0] == self.base_rule:
                    valid_next_messages.add(message[1:])
            else:
                if self.rule_name == "8":
                    messages_to_test = [message]
                    suffix_rule = self.underlying_rules[0][0]
                    while len(messages_to_test) > 0:
                        messages_to_test = suffix_rule.test_message(messages_to_test)
                        for valid_message in messages_to_test:
                            valid_next_messages.add(valid_message)       
                elif self.rule_name == "11":  
                    messages_to_test = [message]
                    prefix_rule = self.underlying_rules[0][0]
                    suffix_rule = self.underlying_rules[0][1]
                    prefix_count = 0
                    while len(messages_to_test) > 0:
                        messages_to_test = prefix_rule.test_message(messages_to_test)
                        prefix_count += 1

                        messages_to_test_suffixes = messages_to_test.copy()
                        for i in range(prefix_count):
                            messages_to_test_suffixes = suffix_rule.test_message(messages_to_test_suffixes)
                            
                        for valid_message in messages_to_test_suffixes:
                            valid_next_messages.add(valid_message)
                else:
                    for rule_set in self.underlying_rules:
                        messages_to_test = [message]
                        for rule in rule_set:
                            messages_to_test = rule.test_message(messages_to_test)
                            if len(messages_to_test) == 0:
                                break

                        for valid_message in messages_to_test:
                            valid_next_messages.add(valid_message)
        
        return valid_next_messages  

@register(19, 2020, 2, True)
def monster_messages_2(split_text):
    return check_messages(split_text, LoopingRule)