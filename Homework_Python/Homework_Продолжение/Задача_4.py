# Реализуйте алгоритм перемешивания списка.

import random
N = input()
N = list(N)

random.shuffle(N)
newWord = ""
for i in N:
    newWord += i
print(newWord)







