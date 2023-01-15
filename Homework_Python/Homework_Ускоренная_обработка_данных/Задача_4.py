# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.  AAABBBBBCCC -> 3A5B3C

def encode(c):
    count = 1
    res = ''
    for i in range(len(c)-1):
        if c[i] == c[i+1]:
            count += 1
        else:
            res += str(count)+c[i]
            count = 1
    res += str(count)+c[i]
    return res

def decode(ex):
    res = ''
    for i in range(0,len(ex),2):
        res += int(ex[i]) * ex[i+1]
    return res

with open('4_ex.txt', 'r', encoding='utf-8') as file:
    c = file.read()

firstFun = encode(c)
print(firstFun)
secondFun = decode(firstFun)
print(secondFun)

with open('4_ex_answer.txt', 'w', encoding='utf-8') as file:
    file.write(firstFun)
