# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil
some_numbers = input().split()
final = []

for i in range(ceil((len(some_numbers))/2)):
    x = int(some_numbers[i]) * int(some_numbers[len(some_numbers)-1-i])
    final.append(x)
print(final)