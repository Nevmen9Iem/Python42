# 1. Завдання
# import result

# Показати на екрані таблицю множення всіх чисел від 1 до 10.

#  У такому вигляді:

#     1*1 = 1  1*2 = 2  ...  1*10 = 10
#     ................................
#     10*1 = 10  10*2 = 20  ...  10*10 = 100

# ver.1 (for)

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()

# ver.2 (white)

# i = 1
# j = 1
#
# while i in range(1,10):
#     i += 1
#     for j in range(1,10):
#         j += 1
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()

# 2. Завдання

# Використовуючи цикл for намалюйте порожній квадрат, якщо користувач задає розмір
# сторони та символ:

# Наприклад:

# Сторона квадрата = 5
# Символ = #
# 1 #####
# 2 #   #
# 3 #   #
# 4 #   #
# 5 #####

# a = int(input("Розмір сторони > "))
# b = input("Символ > ")
# print(b*a)
# for i in range(a-1):
#     i += 1
#     for j in range(2):
#         t = j - 1
#         print(b," "*(a-4),end=" ")
#     print()
# print(b*a)

# ver.2 Правильне рішення

# a = int(input("Розмір сторони > "))
# b = input("Символ > ")
#
# for i in range(a):
#     if i == 0 or i == a - 1:
#         print(b * a, end="")
#     else:
#         print(b, end="")
#         for j in range(a - 2):
#             print(" ", end="")
#         print(b, end="")
#     print("\n", end="")

# 3. Завдання

# Використовуючи цикл for, зведіть у квадрат усі числа від 11 до 99 і виведіть результат на
# екран.

# for i in range(11,99,10):
#     print(i*i,end=" ")
#     i += 1
#     for j in range(11,99):
#         j += 1
#         print(j*j,end=" ")
#
#     print()

# Другий for рахує все правильно тільки в 1 строчку, а всі інші рази повторю результат


# 4. Завдання

# Користувач вводить з клавіатури діаметр кола. Залежно від вибору користувача, порахуйте
# або площу, або периметр кола.
# import math
#
# d = int(input("Діаметр кола = "))
# action = int(input("Виберіть дію:\nПорахувати площу = 1 \nПорахувати периметр = 2\n"))
#
# if action == 1:
#     s = math.pi * ((d/2)**2)
#     print(f"Площа = {round(s,2)} см2")
# elif action == 2:
#     p = math.pi * d
#     print(f"Периметр = {round(p,2)} см")
# else:
#     print("Erorr")

# 5. Завдання

# Напишіть програму, яка на вхід отримує п'ять слів, а на виході у випадковому порядку бере
# з кожного слова по одному символу і складає їх слово.

# Наприклад:

# Word 1: Cat – Random = C Word 2: Yard – Random = a
# Word 3: Tree – Random = r Word 4: Dog – Random = g
# Word 5: Mouse – Random = o
# Result: Cargo

# import random
#
# words = []
# for i in range(1, 6):
#     word = input(f"Word {i}: ")
#     words.append(word)
#
# random_chars = []
# for word in words:
#     random_char = random.choice(word)
#     random_chars.append(random_char)
#
# result = ''.join(random_chars)
# print(f"Result: {result}")

# Вирішено за допомогою ChatGPT !!! Мені здається на заняттях ми це ще непроходили


# 6. Завдання

# Напишіть програму, яка на вхід отримує слово від 5 до 10 символів, а на виході замінює це
# слово на символи.
# При цьому:
# 0 індекс = @, 1 та 7 індекс = #, 3 та 6 та 9 індекс = !,
# 2 та 8 індекс = &, 4 індекс = +, 5 індекс = //

# Наприклад:

# Input your word: Movie =>>>> Result: @#&!+
# Input your word: Research =>>>> Result: @#&!+//!#

# text = input("Введіть слово від 5 до 10 літер: ")
#
# if len(text) < 5 or len(text) > 10:
#     print("Помилка: довжина слова повинна бути від 5 до 10 символів.")
# else:
#     text_2 = ""
#     for i in range(len(text)):
#         if i == 0:
#             text_2 += "@"
#         elif i == 1:
#             text_2 += "#"
#         elif i == 2:
#             text_2 += "&"
#         elif i == 3:
#             text_2 += "!"
#         elif i == 4:
#             text_2 += "+"
#         elif i == 5:
#             text_2 += "//"
#         elif i == 6:
#             text_2 += "!"
#         elif i == 7:
#             text_2 += "#"
#         elif i == 8:
#             text_2 += "&"
#         elif i == 9:
#             text_2 += "!"
#
#     print(f"Результат: {text_2}")
