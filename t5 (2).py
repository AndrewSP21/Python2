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

start = 2021
import random



def first_move():
    return random.randint(1, 2)

def next_move():
    return random.randint(1, 28)

def next_player(current_player):
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    return current_player

def winner(player):
    return print(f'Поздаравляем, победил {player}')

#
# player1 = input('Введите имя первого игрока')
# player2 = input('Введите имя второго игрока')
player1 = 'Вася'
player2 = 'Петя'

current_player = first_move()
if current_player == 1:
    print(f'Первым ходит: {player1}')
else:
    print(f'Первым ходит: {player2}')

while start >= 0:
    start -= next_move()
    if start >= 0:
        winner(current_player)



#
# b = next_move()
# print(a)
# print(b)
