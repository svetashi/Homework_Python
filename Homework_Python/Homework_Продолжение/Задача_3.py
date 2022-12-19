# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

# Пример:

# -Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

n = int(input())
ran = range(1, n)
count = 0

print('Для n=', n, '{', end='')

for i in ran:
    temp = (1+1/i) ** i
    count = temp + count
    print(i, ':', '{:.2f}'.format(temp), end=', ')

last = (1+1/n) ** n
print(i+1, ':', '{:.2f}'.format(last), '}')

print('Сумма: {:.2f}'.format(count+last))
