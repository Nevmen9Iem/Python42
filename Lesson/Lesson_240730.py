# for (параметр) in <value>:
#     <тіло>

# i - ітерація

# for i in range(1,10):
#      print(i)

# while <value>:
#     <тіло>(body)

# 1. i=1, i<=10 (True), print(i) 1, i1=i+1 i1=1+1=2
# 2. i=2, i<=10 (True), print(i) 2, i1=i1+1? i2=11+1=3
# 3. i=3, i<=10 (True), print(i) 3, i1=i2+3? i3=1+1=4
# ............
# 10. i=1, i<=10 (True), print(i) 1, i1=i+1? i1=1+1=2
# 11. i=11, i(11)<=10 (False), print(i) 1, i1=i+1? i1=1+1=2

# Завдання 1

# start a - random (10,50)
# start b - random (51,100)
# start c - random (10,50)
# from a to b, if step c

# import random
#
# a = random.randint(10,50)
# print(a)
# b = random.randint(51,100)
# print(b)
# c = int(input("Enter num: "))
# print(c)
# i = 1
# s=0
# while a<=b:
#     s=s+1
#     # print("Result: ",a,s-1)
#     a = a + c
# print("Result: ",s-1)

# Завдання 2 (Показати слово -1 буква)

# s="Python"

# ver.1

# while s:
#     print(s)
#     s=s[:-1]

# ver.2

### s="Python"
###
### for i in range(len(s),0,-1):
###     print(s[:i])

# Завдання 3

# a = int(input("Size a="))
# b = int(input("Size b="))
#
# for i in range(a):
#     for j in range(b):
#         if i==j:
#             print("@",end=" ")
#         else:
#             print(" ",end=" ")
#     print("\n",end=" ")
#
# print("\n", end="")

# ver.2
# a=int(input("Висота: "))
# b=int(input("Ширина: "))
#
# n=0
#
# while n<a:
#     n=n+1
#     print('*'*b)



# Домашка буде !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# a = int(input("Size a="))
# b = int(input("Size b="))
#
# for i in range(a):
#     for j in range(b):
#         if i%2==0 and j%2==0:
#             print("@",end="")
#         else:
#             print(" ",end="")


# Завдання 4.


# a = int(input("Size a="))
# b = int(input("Size b="))
#
# for i in range(a):
#     for j in range(b):
#         if (i+j)%2==0:
#             print("@",end="")
#         else:
#             print(" ",end="")
#     print("\n",end="")

# Завдання 5.

# text = "Phyton175 World Hello Lesson"
# text = "175"
# text = "Phyton175

# print(text.capitalize()) # Всі букви переводи в нижній регістр крім 1-ї
# print(text.lower()) # Всі букви переводи в нижній регістр
# print(text.upper()) # Всі букви переводи в верхній регістр
# print(text.title()) # то саме що ввели
# print(text.isalnum()) # перевіряє чи текст тільки із цифр
# print(text.isalpha()) # перевіряє чи текст тільки із букви
# print(text.isdigit()) # перевіряє чи текст тільки із цифр
# print(text.isspace()) # перевіряє чи є в тексті пробіли

# Визначаємо скільки цифр у тексті та вираховуємо їх суму

##text = "Phyton175 i25 100 751"
##summ=0
##for i in range(len(text)):
##    if (text[i].isdigit()):
##        # print(text[i].isdigit())
##        print(int(text[i]),end="")
##        summ=summ+int(text[i])
##        print(text[i],end="")
##print()
##print("Total sum =", summ)

# text = "Phyton175 world hello lesson city mobile."
#
# summ=1
# for i in range(len(text)):      # розбираємо речення на символи
#     if (text[i].isspace()):     # перевіряємо чи є пробіли
#         summ=summ+1             # зберігаємо пробіли у змінній
#         print(text[i],end="")
# print()
# print("Total sum =", summ)