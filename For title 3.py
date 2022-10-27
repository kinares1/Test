
# 1.Welcоme to Python
name = 'Denis'
surname ='Chaptarov'

print(f'Hello {name} {surname}!You just delved into Python. Great start :)')

# 2. Заголовок
text= ('I do not understand anything')
print(text.title())


# 3.Форматированный вывод денежной суммы
#Дано: денежная сумма (amount > 0).

#Задание: написать программу, которая распечатает число в принятом денежном формате XXX,XXX.XX.

#Пример: amount = 100500.157; результат = 100,500.16
Amount = 742858.4
for_numbers: str = "$ {:,.2f}".format(Amount)
print(for_numbers)

# 4. Python art
thickness = 5
c = 'P'


# Python art
thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))





    # [Junior] 5. Дизайнер ковриков

    height = 11
    width = height * 3

    for stick_count in range(1, height, 2):
        print(('.|.' * stick_count).center(width, '-'))

    print('WELCOME'.center(width, '-'))

    for stick_count in range(height - 2, 0, -2):
        print(('.|.' * stick_count).center(width, '-'))



