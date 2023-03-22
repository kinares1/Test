def lazy_sequence(n):
    for x in range(n):
        if x == 0:
            yield -10
        elif x % 3 == 0:
            yield 45
        elif x % 5 == 0:
            yield x / 5 + 93
        else:
            yield x / 2
for value in lazy_sequence(10):
    print(value)
