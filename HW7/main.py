# guide = [{'surname': 'Иванов', 'name': 'Иван', 'patronymic': 'Иванович', 'phone': '+74951234567', 'post': 'Директор'},
#          {'surname': 'Петров', 'name': 'Петр', 'patronymic': 'Петрович', 'phone': '+74957654321', 'post': 'Бухгалтер'},
#          {'surname': 'Сидоров', 'name': 'Сидор', 'patronymic': 'Сидорович', 'phone': '+74959999999',
#           'post': 'Секретарь'},
#          {'surname': 'Мартов', 'name': 'Март', 'patronymic': 'Мартович', 'phone': '+74991111111', 'post': 'Водитель'}]



def main():
    import user_interfase as ui
    import Convertor as co
    item, filename = ui.start()
    co.process(item, filename)

main()
