# 38. Напишите программу, удаляющую из текста все слова, содержащие "abc".

with open('1_ex.txt', 'r', encoding='utf-8') as file:
    new_list = file.read().split()

new_list = list(filter(lambda word: 'a' not in word and 'b' not in word and 'c' not in word, new_list))
print(new_list)