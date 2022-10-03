'''
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, ? = 3.141.$    $10^{-1} ? d ?10^{-10}$
'''

# def rounds(n: float, d: int) -> float:
#     return round(n, d)
#
#
# pi = 3.1415926535
#
# print(rounds(pi, 3))

'''
2.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
# n = 5390
#
# lst = []
#
# for i in range(2, int((n + 1) ** 0.5 // 2)):
#     while n % i == 0:
#         lst.append(i)
#         n = n / i
#
# if len(lst) == 0:
#     lst = [1, n]
# print(lst)

'''
3.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
исходной последовательности.
'''

lst = [1, 2, 2, 5, 7, 7, 8, 8, 8, 9]
print(set(lst))
di = dict.fromkeys(lst, 0)
print(list(di.keys()))
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)

print(lst1)

'''
4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import random

# k = 4
# st = ''
#
# for i in range(k + 1):
#     t = random.randint(0, 100)
#     if t != 0:
#         if k - i == 1:
#             st += str(t) + 'x' + ' + '
#         elif k - i == 0:
#             st += str(t) + ' = 0'
#         else:
#             st += str(t) + 'x' + '^' + str(k - i) + ' + '
#
# with open('file3Hw4.txt', 'a') as f:
#     f.write(st + '\n')

'''
5.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
содержащий сумму многочленов.
'''
# m1 = '- 12x^4 + 77x^3 - 57x^2 - 2 = 0'
# m2 = '42x^4 + 38x^3 + 12x^2 + 59x + 34 = 0'
#
# lst1 = m1.split('=')
# lst = lst1[0].split()
# lst2 = m2.split('=')
# lst3 = lst2[0].split()
#
#
#
# def factoring(lst: list) -> dict:
#     '''
#     Функция раскладывает многочлен из списка в словарь. Каждый ключ словаря соответсвует степени элемента многочлена.
#     :param lst:
#     :return:
#     '''
#     di = {}
#     if lst[0] != '-':
#         if lst[0].find('^') != -1:
#             di[int(lst[0][lst[0].find('x^') + 2:])] = float(lst[0][:lst[0].find('x^')])
#     for i in range(len(lst)):
#         if lst[i] == '-':
#             if lst[i + 1].find('^') != -1:
#                 di[int(lst[i + 1][lst[i + 1].find('x^') + 2:])] = float(lst[i + 1][:lst[i + 1].find('x^')]) * (-1)
#             elif lst[i + 1].find('x') != -1:
#                 di[1] = float(lst[i + 1][:lst[i + 1].find('x')]) * (-1)
#             elif lst[i + 1].isdigit():
#                 di[0] = float(lst[i + 1]) * (-1)
#         elif lst[i] == '+':
#             if lst[i + 1].find('^') != -1:
#                 di[int(lst[i + 1][lst[i + 1].find('x^') + 2:])] = float(lst[i + 1][:lst[i + 1].find('x^')])
#             elif lst[i + 1].find('x') != -1:
#                 di[1] = float(lst[i + 1][:lst[i + 1].find('x')])
#             elif lst[i + 1].isdigit():
#                 di[0] = float(lst[i + 1])
#
#     return di
#
#
# def max_key(d1: dict, d2: dict) -> int:
#     """
#     Функция находит максимальное значение ключа в 2-х словарях
#     :param d1:
#     :param d2:
#     :return:
#     """
#     ls1 = []
#     ls2 = []
#     for key, con in d1.items():
#         ls1.append(key)
#     for key, con in d2.items():
#         ls2.append(key)
#     return max(max(ls1), max(ls2))
#
#
# di1 = factoring(lst)
# di2 = factoring(lst3)
# m = max_key(di1, di2)
#
# di3 = {}
# st2 = ''
# for i in range(m+1):
#     di3[m-i] = di1.get(m-i, 0) + di2.get(m-i, 0)
#     if m - i == 0:
#         st2 += str(di1.get(m - i, 0) + di2.get(m - i, 0)) + 'x^' + str(m - i) + ' = 0'
#     else:
#         st2 += str(di1.get(m-i, 0) + di2.get(m-i, 0)) + 'x^' + str(m-i) + ' + '
#
#
#
# print(m1)
# print(m2)
# print(st2)
