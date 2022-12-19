# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('введите координату x1: '))
y1 = float(input('введите координату y1: '))
x2 = float(input('введите координату x2: '))
y2 = float(input('введите координату y2: '))

temp = ((x2 - x1)**2) + ((y2 - y1)**2)
sqrt = temp ** (0.5)
print('Расстояние между точками: {:.3f}'.format(sqrt))

