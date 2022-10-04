import csv
import json
import view

from dicttoxml2 import dicttoxml

file_name = 'data'


def create_user(data):
    with open(file_name + '.csv', 'a', encoding='utf8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator='\r')
        file_writer.writerow(data)


def new_create_user(data):
    with open(file_name + '.csv', 'w', encoding='utf8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator='\r')
        file_writer.writerows(data)


def show_users():
    lst = []
    with open(file_name + '.csv', 'r', encoding='utf8') as file:
        file_reader = csv.reader(file, delimiter=';', lineterminator='\r')
        for item in file_reader:
            lst.append(item)
    return lst


# def update_user(id_user, date):
#     res = view.user_data_entry()
#     date[id_user] = res
#     return date


def delete_user(id_user, data):
    del data[id_user]
    return data


# def txt_creator(guide):
#     with open(file_name + '.txt', 'w') as file:
#         for line in guide:
#             for word in line:
#                 file.write(f'{word} \n\n')
#
#
# def xml_creator(guide):
#     with open(file_name + '.xml', 'w', encoding='utf-8-sig') as file:
#         xml = dicttoxml(guide)
#         file.write(xml.decode())
#
#
# def json_creator(guide):
#     with open(file_name + '.json', 'w', encoding='utf-8-sig') as file:
#         file.write(json.dumps(guide, ensure_ascii=False))
