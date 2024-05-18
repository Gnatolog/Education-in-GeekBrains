# Task2 2: Найдите сумму цифр трехзначного числа
# Пример: 123 -> 6 (1 + 2 + 3)
#         100 -> 1 (1 + 0 + 0) |

# n = input("Enter number: ")
# sum = 0
# for i in n:
#     sum = sum + int(i)
# print(sum)
# input('\n\tPress Enter to Exit')

# n = input("Enter number: ")
# sum = 0
# n = int(n)
# for i in range(n):
#     sum = sum + n % 10
#     n = n//10
# print(sum)
# input('\n\tPress Enter to Exit')

# Task 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и
# Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше
# журавликов, чем Петя и Сережа вместе?
# Пример:
#     6 -> 1  4  1
#     24 -> 4  16  4
#     60 -> 10  40  10
# S = input("Введите число журавликов: ")
# Petya = int(S) // 6 # делим общее число журавликов нацело по формуле получаем сколько журавликов сделал Петя
# Serega = Petya # Сергей  по условию сделал столько же журавликов сколько Петя
# Katya = (Serega + Petya) * 2 # Получаем количество журавликов которое сделала Катя
# print(f"Petya = {Petya}")    # Выводим результаты
# print(f"Katya = {Katya}")
# print(f"Serega = {Serega}")
# input ('\n\tPress Enter to Exit ')

# Task 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# Пример:
# 385916 -> yes
# 123456 -> no

# class Luckyticket():
#     """Класс проверяющий счастливый ли ваш билет"""
#
#     def __init__(self, tickets):
#         self.tickets = int(tickets)
#         self.sum1 = 0
#         self.sum2 = 0
#
#     def result(self,):
#         numb = int(self.tickets) % 1000
#         for i in range(numb):
#             self.sum1 = self.sum1 + numb % 10
#             numb = numb//10
#         print(f"Сумма первой тройки {self.sum1}")
#
#         numb2 = self.tickets // 1000
#         for i in range(numb2):
#             self.sum2 = self.sum2 + numb2 % 10
#             numb2 = numb2//10
#         print(f"Сумма второй тройки тройки {self.sum2}")
#
#         if self.sum1 == self.sum2:
#            print(f'Является ли ваш билет счастливым: yes')
#         else:
#            print(f'Является ли ваш билет счастливым: no')
#
#
# def main():
#
#     tickets = input('Enter your number tickets: ') # запрашивает номер билета для проверки
#     while tickets != 6:
#         if len(tickets) < 6:
#             print('Вы ввели некорректный номер пожалуйста повторите ввод')
#             tickets = input("Enter number ticket: ")
#         else:
#             return tickets
#
#
# ticket = Luckyticket(main()) # Создаём экземпляр счастливого билета
# ticket.result() # выводим результат проверки
#
# input("\n\tPress Enter to Exit")

# Task 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
#
# n = int(input("Введите длину шоколадки: "))
# m = int(input("Введите ширину шоколадки: "))
# k = int(input("Введите количесвто долек которое хотите получить: "))
# if k % n == 0 or k % m == 0 and n * m >= k:
#     print(f'Можно получить {k} дольки  -  yes')
# else:
#     print(f'Нельзя получить {k} долек  -  no')
#
# input('\n\tPress Enter to Exit')
