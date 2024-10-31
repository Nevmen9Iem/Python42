# Завдання 1
from dataclasses import replace

# create random list (1,100), value 30
# filter (65,90)
# new_list => from numbers to letters
# join list

# import random

# list_num = [random.randint(1, 100) for i in range(30)]
# print(list_num)
# f_list = list(filter(lambda i: i if i > 65 and i < 90 else False, list_num))
# print(f_list)
# new_list = list(map(lambda i: chr(i), f_list))
# print(new_list)
# print(''.join(new_list))

# Завдання 2
# ver.my

# list_num = [11,15,17,1,2,8,9,36,41,47,48,24,51,7,27,31,74,78,81,16,33,56,90,97,94,20,13,8,6,64]
# even = [i for i in list_num if i%2==0]
# odd = [i for i in list_num if i%2!=0]
# print(f"{even} = {sum(even)}")
# print(f"{odd} = {sum(odd)}")
# if sum(even) > sum(odd):
#     print(f"Even = ({sum(even)}) > Odd = ({sum(odd)})")
# else:
#     print(f"Even = ({sum(even)}) < Odd = ({sum(odd)})")

# ver.2

# def sum_1(a):
#     list_ev=list(filter(lambda i: i%2==0 ,list_1))
#     print(list_ev)
#     list_od=list(filter(lambda i: i%2!=0 ,list_1))
#     print(list_od)
#     a=sum(list_ev)
#     b=sum(list_od)
#     if a>b:
#         print ('list_ev>list_od')
#         print ("sum_a = ", a,"  sum_b = ",b)
#     else:
#         print ('list_od>list_ev')
#         print ("sum_a = ", a,"  sum_b = ",b)
# #------
# list_1=[11,15,17,1,2,8,9,36,41,47,48,24,51,7,27,31,74,78,81,16,33,56,90,97,94,20,13,8,6,64]
# sum_1(list_1)

# Завдання 3

# text = "The Python is a new language for us. So, we started learning it a few months ago."
#
# list_text = list((text))
# print(list_text)
#
# list_new = list(filter(lambda i: i if i!="e" and i!="o" and i!="y" and i!="a" and i!="u" and i!="i" else False, list_text))
# print(list_new)
# print("".join(list_new))

# Завдання 4

# ver.my

# text = "The 1 position of our order is most important then 2. Please check 1 and 1 and 1 for us."
#
# text_new = text.replace("1", "first").replace("2", "second")
# print(text_new)
# list_letter = list(filter(lambda i: str(i) if str(i).isalpha() == True else False, text_new))
# print(list_letter)
# text_num = list(map(lambda i: ord(i), list_letter))
# print(text_num)
# print(sum(text_num))

# ver.2

##text = "The 1 position of our order is most important then 2. Please check 1 and 1 and 1 for us."
##
##new_text = text.replace("1", "first").replace("2", "second")
##print(new_text)
##list_text = list((text))
##list_letter = list(filter(lambda i: str(i).isalpha(), list_text))
##print(list_letter)
##list_num = list(map(lambda i: ord(i), list_letter))
##print(sum(list_num))

# Декорування функцій (функція у функції)

##def name1():
##    def name2():

##def Decorator(a):
##    print("Hello User")
##    def Text():
##        print("Code start working...")
##        a()
##        print("OK")
##    return Text
##
##@Decorator
##def Welcome():
##    print("Welcome")
##
##
##Welcome()

##def Decorator(a): #Welcome
##    print("Hello User")
##    def Text():
##        print("Code starts working...")
##        a() #Welcome()
##        print("OK")
##    return Text
## 
##def Decorator1(a): #Welcome
##    print("Good job")
##    def Text():
##        print("Python Code working...")
##        a() #Welcome()
##        print("Finish")
##    return Text
## 
## 
##@Decorator
##@Decorator1
##def Welcome():
##    print("Welcome")
## 
## 
##Welcome()

import random

##def even_odd(func):
##    if func()%2==0:
##        print("Even")
##    else:
##        print("Odd")
##
##@even_odd       
##def startnumber():
##    a=random.randint(1,1000)
##    print(a)
##    return a
##
###-------------main-------------
##
##startnumber

##def even_odd(func):
##    a=func()
##    if a%3==0:
##        print("Yes, 3 ")
##    else:
##        print("No, 3 ")
## 
## 
##@even_odd
##def startnumber():
##    a=random.randint(1,1000)
##    print(a)
##    return a
## 
###----------main---------------------
## 
##startnumber

##def even_odd(func):
##    a=func()
##    if a%2==0:
##        print("Even")
##    else:
##        print("Odd")
##
##@even_odd       
##def startnumber():
##    a=random.randint(1,1000)
##    print(a)
##    return a
##
###-------------main-------------
##
##startnumber


def decorator(a):
    if a()%2==0 :
        print("even")
    else:
        print("Odd")
    return a
def decorator1(a):
    print(len(str(a())))
    return a
 
@decorator
@decorator1
def welcome():
    a=random.randrange(1,1000)
    print(a)
    return a
welcome
