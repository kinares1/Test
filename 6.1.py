elements = [0, 1, 2, 3, 4, 5]
sum = 0
n = len(elements)
for i in range(n):
    if ( i % 2 ==0):
        sum += elements[i]
if n != 0:
    print(f'elements = {elements}), результат : {sum * elements[n - 1]}')
else:
    print(f'elements = {elements}, резульат: {0}')
#Решенная

