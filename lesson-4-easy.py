# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
random_list = [random.randint(-10, 10) for _ in range(10)]
result = [el ** 2 for el in random_list]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruit_one = ["груша", "яблоко", "банан", "киви", "манго"]
fruit_two = ["ананас", "яблоко", "апельсин", "грейпфрут", "манго"]
same_fruits = [el for el in fruit_one if el in fruit_two]

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
random_list2 = [random.randint(-10, 10) for _ in range(10)]
approved_list = [el for el in random_list2 if el > 0 and el % 3 == 0 and el % 4 != 0]