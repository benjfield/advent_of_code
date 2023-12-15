from aocd import get_data
import re
from collections import OrderedDict

def hash_function(text):
    result = 0
    for char in text:
        result += ord(char)
        result = result * 17
        result = result%256
    return result

def hash_1(text):
    hashes = []

    for label in text.split(","):
        hashes.append(label)

    results = []
    for hash in hashes:
        results.append(hash_function(hash))

    return sum(results)

def hash_2(text):
    labels = []

    for label in text.split(","):
        parsed_text = re.match(r"(.*)([=|-])(\d*)", label)

        if parsed_text is None:
            print(label)
        else:
            labels.append({
                "label": parsed_text.group(1),
                "operation": parsed_text.group(2),
                "focal_length": parsed_text.group(3),
            })

    for label in labels:
        label["hash"] = hash_function(label["label"])

    boxes = []

    for i in range(256):
        boxes.append(OrderedDict())

    for label in labels:
        if label["operation"] == "-":
            if label["label"] in boxes[label["hash"]]:
                boxes[label["hash"]].pop(label["label"])
        else:
            boxes[label["hash"]][label["label"]] = label

    focal_length = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box.values()):
            focal_length += (1 + i) * (1 + j) * int(lens["focal_length"])

    return focal_length

hash_text = get_data(day=15, year=2023)
print(hash_2(hash_text))