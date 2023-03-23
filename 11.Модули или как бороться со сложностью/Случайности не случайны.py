import random

def random_floats(n):
    for i in range(n):
        yield random.uniform(0, n)
"""Функция принимает параметр n, который определяет количество чисел, которые нужно сгенерировать."""
result = list(random_floats(3))
print(result)
