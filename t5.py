"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""
# a = 'Рыжиий котабв пришел в паб От рассвета абв до закатаабв'
# res = list(filter(lambda x: 'абв' not in x, a.split()))
# print(' '.join(res))

'''
2.	Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"

'''

start = 35
import random


def first_move(player1, player2):
    res = random.choice([player1, player2])
    print(f'Первым ходит: {res}')
    return res


def next_move(current_player, start):
    if start > 28:
        res = random.randint(1, 28)
    else:
        res = random.randint(1, start)

    print(f'Выбор игрока {current_player}: {res}')
    return res


def next_player(current_player, pl1, pl2):
    if current_player == pl1:
        current_player = pl2
    else:
        current_player = pl1
    return current_player


def winner(current_player):
    return print(f'Поздравляем, победил игрок: "{current_player}"')


'''------------------Бот против бота----------------------'''


# player1 = 'Вася'
# player2 = 'Петя'
#
# current_player = first_move(player1, player2)
#
# while start > 0:
#     start -= next_move(current_player, start)
#     print(f'Осталось {start} конфет')
#     if start <= 0:
#         break
#     current_player = next_player(current_player, player1, player2)
#
#
# winner(current_player)

def next_move_live(current_player, start):
    flag = 0
    if start > 28:
        while 1 > flag or flag > 28:
            flag = int(input(f'Игрок: {current_player}. Введите число от 1 до 28: '))
        res = flag
    else:
        while 0 >= flag or flag > start:
            flag = int(input(f'Игрок: {current_player}. Введите число от 1 до {start}: '))
        res = flag

    print(f'Выбор игрока {current_player}: {res}')
    return res


'''------------------------Игрок против игрока--------------------'''
# player1 = input('Введите имя первого игрока: ')
# player2 = input('Введите имя второго игрока: ')
#
# current_player = first_move(player1, player2)
#
# while start > 0:
#     start -= next_move_live(current_player, start)
#     print(f'Осталось {start} конфет')
#     if start <= 0:
#         break
#     current_player = next_player(current_player, player1, player2)
#
# winner(current_player)


'''------------------------Игрок против бота--------------------'''


# next_move(current_player, start)


def next_move_live_bot(current_player, start):
    if current_player == 'Бот':
        res = next_move(current_player, start)
    else:
        res = next_move_live(current_player, start)
    return res


# print('Игра против бота')
# player1 = input('Введите имя игрока: ')
# player2 = 'Бот'
#
# current_player = first_move(player1, player2)
#
# while start > 0:
#     start -= next_move_live_bot(current_player, start)
#     print(f'Осталось {start} конфет')
#     if start <= 0:
#         break
#     current_player = next_player(current_player, player1, player2)
#
# winner(current_player)

'''------------------------Игрок против умного бота--------------------'''


def next_move_clever(current_player, start):
    if current_player == 'Бот':
        if not start % 2 and start >= 30:
            res = 1
            print(f'Выбор игрока {current_player}: {res}')
        elif start % 2 and start >= 31:
            res = 2
            print(f'Выбор игрока {current_player}: {res}')
        elif start <= 28:
            res = start
            print(f'Выбор игрока {current_player}: {res}')
    else:
        res = next_move_live(current_player, start)

    return res


# print('Игра против умного бота')
# player1 = input('Введите имя игрока: ')
# player2 = 'Бот'
#
# current_player = first_move(player1, player2)
#
# while start > 0:
#     start -= next_move_clever(current_player, start)
#     print(f'Осталось {start} конфет')
#     if start <= 0:
#         break
#     current_player = next_player(current_player, player1, player2)
#
# winner(current_player)

'''
Создайте программу для игры в ""Крестики-нолики"".
'''




def p(m, x):
    """Проверяет заполненость ячейки, если заполнена, то выводит пробел, если не заполнена номер ячейки"""
    return [x if m[x]==' ' else ' '][0]

def free_point_matrix(m):
    return print(
                f"""
Номера ячеек:        Не заполненные ячейки:
    1 2 3                {p(m,1)} {p(m,2)} {p(m,3)}
    4 5 6                {p(m,4)} {p(m,5)} {p(m,6)}
    7 8 9                {p(m,7)} {p(m,8)} {p(m,9)}
                """)



def update_field(m):
    field =\
f"""Игровое поле:
    {m[1]}{m[0]}{m[2]}{m[0]}{m[3]}
    ------
    {m[4]}{m[0]}{m[5]}{m[0]}{m[6]}
    ------
    {m[7]}{m[0]}{m[8]}{m[0]}{m[9]}
    """
    return field


def free_point(m):
    '''Выводит список пустых ячеек'''
    return [k for k, v in m.items() if v == ' ']


def check_win(m, current_playerX):
    '''Проверка выигрышных вариантов'''
    if m[1] == m[2] == m[3] == current_playerX \
            or m[4] == m[5] == m[6] == current_playerX \
            or m[7] == m[8] == m[9] == current_playerX \
            or m[1] == m[4] == m[7] == current_playerX \
            or m[2] == m[5] == m[8] == current_playerX \
            or m[3] == m[6] == m[9] == current_playerX \
            or m[1] == m[5] == m[9] == current_playerX \
            or m[7] == m[5] == m[3] == current_playerX:
        return current_playerX
    return None

def next_playerX(current_player):
    '''Смена игрока'''
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'
    return current_player





def your_move(current_playerX, f):
    print(f'Ход игрока играющего "{current_playerX}"')
    x = 0
    while x not in f:
        x = int(input('Введите ячеку для хода: '))
    return x

def main():
    print('Игра "Крестики - нолики"')
    m = {0: '|', 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    current_playerX = 'X'

    while not check_win(m, current_playerX):
        free_point_matrix(m)
        update_field(m)
        m[your_move(current_playerX, free_point(m))] = current_playerX

        if check_win(m, current_playerX):
            field = update_field(m)
            print(field)
            print(f'Победитель "{current_playerX}". Игра закончена.')
            break
        elif not check_win(m, current_playerX) and not free_point(m):
            field = update_field(m)
            print(field)
            print(f'Ничья. Игра закончена.')
            break

        field = update_field(m)
        current_playerX = next_playerX(current_playerX)
        print(field)

# main()

"""
4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Пример:
Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
Текст после кодировки: 12W1B12W3B24W1B14W
Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""
def prepare(file_name_text):
    plain_text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

    with open(file_name_text, 'w') as f:
        f.write(plain_text)


def codding(file_name_text,file_name_code):
    with open(file_name_text, 'r') as f:
        plain = f.readline()

    first = plain[0]
    count = 0
    code = ''

    for i in range(0, len(plain)):
        if plain[i] == first and i != (len(plain)-1):
            count += 1
        elif plain[i] == first and i == (len(plain)-1):
            count += 1
            code += str(count) + first
        else:
            code += str(count) + first
            count = 1
            first = plain[i]

    with open(file_name_code, 'w') as f:
        f.write(code)

def decodding(file_name_code, file_name_text):
    with open(file_name_code, 'r') as f:
        code = f.readline()
    di = ''
    text = ''
    for i in code:
        if i.isdigit():
            di += str(i)
        else:
            text += int(di) * i
            di = ''

    with open(file_name_text, 'a') as f:
        f.write(f'\n{text}')
def main():
    prepare("fileHW5.txt")
    codding("fileHW5.txt", 'fileHW5_code.txt')
    decodding('fileHW5_code.txt', "fileHW5.txt")

main()