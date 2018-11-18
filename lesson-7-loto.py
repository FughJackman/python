#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

"""
Карточка - список, заполяемый рандомом и проверкой каждого нового элемента на несовпадение с добавленными элементами
[[ ], [ ], [ ]]

Получение бочонка - генератор списка с range [1,90] и if not in used_items

Card - заполнение, зачёркивание, вывод в отформатированном варианте
"""
import random

class Card:
    match_counter = 0
    def __generate_numbers(self):
        return random.sample(range(1,20), 15)
        
    def __slice_numbers(self, numbers):
        sliced_numbers = []
        a = 0
        b = 5
        for _ in range(3):
            sliced_numbers.append(sorted(numbers[a:b]))
            a += 5
            b += 5
        return sliced_numbers

    def __init__(self, name):
        self.owner = name
        self.numbers = self.__generate_numbers()
        self.sliced_numbers = self.__slice_numbers(self.numbers)

    def exclude_value(self, value):
        if value in self.numbers:
            for a in self.sliced_numbers:
                for n, i in enumerate(a):
                    if i == value:
                        a[n] = "-"
                        self.match_counter += 1
                        return True
        else:
            return False

    def print_current_state(self):
        print("Карточка ", self.owner)
        for a in self.sliced_numbers:
            print(' '.join(str(e) for e in a))
        print("------------------\n")

    @property
    def win_status(self):
        return self.match_counter >= 15

def quit_script():
    print("До будущих побед!")
    return False

def retrieve_number(lst):
    while len(lst) > 0:
        a = random.choice(lst)
        lst.remove(a)
        yield(a)


def game_script():
    card1 = Card("Пользователя")
    card2 = Card("Компьютера")

    avaliable_numbers = [a for a in range(1,31)] 

    while not card1.win_status and not card2.win_status:
        answ = ""
        try:
            current_number = next(retrieve_number(avaliable_numbers))
        except:
            # Такого случая не должно быть, но не обрабатывать эксепшн тоже неправильно
            print("Бочонки закончились")
            return False
        print("Новый бочонок: {} (осталось {})".format(current_number, len(avaliable_numbers)))
        print(card1.print_current_state(), card2.print_current_state())
        while answ != "quit" or answ!= "y" or answ != "n":
            answ = input("Зачеркнуть цифру? (y/n), quit - выход ")
            if answ not in ["y", "n", "quit"]:
                print("\nНеверная команда!\n")
            else:
                break
        if answ == "quit":
            commands[answ]()
        elif (answ == "y" and card1.exclude_value(current_number)) or (answ == "n" and not card1.exclude_value(current_number)):
            print("\nВерное решение! \n")
            # ход компьютера
            card2.exclude_value(current_number)
        else:
            print("\nУвы, вы проиграли \n")
            return False

    if card1.win_status and card2.win_status:
        print("Ничья! Победила дружба \n")
    elif card2.win_status:
        print("Сегодня удача на стороне компьютера! \n")
    else:
        print("Поздравляю! Вы победили! \n")



commands = {
    "start": game_script,
    "quit": quit_script
}

answer = ""
while answer != "quit":
    answer = input("Сыграем? start - да, quit - нет \n")
    if commands.get(answer):
        commands[answer]()
    else:
        print("Неверная команда \n")