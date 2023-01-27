# Задача 1.
# На заводе Sibaristika открывается новое кафе. Изначально есть некоторое количество кофейных зерен, молока и взбитых сливок.
# Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), которая
# возвращает напиток, который можно приготовить из имеющихся продуктов (ingredients). На
# вход функция принимает заранее неизвестное количество предпочтений посетителя. Все
# напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
# Бариста готовит наиболее предпочитаемый напиток из доступных.

coffee_dict = {
    'Эспрессо': [1,0,0],
    'Каппучино': [1,3,0],
    'Маккиато': [2,1,0],
    'Венский кофе': [1,0,2],
    'Латте': [1,2,1],
    'Кон Панна': [1,0,1]
}

ingredients = [4, 4, 0]                                                    # кофе, молоко, сливки

def choose_coffee(*args):
    global ingredients                                                     # достаём глобальный список доступных ингридиентов
    for preference in args:                                                # для напитка в предпочитаемых
        required = coffee_dict[preference]                                 # достаём состав
        makeable = True                                                    # можем сделать
        for ingredient_index in range(len(required)):                      # для каждого ингридиента под индексом
            if required[ingredient_index] > ingredients[ingredient_index]: # Если не хватает ингридиента
                makeable = False                                           # Не можем сделать
        if makeable:                                                       # Если можем сделать
            for ingredient_index in range(len(required)):                  # для каждого ингридиента под индексом
                ingredients[ingredient_index] = ingredients[ingredient_index] - required[ingredient_index] # отнимаем нужное количество от ингридиента
            return preference                                              # готовим кофе (возвращаем приготовленный)
    return 'Не можем приготовить ничего'                                   # если так ничего и не приготовили, то говорим что ничего не можем

user_preferences = list(input('Введите желаемый напиток в порядке убывания предпочтений: ').split())
print(choose_coffee(*user_preferences))
print(choose_coffee(*user_preferences))
print(choose_coffee(*user_preferences))
print(choose_coffee(*user_preferences))
