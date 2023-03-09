def func(n):
    digits = [int(a) for a in str(n)]
    get_numbers = []
    for number in reversed(digits):
        get_numbers.append(number)
    return get_numbers


print(func(123))
