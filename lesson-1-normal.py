
__author__ = 'Саманов Антон Владимирович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

a = 58375
max = 0
while(a != 0):
    if (max < a%10):
        max = a%10
    a = a//10
print(max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a, b = input('Введите значения для двух переменных через запятую: ')
a = a + b
b = a - b
a = a - b
print(a, b)



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
a, b, c = input('Введите значения коэффициентов через запятую: ')
x1 = 0
x2 = 0
if a == 0:
    print('Ошибка, а = 0')
else:
    d = b**2 - 4 * a * c
    if d < 0:
        print('Нет действительный корней')
    elif d == 0:
        x1 = -b/2*a
        print('Один корень:', x1)
    elif d > 0:
        x1 = (-1*b + math.sqrt(d))/(2 * a)
        x2 = (-1*b - math.sqrt(d))/(2 * a)
        print('Два корня: ', x1, x2)
