### 1. Задача
##
##a=input("Enter num: ")
##
##a1=int(a[0])
##a2=int(a[1])
##a3=int(a[2])
##a4=int(a[3])
##a5=int(a[4])
##a6=int(a[5])
##
##if len(a)==6 and a1+a2+a3==a4+a5+a6:
##    print("Happy")
##elif len(a)==6 and a1+a2+a3!=a4+a5+a6:
##    print("Nonhappy")
##elif len(a)!=6:
##    print("Erorr!!!")

### ver.2
##
##a=input("Enter num: ")
##
##a1=int(a[0])
##a2=int(a[1])
##a3=int(a[2])
##a4=int(a[3])
##a5=int(a[4])
##a6=int(a[5])
##
##if len(a)==6:
##    if a1+a2+a3==a4+a5+a6:
##        print("Happy")
##    else:
##        print("Nonhappy")
##else:
##    print("Erorr!!!")

# 2. Задача 2<=>5 1<=>6

##a=input("Enter num: ")
##
##a1=int(a[0])
##a2=int(a[1])
##a3=int(a[2])
##a4=int(a[3])
##a5=int(a[4])
##a6=int(a[5])
##
##if len(a)==6:
##    print(a6,a5,a3,a4,a2,a1,sep="")
##else:
##    print("Erorr!!!")

# 3. Задача ( 0-6 6-13 13-17 17-0)

##a=int(input("Enter num: "))
##
##if a>=0 and a<6:
##    print("Good Night")
##elif a>=6 and a<13:
##    print("Good Morning")
##elif a>=13 and a<17:
##    print("Good Day")
##elif a>=17 and a<=23:
##    print("Good Evening")
##else:
##    print("Erorr!!!")


# Цикли for/while

##for змінна in <завдання>:
##    <вказуємо що буде робити цикл>
##else:(він також є но його не вказують у for)
##
##    ##for i in range(10):
##    ##    # print(i+1,end=" ")
##    ##    # print(i*i,end=" ") # піднесення до квадрату

##for i in range(10):
##    if i==5:
##        print("Good")
##    else:
##        print("Bad")

##for i in range(10):
##    if i!=5 and i!=7 and i!=9:
##    if i%2==0:
##        print(i)
##    else:
##        continue

# break # break - пририває, continue - пропускає

##while <операція яку повинен виконати>:
##    <вказуємо що буде робити цикл>
##else:

# i=0
#
# while i<=10:
#     print(i)
#     i=i+1 # - лічильник називається (задає кількість операцій потрібно зробити)

# 0 while 0<=10: print(0) 0=0+1
# 1 while 0<=10: print(0) 1=1+1
# 2 while 0<=10: print(0) 2=2+1
# 3 while 0<=10: print(0) 3=3+1
# 4 while 0<=10: print(0) 4=4+1
# 5 while 0<=10: print(0) 5=5+1
# 6 while 0<=10: print(0) 6=6+1
# 7 while 0<=10: print(0) 7=7+1
# 8 while 0<=10: print(0) 8=8+1
# 10 while 0<=10: print(0) 9=9+1
# 11 while 0<=10: print(0) 10=10+1

# t=True
# while t==True:
#    a=int(input("a="))
#    b=int(input("b="))
#    print("Sum = ",a+b)
#    print()
#    print("Exit? [y/n]")
#    c=input("Answer = ")
#    if c=="n":
#        t=True
#    else:
#        t=False

# Гра у кості

#4.

##for i in range(10,100,5):
##    print(i,end=" ")

#5. Вивести числа від 10 до 100 які діляться на 3 і на 7

##for i in range(10,100):
##    if i%3==0 and i%7==0:
##        print(i,end=" ")

#6. Порахувати загальну суму цифр від 1 до 10 (55)

##summ=0
##for i in range(1,11):
##    summ=summ+i
##    print("Step ",i,"sum",summ)
##print()
##print("Total sum",summ)

# ver.2 із вводом

##a=int(input("number = "))
##summ=0
##for i in range(1,a+1):
##    summ=summ+i
##    print("step ",i, "sum ",summ)
##
##print()
##print("total sum ",summ)
