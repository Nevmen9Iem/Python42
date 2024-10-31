### Домашка за 01.08, Завдання 2
##
##    ######
##    #    #
##    #    #
##    #    #
##    ######
##

##a=int(input("a="))
##for i in range(a):
##    if i==0 or i==a-1:
##        print("#"*a,end="")
##    else:
##        print("#",end="")
##        for j in range(a-2):
##            print(" ",end="")
##        print("#",end="")
##    print("\n",end="")


##list_1 = list(("A","B","C"))
##print(list_1)
##
##list_2 = ["A","B","C"]
##print(list_2)
##
##list_3 = [5,4,3,"A","B","C",True,False,"D",[2,5,"D","F"]]
##print(list_3)
##print(type(list_3))
##
##text = "Python"
##list_4 = list(text)
##print(list_4)

#          0       1     2      3    4  5  6  7  8   9     10     11
##list_1=["Movie","Game","App","Play",10,20,50,70,80,100,"Mobile","IOS"]
##print(list_1)
##print(len(list_1))
##print(list_1[0])
##print(list_1[1:5])
##print(list_1[1:11])
##print(list_1[1:11:2])
##print(list_1[::-1]) # revers
##list_1[1] = "Store"
##print(list_1)

# max, min, sum, sorted => only number or only letter (Тільки цифри або тільки букви)

##list_num = [10,20,50,70,80,100]
##list_letter =["Movie","Game","App","Play","Mobile","IOS"]

##print(max(list_num))
##print(min(list_num))
##print(sum(list_num))
##print(sorted(list_num))
##print(sorted(list_letter))

##list_new = list_num + list_letter
##print(list_new)
##print(list_new*2)

#          0       1     2      3    4  5  6  7  8   9     10     11
# list_1=["Movie","Game","App","Play",10,20,50,70,80,100,"Mobile","IOS"]

# for i in list_1:
#    print(i)

# for i in list_1:
#    if i%2==0:
#        print(i) # Не працює

# for i in range(len(list_1)):
#    if i%2==0:
#        print(list_1[i])

# print("Clock" in list_1/)

# list_num = []
#
# for i in range(1,102,10):
#    list_num.append(i)     # one element
#
# print(list_num)

##list_1=["Movie","Game","App","Play",10,20,50,70,80,100,"Mobile","IOS","Mobile"]

##list_1.append("Clock") # добавляє 1 елемент в кінці списку
##print(list_1)

##list_12 = ["Watch","TV"]
##list_1.extend(list_12) # добавляє кілька елемент в кінці списку
##print(list_1)

##list_1.insert(0,"TV")  # добавляє елемент в початку списку (0)
##print(list_1)

##list_1.remove("Play")  # удаляє елемент із списку
##print(list_1)

##list_1.pop(8)  # удаляє елемент із списку (8)
##print(list_1)

##list_1.clear()  # удаляє всі елемент із списку
##print(list_1)

##print(list_1.index("Mobile")) # щоб узнати індекс елементу
##print(list_1.count("Mobile"))

##list index => "Mobile"

# list_1 = ["Movie", "Game", "App", "Play", 10, 20, 50, 70, 80, 100, "Mobile", "IOS", "Mobile"]
#
# list_num = []
#
# for i in range(len(list_1)):
#     if list_1[i] == "Mobile":
#         list_num.append(i)
#
# print(list_num)

##list.let.sort(reverce=False) # end reverce=True
##print(list_let)

##list.let.reverce()
##print(list_let)

##list_let2 = list_let1
##list_let2 = list_let1.coppy()
##print(list_let2 is list_let1)
