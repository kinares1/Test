while True:
    x: str = input('Введите целое число: ')
    x1: int = int(x)

    if (x1 > 20) and (x1 % 2) == 0:
        print("Отлично!")
        continue
    if (x1>=2) and (x1<=5) and (x1 % 2) == 0:
        print("Неплохо")
        continue
    if (x1 >= 6) and (x1 <=20) and (x1 % 2) == 0:
        print("Так себе")
        continue
    if (x1 % 2) > 0:
        print("Плохо")
    else:
        print("Попробуйте снова")
#Решенная