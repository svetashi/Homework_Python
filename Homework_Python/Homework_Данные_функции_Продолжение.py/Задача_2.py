# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

with open('Ex_2.txt', 'r', encoding='utf-8') as file:
    number = file.read()

# numbers = list(range(2, int(number)+1))
# print(numbers)

lst = []
for i in range(2, int(number)+1):
    k = 0
    for j in range(1,i+1):
        if i % j == 0:
            k+= 1
    if k == 2:
        lst.append(i)
print(lst)

count = int(number)
while count > 1:
    for i in reversed(lst):
        if int(count) % i == 0:
            print(i, end=',')
            count = count / i
            break
