# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# x, y = map(float, input().split())

N = input().split()

float_N = [float(x) for x in N]
result = []
print(float_N)

for i in range(len(float_N)):
    comma_N = float(float_N[i]) % 1
    if comma_N == 0:
        continue
    result.append(comma_N)
print(round(max(result)-min(result),2))

