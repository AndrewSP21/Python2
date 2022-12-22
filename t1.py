"""
1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
o	6 -> да
o	7 -> да
o	1 -> нет
"""

# a = 0
# err = 'Номер недели вне диапазона: 1 - 7'
# while 0 >= a or a < 8:
#     print('Введите номер дня недели (1 - 7) ')
#     a = input()
#     try:
#         a = int(a)
#         if a in (1, 2, 3, 4, 5):
#             print(f'{a} -> да')
#         if a in (6, 7):
#             print(f'{a} -> нет')
#         if a not in range(1, 8):
#             print(err)
#     except Exception:
#         print(err)

"""
2.	Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
V - или
⋀ - и
"""
# truefalse = [True, False]
#
# for x in truefalse:
#     for y in truefalse:
#         for z in truefalse:
#             assert not(x or y or z) == ((not x) and (not y) and (not z)), 'Утверждение не верно'

"""
3.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
o	x=34; y=-30 -> 4
o	x=2; y=4-> 1
o	x=-34; y=-30 -> 3

Четверти:
 2 | 1
 3 | 4

"""
# err1 = 'Введены координаты вне декартовой системы координат.'
# try:
#     x = float(input('Введите координату X: '))
#     y = float(input('Введите координату Y: '))
#     if x > 0 and y > 0:
#         print(f'x = {x}; y = {y} -> 1')
#     elif x > 0 and y < 0:
#         print(f'x = {x}; y = {y} -> 4')
#     elif x < 0 and y < 0:
#         print(f'x = {x}; y = {y} -> 3')
#     elif x > 0 and y < 0:
#         print(f'x = {x}; y = {y} -> 2')
#     elif x == 0 or y == 0:
#         print('Точка может принадлежать нескольким четвертям.')
# except Exception:
#     print(err1)
"""
4.	Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
точек в этой четверти (x и y).
Четверти:
 2 | 1
 3 | 4
"""

# err2 = 'Введен не корректный номер четверти'
#
# try:
#     quarter = int(input('Введите номер четверти (1 - 4): '))
#     if quarter == 1:
#         print(f'В четверти 1 диапазон возможныx координат X: от 0 до бесконечности, Y: от 0 до бесконечности')
#     elif quarter == 2:
#         print(f'В четверти 2 диапазон возможныx координат X: от минус бесконечности до 0, Y: от 0 до бесконечности')
#     elif quarter == 3:
#         print(f'В четверти 3 диапазон возможныx координат X: от минус бесконечности до 0, Y: от минус бесконечности до 0')
#     elif quarter == 4:
#         print(f'В четверти 4 диапазон возможныx координат X: от 0 до бесконечности, Y: от минус бесконечности до 0')
#     else:
#         print(err2)
# except Exception:
#     print(err2)

"""
5.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
o	A (3,6); B (2,1) -> 5,09
o	A (7,-5); B (1,-1) -> 7,21

"""

err1 = 'Введены координаты вне декартовой системы координат.'

try:
    x1 = float(input('Введите координату X первой точки: '))
    y1 = float(input('Введите координату Y первой точки: '))
    x2 = float(input('Введите координату X второй точки: '))
    y2 = float(input('Введите координату Y второй точки: '))

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    print(round(distance, 2))
except Exception:
    print(err1)