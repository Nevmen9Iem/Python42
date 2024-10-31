'''Завдання 1
Напишіть програму, яка запитує у користувача ім'я та вік.
Після отримання даних програма повинна виводити привітання у форматі:
"Привіт, {ім'я}! Твій вік — {вік}". Обробіть виняток,
що виникає при введенні некоректного віку (вік < 0 або вік > 130),
і виведіть повідомлення про помилку.'''

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# if age < 0 or age > 130:
#     raise ValueError
# print(f'Hello, {name}! Your age is {age}')

'''Завдання 2
Реалізуйте перше завдання через функцію. 
Функція повинна приймати ім'я і вік як параметри і повертати відформатований рядок. 
Перевірка коректності отриманих даних повинна бути всередині функції. 
Створіть дві версії реалізації функції:
Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.'''

# def hello1(name, age):
#     if not isinstance(name, str)or not isinstance(age, int):
#         raise ValueError ('Name must be a string and age must be an integer')
#     elif age < 0 or age > 130:
#         raise ValueError ('Age must be between 0 and 130')
#     return f'Hello, {name}! Your age is {age}'
#
# print(hello1('Andrey', 36))
# print(hello1(36, 'Andrey'))
# print(hello1('Andrey', -36))

#     raise ValueError (f'Error: {e}')

# def hello2(name, age):
#     try:
#         if not isinstance(name, str)or not isinstance(age, int):
#             raise ValueError ('Name must be a string and age must be an integer')
#         elif age < 0 or age > 130:
#             raise ValueError ('Age must be between 0 and 130')
#         return f'Hello, {name}! Your age is {age}'
#     except ValueError as e:
#         return f'Error: {e}'
#
# print(hello2('Andrey', 36))
# print(hello2(36, 'Andrey'))
# print(hello2('Andrey', -36))

'''Завдання 3
Напишіть програму, яка дозволяє користувачеві ввести з клавіатури 
набір додатних (число більше нуля) чисел. Числа необхідно накопичувати у списку. 
Після отримання всіх значень програма повинна проаналізувати дані. 
У разі виявлення від'ємного значення програма має згенерувати виняток. 
Якщо всі значення у списку позитивні, програма має повернути на екран суму всіх чисел списку.
Згенерований виняток має бути оброблений кодом програми.'''

# num = input('Enter numbers separated by a space: ').split()
# list_num = []
# for i in num:
#     list_num.append(int(i))
# try:
#     for i in list_num:
#         if i < 0:
#             raise ValueError('Negative values are not allowed.')
#     print(sum(list_num))
# except ValueError as e:
#     raise e

'''Завдання 4
Реалізуйте третє завдання через функцію. 
Функція повинна приймати список як аргумент і повертати суму елементів списку. 
Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:
Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.'''


# def sum_list(num):
#     list_num = []
#     for i in num:
#         list_num.append(int(i))
#     for i in list_num:
#         if i < 0:
#             raise ValueError('Negative values are not allowed.')
#     print(sum(list_num))
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_list(numbers)
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]
# sum_list(numbers1)

# def sum_list2(num):
#     list_num = []
#     for i in num:
#         list_num.append(int(i))
#     try:
#         for i in list_num:
#             if i < 0:
#                 raise ValueError('Negative values are not allowed.')
#         print(sum(list_num))
#     except ValueError as e:
#         raise e
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_list2(numbers)
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]
# sum_list2(numbers1)