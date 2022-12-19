# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#  Пример:

#  - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


N = int(input())
print('пусть N =',N,', тогда' , end= ' ')
ran = range(1, N+1)
result = []
for i in ran:
    fact = 1
    for n in range(1, i+1):
        fact = fact * n
    result.append(fact)
print(result)
