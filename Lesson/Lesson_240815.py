# text_list = [i * i for i in listlistc  if a > b or a > c]


# import random
#
# list = []
# even = []
#
# for i in range(30):
#     list.append(random.randint(65, 90))
#
# print(list)
# even_list = [i for i in list if i % 2 == 0]
# print(even_list)
# print(sum(even))
# even_chr = str("".join(chr(i) for i in even_list))
# print(even_chr)

# Варіант викладача

# list_num = []
# for i in range(30):
#     num = random.randint(65, 90)
#     list_num.append(num)
#
# print(list_num)
#
# list_even = [i for i in list_num if i % 2 == 0]
# print(list_even)
# print(sum(list_even))
#
# list_text = [chr(i) for i in list_even]
# print(list_text)
#
# word_text = "".join([chr(i) for i in [i for i in list_num if i % 2 == 0]])
# print(word_text)

# list_matrix = [[1, 2, 3], [7, 8, 9]]
# print(list_matrix)
#
# num = 0
#
# for i in range(len(list_matrix)):
#     for j in range(len(list_matrix[i])):
#         print(list_matrix[i][j])
#         num = num + list_matrix[i][j]
#
#
# print(num)


# num = 0
#
# for i in range(len(list_matrix)):
#     for j in range(len(list_matrix[i])):
#         num = num + list_matrix[i][j]
#
# print(num)

# list_m = [[1, 2, 3], [7, 8, 9]]
#
# list_mx = [[list_m[i][j] for j in range(len(list_m[i]))] for i in range(len(list_m))]
# print(list_mx)

# random matrix 3 x 3 (10,50)
#


# matrix = [[random.randint(10, 50) for i in range(3)] for j in range(3)]
# print(matrix)

# a = []
#
# for i in range(3):
#     b = []
#     for j in range(3):
#         b.append(random.randint(10, 50))
#     a.append(b)
# print(a)

# def number_num():
#     a = input("Name => ")
#     print("Hello,", a, "!")
#
#
# number_num()

# def number_num(a, b, c):
#     r = a * 2 + b ** 2 + c * 10
#     return r
#
#
# x = int(input("Enter a: "))
# y = int(input("Enter b: "))
# z = int(input("Enter c: "))
#
# number_num(x, y, z)

# Перероблена гра в кості з використанням функціонального програмування

# import random
#
#
# def selectOne(a, b):
#     if a == 0 and b != 0:
#         print("Winer Player1", a, b)
#     elif a % 2 != 0 and b % 2 == 0:
#         print("Winer Player2", a, b)
#     elif a == 0 and b == 0:
#         print("Win - Win", a, b)
#     else:
#         print("Lose - Lose", a, b)
#
#
# def selectTwo(a, b):
#     if a > b:
#         print("Winer Player1", a, b)
#     elif a < b:
#         print("Winer Player2", a, b)
#     else:
#         print("Win - Win", a, b)
#
#
# def selectThree(a, b):
#     num = int(input("Enter number of 1 to 36\n"))
#     i = min(abs(num - a), abs(num - b))
#     if i == abs(num - a):
#         print("Winer Player1", a, b)
#     elif i == abs(num - Player2):
#         print("Winer Player2", a, b)
#     else:
#         print("Win - Win", a, b)
#
#
# # main code
# Player1_cube1 = random.randint(1, 6)
# Player1_cube2 = random.randint(1, 6)
# Player1_cube3 = random.randint(1, 6)
# Player1_cube4 = random.randint(1, 6)
# Player1_cube5 = random.randint(1, 6)
# Player1_cube6 = random.randint(1, 6)
#
# Player1 = Player1_cube1 + Player1_cube2 + Player1_cube3 + Player1_cube4 + Player1_cube5 + Player1_cube6
#
# print(Player1)
#
# Player2_cube1 = random.randint(1, 6)
# Player2_cube2 = random.randint(1, 6)
# Player2_cube3 = random.randint(1, 6)
# Player2_cube4 = random.randint(1, 6)
# Player2_cube5 = random.randint(1, 6)
# Player2_cube6 = random.randint(1, 6)
#
# Player2 = Player2_cube1 + Player2_cube2 + Player2_cube3 + Player2_cube4 + Player2_cube5 + Player2_cube6
#
# print(Player2)
#
# a = int(input("Виберіть режим гри: \n1 - Even Odd \n2 - Sum (+) \n3 - Check number\n"))
#
# if a == 1:
#     selectOne(Player1, Player2)
# elif a == 2:
#     selectTwo(Player1, Player2)
# elif a == 3:
#     selectThree(Player1, Player2)

# def rand_list():
#     list_num = []
#     for i in range(20):
#         num = random.randint(65, 90)
#         list_num.append(num)
#     print(sum(list_num))
#     if sum(list_num) % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#
# # ------- main code ----------------
# rand_list()


# def rand_list():
#     list_num = []
#     for i in range(3):
#         num = random.randint(65, 90)
#         list_num.append(num)
#     return list_num
#
#
# # ------- main code ----------------
#
# a = rand_list()
# print(a)
# print(a[1])
