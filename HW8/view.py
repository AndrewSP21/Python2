def user_menu():
    menu = ['Все сотрудники', 'Добавить сотрудника', 'Удалить сотрудника', 'Внести изменения в запись',
            'Экспортировать в txt', 'Экспортировать в json', 'Экспортировать в xml']
    for item in enumerate(menu, 1):
        print(*item)
    num = int(input("Выберите пункт меню: "))
    return num


def user_data_entry():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите № телефона: ')
    directory_entry = [name, surname, phone]
    return directory_entry


def view_user(data):
    for row in enumerate(data, 1):
        print(*row)


def up_del_user():
    num = int(input('Введите номер записи для изменения: '))
    return num - 1




