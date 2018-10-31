#!/usr/bin/python
# -*- coding: utf-8 -*-
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
new_list = []
for a in [2, -5, 8, 9, -25, 25, 4]:
    if a >= 0 and math.sqrt(a) % 1 == 0:
        new_list.append(int(math.sqrt(a)))
print(new_list)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
days_less_ten = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвёртое', 5: 'пятое', 6: 'шестое', 7: 'седьмое', 8: 'восьмое', 9: 'девятое'}
days_multiple_ten = {2: 'двадцать', 3: 'тридцать'}
days_round = {10: 'десятое', 20: 'двадцатое', 30: 'тридцатое'}

date = "30.08.2014"

day = int(date[:2])
month = int(date[3 :5])
year = date[6:]

day_word = ''
month_word = ''

if day < 10:
    day_word = days_less_ten[day]
elif day % 10 == 0:
    day_word = days_round[day]
else:
    day_word = days_multiple_ten[day // 10] + ' ' + days_less_ten[day % 10]

month_word = months[month]

print('{day} {month} {year} года'.format(day=day_word, month=month_word, year=year))




# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = 10
i = 0
random_list = []
while i < n:
    random_list.append(random.randint(-100, 100))
    i += 1
print(random_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
new_list1 = []
new_list2 = []

# а)
#Вариант 1
for a in lst:
    if a not in new_list1:
        new_list1.append(a)
print(new_list1)

#Вариант 2
new_list1 = list(set(lst))
print(new_list1)

# б)
from collections import Counter
lst_counter = Counter(lst)
for a in new_list1:
    if lst_counter[a] == 1:
        new_list2.append(a)
print(new_list2)

result = new_list1 + new_list2