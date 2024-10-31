'''Завдання 1
Напишіть програму, яка запитує у користувача число і обчислює його факторіал.
Обробіть виняток, що виникає при введенні від'ємного числа, і виведіть повідомлення про помилку.'''

# factorial = int(input("Input a number: "))
# try:
#     if factorial < 0:
#         raise ValueError
# except ValueError:
#     print("Factorial is not defined for negative numbers")
# else:
#     ffactor = 1
#     for j in range (1, factorial+1):
#         ffactor = ffactor * j
#     print(f'The factorial of the number is, {ffactor}')

'''Завдання 2
Реалізуйте перше завдання через функцію. 
Функція повинна приймати число як параметр і повертати його факторіал. 
Перевірка коректності отриманих даних повинна бути всередині функції. 
Створіть дві версії реалізації функції:
Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.'''

# def factorial1(n):
#     if n < 0:
#         raise ValueError('Factorial is not defined for negative numbers')
#     else:
#         ffactor = 1
#         for j in range (1, n+1):
#             ffactor = ffactor * j
#         print(f'The factorial of the number is, {ffactor}')
#
# factorial1(5)
# factorial1(-5)
#---------------------------------------------------------------------------------
# def factorial2(n):
#     try:
#         if n < 0:
#             raise ValueError
#     except ValueError:
#         print("Factorial is not defined for negative numbers")
#     else:
#         ffactor = 1
#         for j in range (1, n+1):
#             ffactor = ffactor * j
#         print(f'The factorial of the number is, {ffactor}')
#
# factorial2(5)
# factorial2(-5)

'''Завдання 3
Напишіть програму, яка дає змогу користувачеві заповнити список із клавіатури числами. 
Після отримання даних відобразіть на екран меню, яке дозволяє виконати такі операції:
Відображення списку;
Отримання максимального значення у списку;
Отримання мінімального значення у списку;
Відображення значення елемента за індексом, введеним користувачем;
Видалення елемента за індексом, введеним користувачем.
Обробіть виняток, що виникає під час виходу за межі списку 
(користувач ввів неправильне значення для індексу елемента в списку), 
і виведіть повідомлення про помилку.'''

# try:
#     n = []
#     while True:
#         if len(n) == 0:
#             n = input("Enter numbers separated by a space: ").split(" ")
#         else:
#             action = input('''Select an action:
#         1. Show list
#         2. Show maximum value
#         3. Show minimum value
#         4. Show element by index
#         5. Delete element by index
#         6. Exit
#         ''')
#             if action == '1':
#                 print(n)
#             elif action == '2':
#                 print(max(n))
#             elif action == '3':
#                 print(min(n))
#             elif action == '4':
#                 index = int(input('Input an index: '))
#                 if index < 0 or index >= len(n):
#                     raise ValueError('Index out of range')
#                 else:
#                     print(n[index])
#             elif action == '5':
#                 index = int(input('Input an index: '))
#                 if index < 0 or index >= len(n):
#                     raise ValueError('Index out of range')
#                 else:
#                     del n[index]
#             elif action == '6':
#                 print('Goodbye!')
#                 break
#             else:
#                 raise ValueError('Invalid action')
# except ValueError as e:
#     print(e)

'''Завдання 4
Реалізуйте третє завдання через функції. Створіть дві версії реалізації функцій:
Перша версія не обробляє винятки всередині функцій. Уся обробка знаходиться зовні;
Друга версія обробляє винятки всередині функцій.'''

# def MyFunction1():
#     n = []
#     while True:
#         if len(n) == 0:
#             n = input("Enter numbers separated by a space: ").split(" ")
#         else:
#             action = input('''Select an action:
#         1. Show list
#         2. Show maximum value
#         3. Show minimum value
#         4. Show element by index
#         5. Delete element by index
#         6. Exit
#         ''')
#             if action == '1':
#                 print(n)
#             elif action == '2':
#                 print(max(n))
#             elif action == '3':
#                 print(min(n))
#             elif action == '4':
#                 index = int(input('Input an index: '))
#                 if index < 0 or index >= len(n):
#                     raise ValueError('Index out of range')
#                 else:
#                     print(n[index])
#             elif action == '5':
#                 index = int(input('Input an index: '))
#                 if index < 0 or index >= len(n):
#                     raise ValueError('Index out of range')
#                 else:
#                     del n[index]
#             elif action == '6':
#                 print('Goodbye!')
#                 break
#             else:
#                 raise ValueError('Invalid action')
# try:
#     (MyFunction1())
# except ValueError as e:
#     print(e)
#------------------------------------------------------------------------------
# def MyFunction2():
#     try:
#         n = []
#         while True:
#             if len(n) == 0:
#                 n = input("Enter numbers separated by a space: ").split(" ")
#             else:
#                 action = input('''Select an action:
#             1. Show list
#             2. Show maximum value
#             3. Show minimum value
#             4. Show element by index
#             5. Delete element by index
#             6. Exit
#             ''')
#                 if action == '1':
#                     print(n)
#                 elif action == '2':
#                     print(max(n))
#                 elif action == '3':
#                     print(min(n))
#                 elif action == '4':
#                     index = int(input('Input an index: '))
#                     if index < 0 or index >= len(n):
#                         raise ValueError('Index out of range')
#                     else:
#                         print(n[index])
#                 elif action == '5':
#                     index = int(input('Input an index: '))
#                     if index < 0 or index >= len(n):
#                         raise ValueError('Index out of range')
#                     else:
#                         del n[index]
#                 elif action == '6':
#                     print('Goodbye!')
#                     break
#                 else:
#                     raise ValueError('Invalid action')
#     except ValueError as e:
#         print(e)
#
# MyFunction2)