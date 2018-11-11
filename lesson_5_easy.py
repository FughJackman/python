# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

# Вызов скриптов, используемыех только в рамках easy вынесен в конец файла.

def create_folder(name, path=os.getcwd()):
    dir_path = os.path.join(path, name)
    try:
        os.mkdir(dir_path)
        print('Директория успешно создана')
    except FileExistsError:
        print('Такая директория уже существует')

def remove_folder(name, path=os.getcwd()):
    try:
        os.rmdir(os.path.join(path, name))
        print('Директория успешно удалена')
    except FileNotFoundError:
        print('Ошибка при удалении директории')

def create_ten_folders():
    for i in range(1,10):
        create_folder('dir_{}'.format(i))
    print('Директории созданы \n')

def remove_ten_folders():
    for i in range(1,10):
        remove_folder('dir_{}'.format(i))
    print('Директории удалены \n')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders_list():
    print([dir_name for dir_name in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), dir_name))])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():

    current_file = os.path.basename(__file__)

    # Вариант с shutil:
    # shutil.copy(current_file, f'{current_file}'.replace('.py', '_copy.py'))

    #Вариант с использванием пройденного в уроке по работе с файлами. 
    buffer = ""

    with open(current_file, 'r', encoding='UTF-8') as p:
        buffer = p.read()
        p.close()

    path = os.path.join(f'{current_file}'.replace('.py', '_copy.py'))
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(buffer)
        f.close()
        print('Файл скопирован \n')

# create_ten_folders()
# show_folders_list()
# remove_ten_folders()
# copy_current_file()