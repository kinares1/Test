def power_lists(x, y):
    return [xi ** yi for xi, yi in zip(x, y)]
print(power_lists([2, 3, 4],[10, 11, 12]))