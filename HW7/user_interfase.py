def start():
    print('Конвертация данных')
    menu = '''
    1. Справочника txt в csv
    2. Справочника csv в txt
    3. Справочника txt в xml
    4. Справочника txt в json
    5. Справочника csv в xml
    6. Справочника csv в json
    7. Справочника json в xml
    8. Справочника json в txt
    9. Справочника json в csv
    '''
    print(menu)
    item = 0
    while item not in range(1, 10):
        item = int(input('Выберите пункт меню: '))
        # print(item)

    file_name = str(input('Укажите имя файла, который нужно сконвертировать(по умолчанию guide '
                          'с соответсвующим расширением): '))
    return item, file_name
