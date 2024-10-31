# Завдання 1

##a=int(input("Enter a number from 1 to 7: "))
##
##if a==1:
##    print("Monday")
##elif a==2:
##    print("Tuesday")
##elif a==3:
##    print("Wednesday")
##elif a==4:
##    print("Thursday")
##elif a==5:
##    print("Friday")
##elif a==6:
##    print("Saturday")
##elif a==7:
##    print("Sunday")
##else:
##    print("Erorr")

# Завдання 2

##a=int(input("Enter a number from 1 to 12: "))
##
##if a==12 or a==1 or a==2:
##    print("Winter",a)
##elif a==3 or a==4 or a==5:
##    print("Spring",a)
##elif a==6 or a==7 or a==8:
##    print("Summer",a)
##elif a==9 or a==10 or a==11:
##    print("Autumn",a)
##else:
##    print("Erorr")

# Завдання 3

##a=int(input("Num A: "))
##b=int(input("Num B: "))
##
##if a==b:
##    print("Result: The same numbers")
##elif a<b:
##    print("Result:",a,b)
##else:
##    print("Result:",b,a)

# Завдання 4

##import random

##a=int(input("Enter a number from 1 to 1000: "))
##b=random.randint(1,1000)
##
##if a%2==0 and b%2!=0:
##    print(a,b,"You Win")
##elif b%2==0 and a%2!=0:
##    print(a,b,"Bot Win")
##elif a%2==0 and b%2==0:
##    print(a,b,"Win - Win")
##else:
##    print(a,b,"Lost - Lost")

# Завдання 5 (Перетворення км/год в м/с)

##kh=float(input("Enter km/h: "))
##ms=kh*1000/3600
##print(round(ms,2),"m/s")

# Завдання 6

##color=input("Enter the color of the traffic light: ")
##
##if color=="red":
##    print("Stop")
##elif color=="green":
##    print("Go")
##elif color=="yellow":
##    print("Wait")
##else:
##    print("Error !!!")
