from advent.runner import register
from advent.utils.path_finding import Node

@register(18, 2019, 1)
def keys_1(text):
    for y, row in enumerate(text.split("\n")):
        for x, tile in enumerate(row):
            pass