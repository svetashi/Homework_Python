# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$ 

import math

with open('Ex_1.txt', 'r', encoding='utf-8') as file:
    RO = file.read().split('.')

print(RO)
num_RO = len(RO[1])
print(round(math.pi,num_RO))



