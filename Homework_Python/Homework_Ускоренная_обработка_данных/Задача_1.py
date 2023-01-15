# 38. Напишите программу, удаляющую из текста все слова, содержащие "abc".

some_list = ['Hello', 'world', 'today', 'sunny', 'day', 'chuss']
new_list = list(filter(lambda word: 'a' not in word and 'b' not in word and 'c' not in word, some_list))
print(new_list)