"""
1.	Орел и решка

Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла,
а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество
подряд выпавших Решек.

Формат входных данных:
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных:
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
Входные данные	Выходные данные
ОРРОРОРООРРРО	3
ООООООРРРОРОРРРРРРР	7
ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР	31

"""

a = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
def tail(a):
    c = 0
    t = ''
    d = []
    for i in range(len(a)):
        if a[i] == 'Р' and i != len(a)-1:
            c += 1
            t = a[i]
        elif a[i] == 'Р' and i == len(a)-1:
            c += 1
            d.append(c)
        elif a[i] != 'Р' and t == 'Р':
            d.append(c)
            c = 0
            t = a[i]
        elif a[i] != 'Р' and t != 'Р':
            c = 0
            t = a[i]

    if not d:
        d = [0]

    return max(d)


# print(tail(a))


"""
2.	Измените код одной из решенных ранее задач (любой, с прошлых семинаров), применив лямбды, filter, map, zip, 
enumerate, списочные выражения.
"""

'''
3.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
исходной последовательности.
'''

lst = [1, 2, 2, 5, 7, 7, 8, 8, 8, 9]


data = list(filter(lambda x: lst.count(x) == 1, lst))

print(data)

"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
# lst = [int(i) for i in input().split()]
# count = 0
# for i in range(len(lst)):
#     if i % 2 != 0:
#         count += lst[i]
#
# print(count)

lst5 = [2, 3, 5, 8, 9, 3]
count = [x for x in range(len(lst5)) if lst5[x] % 2]
print(count)