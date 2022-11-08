number: str = input('Введите целое число: ')
for_number: int = int(number)


if (for_number // 3) and (for_number//5) and (for_number % 3 == 0) and (for_number %5 == 0):
    print('Fizz Buzz')
elif (for_number // 3) and (for_number % 3 == 0):
    print('Fizz')
elif (for_number//5) and (for_number % 5 == 0):
    print('Buzz')
else:
    print("Try again")
# Решенная