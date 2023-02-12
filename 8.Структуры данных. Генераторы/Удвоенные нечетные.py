number = 4

array = range(number)
double_odd_numbers = {x * 2 for x in range(number)
                      if (x % 2) > 0}
print(double_odd_numbers)
