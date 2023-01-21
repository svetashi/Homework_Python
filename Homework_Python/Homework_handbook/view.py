def inp_mod():
    mod = input('Введите режим работы(импорт или экспорт)')
    return mod



def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname


def view_import(result):
    print(*result, sep='\n')



def view_import_no():
    print(f'По введенной фамилии данные не найдены')


def inp_export():
    name = input('Введите имя для поиска: ')
    surname = input('Введите фамилию для поиска: ')
    phone = input('Введите телефон  для поиска: ')
    comment = input('Введите комментарий: ')
    return '', '', name, surname , phone, comment
