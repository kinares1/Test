'''
Дано: целое число (int).

Задание: Римские цифры пришли к нам из древней римской системы счета. Они основаны на особых буквах алфавита, которые в различных сочетаниях, путем суммирования (а иногда и разницы) описывают различные числа. Первые 10 римских чисел это:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

Римская система счета имеет десятичное основание, но она непозиционная и не включает в себя 0 (ноль). Римские числа образуются путем комбинации следующих семи символов:

Символ Значение I 1 (unus) V 5 (quinque) X 10 (decem) L 50 (quinquaginta) C 100 (centum) D 500 (quingenti) M 1,000 (mille) Узнать больше о римских цифрах вы можете в статье на Википедии.

В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999) в римскую систему счета
'''

import math


def ToRoman(A):
    roman_numbers = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",

        }

    div = 1
    while A >= div:
        div *= 10

    div /= 10

    res = ""

    while A:

        lastNum = int(A / div)

        if lastNum <= 3:
            res += (roman_numbers[div] * lastNum)
        elif lastNum == 4:
            res += (roman_numbers[div] +
                    roman_numbers[div * 5])
        elif 5 <= lastNum <= 8:
            res += (roman_numbers[div * 5] +
                    (roman_numbers[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (roman_numbers[div] +
                    roman_numbers[div * 10])

        A = math.floor(A % div)
        div /= 10

    return res

print(ToRoman(3999))
