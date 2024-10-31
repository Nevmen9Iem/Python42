 '''Завдання 2
Функція повинна приймати два параметри і відображати результат ділення на екран.
Створіть дві версії реалізації функції:
Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.'''

# a = int(input("Введіть перше число a: "))
# b = int(input("Введіть друге число b: "))
#
#
# def divide(a, b):
#     return a / b
#
#
# try:
#     print("Результат:", divide(a, b))
# except ZeroDivisionError:
#     print("divide(): Помилка: Ділення на нуль!")
#
#
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "divide1(): Помилка: Ділення на нуль!"
#
#
# print("Результат:", divide(a, b))

'''Завдання 3
Напишіть програму, яка приймає рядок і намагається перетворити його на число.
Обробіть виняток, що виникає при неможливості перетворення, і виведіть повідомлення про помилку.'''

# text = input("Введіть рядок: ")
# try:
#     number = int(text)
#     print("Число:", number)
# except ValueError:
#     print("ValueError: Не можу перетворити рядок на число!")

'''Завдання 4
Реалізуйте третє завдання через функцію. Функція повинна приймати рядок і відображати результат перетворення на екран. 
Створіть дві версії реалізації функції:
Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.'''

# def convert():
#     try:
#         text = input("Введіть рядок: ")
#         number = int(text)
#         print("Число:", number)
#     except ValueError:
#         print("ValueError: Не можу перетворити рядок на число!")
#
#
# def convert1():
#     text = input("Введіть рядок: ")
#     try:
#         number = int(text)
#         print("Число:", number)
#     except ValueError:
#         print("ValueError: Не можу перетворити рядок на число!")
#
#
# convert()
# convert1()

# class SevenError(Exception):
#     def __init__(self, value):
#         self.value = value
#         super().__init__(f"{self.value}")
#
#
# a = 5
# b = 2
#
#
# def plus(a, b):
#     result = a + b
#     if result == 7:
#         raise SevenError("You cannot use 7")
#     else:
#         return result
#
#
# print(plus(a, b))

# class NumberMoreLimmit(Exception):
#     def __init__(self,value):
#         self.value = value
#         super().__init__(f"{self.value} is more")
#
# def limit_num(l):
#     if len(l) > 1000:
#         raise NumberMoreLimmit(l)
#     else:
#         return l
#
# l=[i for i in range(1,1003)]
# print(l)
# try:
#     print(limit_num(l))
# except NumberMoreLimmit:
#     print("a lot of numb")
# except:
#     print("something went wrong")

class AgeError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"{self.value} is less")

def check_age(age):
    if age < 18:
        raise AgeError("Вік повинен бути не менше 18 років")
    else:
        print("Вік прийнятний")

try:
    check_age(15)
except AgeError as e:
    print(f"Помилка: {e}")
