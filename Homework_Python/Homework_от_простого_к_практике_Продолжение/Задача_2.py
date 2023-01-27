#Шифр Цезаря
import string

count = int(input('Введите число сдвига: '))
sentense = input('Введите предложение: ')
new_sentense = ''


for i in sentense:
    if i in string.ascii_letters:
        i_unicode = ord(i)
        new_unicode = i_unicode + count
        new_character = chr(new_unicode)
        new_sentense = new_sentense + new_character
    else:
        new_sentense+= i
print(sentense)
print(new_sentense)






#ДЛЯ РУССКОГО АЛФАВИТА 

# count = int(input('Введите число сдвига: '))
# sentense = input('Введите предложение: ')
# new_sentense = ''


# for i in sentense:
#     if ord(i) in range(ord('А'), ord('я')+1):
#         i_unicode = ord(i)
#         new_unicode = i_unicode + count
#         new_character = chr(new_unicode)
#         new_sentense = new_sentense + new_character
#     else:
#         new_sentense+= i
# print(sentense)
# print(new_sentense)



