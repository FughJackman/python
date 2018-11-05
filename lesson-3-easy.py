# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    tens = 10 ** ndigits
    a = number*tens
    return (a // 1) / tens if a % 1 < 0.5 else (a // 1 + 1) / tens


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if not isinstance(ticket_number, int) or len(str(ticket_number)) != 6:
        return('Некорректно введён номер билета')
    
    right_part = 0
    left_part = 0    
    
    while(len(str(ticket_number)) != 3):
        right_part += ticket_number%10
        ticket_number = ticket_number//10
    
    while(ticket_number != 0):
        left_part += ticket_number%10
        ticket_number = ticket_number//10
    
    return "Счастливый" if left_part == right_part else "Несчастливый"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))