# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

N = input()
count = 0
N = list(N)

if "," in N:                                     # function 'N = N.replace(',', '0')
    for i in range(len(N)):
        if N[i] == ",":
            N[i] = "0"

for i in N:
    count = count + int(i)
print(count)
