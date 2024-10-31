##import random
##
##
##def month():
##    mon=random.randint(1,12)
##    print('Месяц:',mon)
##    return mon
## 
##def day():
##    if month()==2:
##        d=random.randint(1,29)
##    elif month()==4 or month()==6 or month()==9 or month()==11:
##        d=random.randint(1,30)
##    elif month()==1 or month()==3 or month()==5 or month()==7 or month()==8 or month()==10 or month==12:
##        d=random.randint(1,31)
##    print('День:',d)
##    return d
## 
## 
##day()
##
##
##import random

##def month():
##    mon=random.randint(1,12)
##    print('Месяц:',mon)
##    return mon
## 
##def day():
##    if month()==2:
##        d=random.randint(1,29)
##    elif month()==4 or month()==6 or month()==9 or month()==11:
##        d=random.randint(1,30)
##    elif month()==1 or month()==3 or month()==5 or month()==7 or month()==8 or month()==10 or month==12:
##        d=random.randint(1,31)
##    print('День:',d)
##    return d
## 
## 
##day()

# filter

# def f20(a):
#     if a<20:
#         return False
#     else:
#         return True
#
# list_num = [10,20,30,18,23,35,12,27,39,9,29,33]
#
# new_list = filter(f20,list_num)
# for i in new_list:
#     print(i, end=" ")
#
# ##print(new_list)
#
# new_list1 = list(filter(f20,list_num))
# print(new_list1)
#
# new_list2 = list(filter(lambda i: i>=20,list_num))
# print(new_list2)
#
# list_text=["Category",5,10,"Movie","Game",20,18,"App","Source",50]
#
# new_list1=list(filter(lambda i: i if str(i).isdigit()==True else False,list_text))
# new_list2=list(filter(lambda i: i if str(i).isalpha()==True else False,list_text))
#
# print(sum(new_list1))
# print(new_list2)


# list_num = [1,4,5,11,8,9,21,10,-15]

# new_list = list(lambda i=i: i**3 for i in list_num)
# #print(new_list)
# for i in new_list:
#    print(i(), end=" ")
#
# print()
#
# new_list1 = list(map(lambda i: i**3, list_num))
# print(new_list1)
#
# new_list2 = list(map(lambda i: i if i>0 else 100, list_num))
# print(new_list2)

# Зробити із парних непарні а із непарних - парні

#new_list3 = list(map(lambda i: i+1 if i%2==0 else i-1, list_num))
#print(new_list3)

# із спіска зробити строки

#new_list4 = list(map(lambda i: str(i+1) if i%2==0 else str(i-1), list_num))
#print(new_list4)

# import random
#
# list_num = [random.randint(-20,20) for i in range(15)]
# print(list_num)
# new_list1 = list(map(lambda i: 0 if i<0 else i,list_num))
# print(new_list1)
# new_list2 = list(filter(lambda i: i>0,list_num))
# print(new_list2)

# reduce (reduce => sum)