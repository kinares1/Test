number = int(input("Введите число от 1 до 9 : "))

if number > 9 or number < 1:
    print("Еrrоr")
else:
    string_numbers = ('')

    for i in range(1, number+1):
        string_numbers += str(i)
print(string_numbers)
#Решенная
