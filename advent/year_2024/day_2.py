from advent.runner import register

@register(2, 2024, 1, True)
def reports_1(text):
    safe_count = 0
    for line in text:
        levels = [int(x) for x in line.split()]
        safe = True
        for i in range(1, len(levels)):
            diff = levels[i] - levels[i-1] 
            if i == 1:
                positive = (diff > 0)
            
            if abs(diff) == 0 or abs(diff) > 3 or (positive and diff < 0) or (not positive and diff > 0):
                safe = False
                break

        if safe:
            safe_count += 1

    return safe_count

def check_diff(diff, positive):
    return abs(diff) == 0 or abs(diff) > 3 or (positive and diff < 0) or (not positive and diff > 0)

@register(2, 2024, 2, True)
def reports_2(text):
    safe_count = 0
    for line in text:
        levels = [int(x) for x in line.split()]
        for positive in [True, False]:
            level_removed = False
            skip = False
            safe = True
            for i in range(1, len(levels)):
                if skip:
                    skip = False
                else:
                    diff = levels[i] - levels[i-1] 
                    
                    if check_diff(diff, positive):
                        if level_removed:
                            safe = False
                            break
                        else:
                            level_removed = True
                            skip = True
                            if i == 1:
                                diff_1 = levels[i+1] - levels[i-1] 
                                diff_2 = levels[i+1] - levels[i] 

                                check_1 = check_diff(diff_1, positive)
                                check_2 = check_diff(diff_2, positive)
                                if (check_1 and check_2):
                                    safe = False
                                    break
                            elif i < len(levels) - 1:
                                diff = levels[i+1] - levels[i-1] 
                                if check_diff(diff, positive):
                                    safe = False
                                    break

            if safe:
                safe_count += 1
                break

    return safe_count