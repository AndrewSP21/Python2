"""
1.	Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
o	6782 -> 23
o	0,56 -> 11

"""

# c = 0
# a = str(input('Введите вещественное число '))
# for i in a:
#     if i.isdigit():
#         c += int(i)
# print(c)

"""
2.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
o	пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)
"""
# n = ''
# while not n.isdecimal():
#     n = str(input('Введите целое число '))
# m = ''
# res = 1
# res2 = []
# res3 = []
# for i in range(1, int(n) + 1):
#     res *= i
#     res2.append(res)
#     m += str(i)
#     res3.append(int(m))
# print(res2, tuple(res3))

"""
3.	Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.
"""
# n = ''
# while not n.isdecimal():
#     n = str(input('Введите целое число '))
# res = 0
# for i in range(1, int(n) + 1):
#     res += (1 + 1 / i) ** i
#
# print(res)

"""
4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на 
указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""
#
# with open('file.txt', 'w') as f:
#     f.write("2\n3\n5")
# n = ''
# while not n.isdecimal():
#     n = str(input('Введите целое число больше трех '))
#     if n.isdecimal() and int(n) <= 3:
#         n = ''
#
# n = int(n)
# list1 = []
# for i in range(-n, n+1):
#     list1.append(i)
#
# list2 = []
# with open('file.txt', 'r') as f:
#     for line in f:
#         list2.append(line.splitlines()[0])
#
# res = 1
# for i in list2:
#     res *= list1[int(i)]
#
# print(res)

"""
5.	Реализуйте алгоритм перемешивания списка.
"""
import random
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in range(0, len(list1)):
    a = random.randint(0, len(list1)-1)
    list2.append(list1[a])
    del list1[a]

print(list2)