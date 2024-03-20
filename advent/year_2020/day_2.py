from advent.runner import register
import re

@register(2, 2020, 1, True)
def password_report_1(split_text):
    correct_passwords = 0
    for line in split_text:
        matched_line = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
        
        char_count = {}
        for char in matched_line.group(4):
            char_count[char] = char_count.get(char, 0) + 1
        
        if matched_line.group(3) in char_count and char_count[matched_line.group(3)] >= int(matched_line.group(1)) and char_count[matched_line.group(3)] <= int(matched_line.group(2)):
            correct_passwords += 1
        
    return correct_passwords

@register(2, 2020, 2, True)
def password_report_2(split_text):
    correct_passwords = 0
    for line in split_text:
        matched_line = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
        
        letter_count = 0
        if matched_line.group(4)[int(matched_line.group(1)) - 1] == matched_line.group(3):
            letter_count += 1

        if matched_line.group(4)[int(matched_line.group(2)) - 1] == matched_line.group(3):
            letter_count += 1
        
        if letter_count == 1:
            correct_passwords += 1
        
    return correct_passwords
