numbers = [1, 2, 3, 1, 8, 8, 7, 3]

not_unique_numbers = []
for el in numbers:
    if numbers.count(el) > 1:
        not_unique_numbers.append(el)

print(not_unique_numbers)
