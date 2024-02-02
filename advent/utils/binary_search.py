#maximum_bound should be highest possible not necessarily in beam
def find_first(func_for_test, minimum_bound, maximum_bound):
    value_to_check = int((minimum_bound+maximum_bound)/2)
    #print(f"minimum {minimum_bound} maximum {maximum_bound} value {value_to_check} pass {func_for_test(value_to_check)}")
    if minimum_bound > maximum_bound:
        raise Exception(f"Minimum {minimum_bound} is > than maximum {maximum_bound}")
    if minimum_bound == maximum_bound:
        if func_for_test(value_to_check):
            return minimum_bound
        else:
            return minimum_bound + 1
    else:
        if func_for_test(value_to_check):
            if value_to_check == minimum_bound:
                return minimum_bound
            return find_first(func_for_test, minimum_bound, value_to_check - 1)
        else:
            return find_first(func_for_test, value_to_check + 1, maximum_bound)