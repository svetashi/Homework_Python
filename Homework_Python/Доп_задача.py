# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. НЕОБЯЗАТЕЛЬНАЯ
import sys

for X in [False, True]:
    for Y in [False, True]:
        for Z in [False, True]:
            left = not(X and Y and Z)
            right = (not X) or (not Y) or (not Z)
            if left==right:
                pass
            else:
                print("Not equal")
                sys.exit()
                
print("EQUAL")