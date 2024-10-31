# 1-й файл inpython
# 2-й файл outpython

import random

# 1 Завдання

# with open('/Users/andriisumnevych/Documents/inpython.txt', 'w+') as file_write:    # відкриття файлу
#     num_list = [random.randint(10, 99) for i in range(20)]
#     print(num_list)
#
#
# with open('/Users/andriisumnevych/Documents/inpython.txt', 'r') as file_text:       # відкриття файлу
#     file_read = file_text.read()                                                    # читання тексту
#     list_text = file_read.split(",")                                                # розділення тексту на окремі елементи
#     list_map = list(map(lambda i: chr(int(i)), list_text))                          # перетворення чисел на символи
#     print(list_map)
#
#
# with open('/Users/andriisumnevych/Documents/outpython.txt', 'w') as file_out:       # відкриття файлу
#     letter_text = ','.join(list_map)                                                # перетворення символів на числа
#     file_out.write(letter_text)                                                     # запис у файл


# with open('/Users/andriisumnevych/Documents/inpython.txt', "w") as file_in:           # відкриття файлу
#     list_num = [str(random.randint(65, 90)) for i in range(20)]                 # генерація чисел
#     num_text = ", ".join(list_num)                                                    # перетворення чисел на текст
#     file_in.write(num_text)                                                           # запис у файл
#
# with open('/Users/andriisumnevych/Documents/inpython.txt', "r") as file_text:         # відкриття файлу
#     file_read = file_text.read()                                                      # читання тексту
#     list_text = file_read.split(", ")                                                 # розділення тексту на окремі елементи
#     list_map = list(map(lambda i: chr(int(i)), list_text))                            # перетворення чисел на символи
#     print(list_map)                                                                   # виведення символів
#
# with open('/Users/andriisumnevych/Documents/outpython.txt', "w") as file_out:         # відкриття файлу
#     letter_text = ", ".join(list_map)                                                 # перетворення символів на числа
#     file_out.write(letter_text)                                                       #

# 2 Завдання

# with open('/Users/andriisumnevych/Documents/inpython.txt', "w+") as file_in:
#     list_num = [str(random.randint(65, 90)) for i in range(30)]
#     num_text = ", ".join(list_num)
#     file_in.write(num_text)
#
# with open('/Users/andriisumnevych/Documents/inpython.txt', "r") as file_text:
#     file_read = file_text.read()
#     list_num = file_read.split(", ")
#     print(list_num)

# with open('/Users/andriisumnevych/Documents/even.txt', "w+") as file_even:
#     even_num = list(filter(lambda i: int(i) % 2 == 0, list_text))
#     file_even.write(even_num)
#
# with open('/Users/andriisumnevych/Documents/odd.txt', "w+") as file_odd:
#     odd_num = list(filter(lambda i: int(i) % 2 != 0, list_text))
#     file_odd.write(odd_num)

#  ver.2
# with open('/Users/andriisumnevych/Documents/even.txt', "w") as file_even:
#     list_even = list(filter(lambda i: int(i) % 2 == 0, list_num))
#     letter_text1 = ", ".join(list(map(lambda i: str(i), list_even)))
#     file_even.write(letter_text1)
#
# with open('/Users/andriisumnevych/Documents/odd.txt', "w") as file_odd:
#     list_odd = list(filter(lambda i: int(i) % 2 != 0, list_num))
#     letter_text2 = ", ".join(list(map(lambda i: str(i), list_odd)))
#     file_odd.write(letter_text2)

# 3 - Завдання

# ver.1
# with open('/Users/andriisumnevych/Documents/line.txt', "w+") as file_line:
#     file_line.write(('*'*5 + '\n')*5)

# ver.2
# for i in range(5):
#     with open('/Users/andriisumnevych/Documents/line.txt', "a") as file_line:
#         file_line.write('*' * 5)
#         file_line.write('\n')

# 4 - Завдання

# for i in range(5):
#     i += 1
#     with open('/Users/andriisumnevych/Documents/line1.txt', "a") as file_line:
#         file_line.write('*' * i)
#         file_line.write('\n')

#5 - Завдання

# ver.1
# for i in range(5):
#     with open('/Users/andriisumnevych/Documents/line.txt', "a") as file_line:
#         c = (' '*(i*1))
#         file_line.write(c+'*')
#         file_line.write('\n')
#
# # ver.2
# with open('/Users/andriisumnevych/Documents/line1.txt',"w",encoding='utf-8') as file_text:
#     for i in range(5):
#         for r in range(5):
#             if i==r:
#                 file_text.write("*")
#             else:
#                 file_text.write(" ")
#         file_text.write("\n")

# 6 - Завдання

# input = input("Enter text > 1,2,5,6,7,8,")
# random set = from 1 to 99
# file
# number input = number range() random

# ver.1

# numbers = set(input("Enter numbers > ").split(","))                                         # введення чисел
# numbers_random = set([str(random.randint(1, 99)) for i in range(len(numbers))])         # генерація чисел
# print(numbers)                                                                                # виведення чисел
# print(numbers_random)                                                                         # виведення чисел
# text = numbers & numbers_random                                                             # перетворення чисел
# print(text)                                                                                   # виведення чисел
# with open("/Users/andriisumnevych/Documents/numbers.txt", "w+") as file_text:                 # запис у файл
#     file_text.write(",".join(text))                                                           # запис у файл

# ver.2

# a = input("list number = ")
# # list_num=set(list(a.split(",")))
# list_num1 = set(list(map(lambda i: int(i), list(a.split(",")))))
# print(list_num1)
# list_num2 = set([random.randint(1, 10) for i in range(len(list_num1))])
# print(list_num2)
#
# list_num12 = list_num1 & list_num2
# print(list(list_num12))
#
# with open("C:/Users/Lenovo/Desktop/testpython.txt", "a") as file_line:
#     file_line.write(", ".join(list(map(str, list_num12))))

