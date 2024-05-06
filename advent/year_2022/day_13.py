from advent.runner import register
from enum import Enum
from functools import cmp_to_key

class CorrectOrderEnum(Enum):
    YES = 1
    NO = 2
    MAYBE = 3

def check_order(object_1, object_2):
    for i in range(len(object_1)):
        if i >= len(object_2):
            return CorrectOrderEnum.NO
        if (type(object_1[i]) == list and type(object_2[i]) == int):
            object_2[i] = [object_2[i]]
        elif (type(object_2[i]) == list and type(object_1[i]) == int):
            object_1[i] = [object_1[i]]

        if type(object_1[i]) == list and type(object_2[i]) == list:
            valid_order = check_order(object_1[i], object_2[i])

            if valid_order != CorrectOrderEnum.MAYBE:
                return valid_order
        else:
            if object_2[i] < object_1[i]:
                return CorrectOrderEnum.NO
            elif object_2[i] > object_1[i]:
                return CorrectOrderEnum.YES
    
    if len(object_1) == len(object_2):
        return CorrectOrderEnum.MAYBE
    return CorrectOrderEnum.YES

@register(13, 2022, 1, True)
def distress_signal_1(split_text):
    total_indices = 0
    for i in range(0, len(split_text), 3):
        object_1 = eval(split_text[i])
        object_2 = eval(split_text[i + 1])
        correct_order = check_order(object_1, object_2)
        if correct_order == CorrectOrderEnum.MAYBE:
            raise Exception
        elif correct_order == CorrectOrderEnum.YES:
            total_indices += (i // 3) + 1

    return total_indices

class Signal:
    def __init__(self, signal, divider=False):
        self.signal = signal
        self.divider = divider

def compare_two_objects(object_1, object_2):
    correct_order = check_order(object_1.signal, object_2.signal)
                                
    if correct_order == CorrectOrderEnum.MAYBE:
        return 0
    elif correct_order == CorrectOrderEnum.YES:
        return -1
    else:
        return 1

@register(13, 2022, 2, True)
def distress_signal_2(split_text):
    signals = []
    for line in split_text:
        if len(line) > 0:
            signal = eval(line)
            signal_object = Signal(signal)

            signals.append(signal_object)

    signals.append(Signal([[2]], True))
    signals.append(Signal([[6]], True))

    signals = sorted(signals, key=cmp_to_key(compare_two_objects))

    total = 1
    for i, signal in enumerate(signals):
        if signal.divider:
            total *= (i + 1)

    return total



