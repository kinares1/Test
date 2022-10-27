# 1. Среднее арифметическое случайных  трех чисел
from random import randint

# Задаем три переменных со значением случайных чисел\

x = (randint(0, 1000))
y = (randint(0, 1000))
z = (randint(0, 1000))
print((x+y+z)//3)

# 2. Деление и еще раз деление

# Задаем переменные со значением случайных чисел
random_number_1 = (randint(0, 1000))
random_number_2 = (randint(0, 1000))

if random_number_2 > 0:    # Ставим условие на проверку делителя
    division_random_numbers = (random_number_1 // random_number_2)
    print(division_random_numbers)
    remainder = (random_number_1 % random_number_2)
    print(remainder)
elif random_number_2 == 0: # Для отсутствия пустой строки в случае равенства
    print("You were unlucky")

# 3 Округление

x = 5342.735
n1 = round(x, 2)
n2 = round(x)
print(n1)
print(n2)
print('{0:=011}'.format(x))

# [Junior] 4. Число "наоборот"

number = 324341431
reversed_number = 0
while number > 0:
    # находим остаток - последнюю цифру
    digit = number % 10
    # делим нацело - удаляем последнюю цифру
    number = number//10
    # увеличиваем разрядность второго числа
    reversed_number = reversed_number*10
    # добавляем очередную цифру
    reversed_number = reversed_number+digit

print(reversed_number)


#Дано: число с плавающей точкой.

#Задание: написать программу, которая будет округлять заданное число:

#1) 2х знаков после запятой; 2) до целого; 3) дополнять слева столько нулей, сколько не хватает числу до 11 знаков.

#Пример:

#x = 14.721

#1) 14.72

#2) 15

#3) 0000014.721

