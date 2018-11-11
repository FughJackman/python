# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
from lesson_5_easy import create_folder, remove_folder, show_folders

answer = ""


def print_help():
    print("")
    print("help - получение справки")
    print("chdir - перейти в папку")
    print("listdir - просмотреть содержимое текущей папки")
    print("mkdir - создание директории")
    print("rmdir - удаление директории")
    print("quit - выйти из программы \n")

def change_dir(name, path=os.getcwd()):
    try:
        os.chdir(os.path.join(path, name))
        print("Директория изменена \n"")
    except FileNotFoundError:
        print("Невозможно перейти в директорию \n"")

def quit_script():
    print("bye-bye")

commands = {
    "help": print_help,
    "chdir": change_dir,
    "mkdir": create_folder,
    "rmdir": remove_folder,
    "listdir": show_folders,
    "quit": quit_script
}

while answer != "quit":
    answer = input("Введите команду или help для получения списка команд: ")
    if commands.get(answer):
        if answer == "chdir" or answer == "mkdir" or answer == "rmdir":
            name = input("Введите название папки: ")
            commands[answer](name)
        else:
            commands[answer]()
    else:
        print("Неверная команда \n")