# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


some_numbers = input().split()
count = 0
print(some_numbers)
for i in range(1, len(some_numbers), 2):
    count += int(some_numbers[i])
print(count)


