# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

N = input()
count = 0
N = list(N)

for i in range(len(N)):                # function 'N = N.replace(',', '0')
    if N[i] == ",":
        N[i] == "0"
    else:
        count = count + int(N[i])
print(count)
