# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

with open ('Ex_3.txt', 'r', encoding='utf=8') as file:
    numbers = file.read().split()
print(numbers)

uniq_numbers = []
for i in numbers:
    if numbers.count(i) == 1:
        uniq_numbers.append(i)
print(uniq_numbers)