# 3. Еще немного о друзьях. Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.

from statistics import mean

friends = {}
new_dict= ()

lenght = int(input('Введите кол-во друзей: '))

for name in range(lenght):
    name = input('Введите имя друга: ')
    friends[name] = int(input('Введите возраст друга: '))
dict_mean = mean(friends.values())
max_name = max(friends, key=len)
print(dict_mean)
print(max_name)
