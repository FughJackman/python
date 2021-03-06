## -*- coding: utf-8 -*-
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 1
    b = 1
    fibonacci_list = []
    for __ in range(m):
        a, b = b, a + b
        fibonacci_list.append(a)
    return fibonacci_list[n:]

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1 
    while n < len(origin_list):
        for i in range(len(origin_list)-n):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
        n += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def custom_filter(func, iterators):
    result = []
    for i in iterators:
        if func(i):
            result.append(i)
    return result


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def check_dots((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
    """
    Вектора равны, если их координаты равны. При этом они имеют одинаковую длину, лежат на параллельных прямых или на одной прямой
    Если в четырехугольнике две противоположные стороны равны и параллельны, то этот четырехугольник — параллелограмм.
    """
    #Проверяем, что три точки не лежат на одной прямой. В последний момент заметил возможность деления на ноль, не успел поправить
    if ((x3 - x1) / (x2 - x1) == (y3 - y1) / (y2 - y1)):
        return False
    #Сравниваем координаты векторов AB и DC
    else:
        return (x2 - x1, y2 - y1) == (x3 - x4, y3 - y4)

    

print(check_dots((1, 3), (1, 3), (2, 8), (-1, 4)))