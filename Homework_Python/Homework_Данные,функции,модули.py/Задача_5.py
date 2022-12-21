# НЕОБЯЗАТЕЛЬНАЯ Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Fn = F(n-1) + F(n-2)     для 8 до и включительно: 0, 1, 1, 2, 3, 5, 8, 13, 21

num = int(input())

fibo_list = [0, 1]

for i in range(num-1):
    fibo_list.append((fibo_list[i]) + (fibo_list[i+1]))

temp_list = fibo_list.copy()

for i in range(2, len(temp_list), 2):
    temp_list[i] = temp_list[i] - temp_list[i] * 2
temp_list.reverse()

for i in range(1, len(fibo_list)):
    temp_list.append(fibo_list[i])

fibo_list = temp_list
print(temp_list)
