from advent.runner import register
@register(6, 2021, 1)
def fish_1(text):
    fish = [ 0 for i in range(9)]

    for fish_age in text.split(","):
        fish[len(fish) - int(fish_age) - 1] += 1

    for i in range(80):
        birthed_fish = fish[-1]
        for j in range(len(fish) - 1, 0, -1):
            fish[j] = fish[j-1]
        fish[2] += birthed_fish
        fish[0] = birthed_fish

    return sum(fish)

@register(6, 2021, 2)
def fish_2(text):
    fish = [ 0 for i in range(9)]

    for fish_age in text.split(","):
        fish[len(fish) - int(fish_age) - 1] += 1

    for i in range(256):
        birthed_fish = fish[-1]
        for j in range(len(fish) - 1, 0, -1):
            fish[j] = fish[j-1]
        fish[2] += birthed_fish
        fish[0] = birthed_fish

    return sum(fish)
