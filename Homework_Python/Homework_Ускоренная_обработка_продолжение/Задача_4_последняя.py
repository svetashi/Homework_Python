# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем. Привер: 3,4,7,3 -> 3 уникальных элемента

import random
n = int(input("Сколько элементов? "))
list1 = []
for i in range(n):
    list1.append(random.randint(1, 10))
print('Cделан такой список -', list1)

list2= set(list1)
print('new list', list2)
print('uniq numbers is - ', len(list2))
