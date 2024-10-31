# Завдання 1

# a - 0 - 200 інтервал (більше - помилка)
# b = random(0,100)
# a < 100 появляється рандомний параметр b = 0 - 50 => (a*b), b = 51 -100 => (a+b)
# a > 100 появляється рандомний параметр b = 0 - 50 => (a/b), b = 51 -100 => (a-b)

##import random
##
##a=int(input("Enter num A: "))
##print(a)
##b=random.randint(0,100)
##print(b)
##
##if a<0 or a>200:
##    print("Eroor!!!")
##elif a>=0 and a<=100:
##    if b>=0 and b<=50:
##        print("Result:",a*b)
##    else:
##        print("Result:",a+b)
##elif a>=100 and a<=200:
##    if b>=0 and b<=50:
##        print("Result:",a/b)
##    else:
##        print("Result:",a-b)
##else:
##    print("Erorr !!!")

# step by step chat gpt

# Завдання 2

#chr() ord()
##Беремо 1 букву із слова if < 100 = random 97,122
##Беремо 1 букву із слова if > 100 = random 65,90

##import random
##
##a=input("Enter text: ")
##
##print(ord(a[0]))
##
##if ord(a[0])<100:
##    b=chr(random.randint(97,122))
##    print(b+a[1::])
##elif ord(a[0])>100:
##    c=chr(random.randint(65,90))
##    print(c+a[1::])

# Завдання 3

##a=int(input("Enter num A: "))
##print("Select action: \n1 - ** \n2 - * \n3 - +")
##c=int(input("Action num: "))
##
##if a==1:
##        b=int(input("Enter num B: "))
##        print("Result:",a**b)
##elif a==2:
##        b=int(input("Enter num B: "))
##        print("Result:",a*b)
##elif a==3:
##        b=int(input("Enter num B: "))
##        print("Result:",a+b)
      
# Завдання 4 Гра кості на, кожен ігрок кидає 6 кубиків)

# 6 сторін (1-6)
# 6-cube (1-6) random
# 2 user
# 1 - Even Odd, Win Even all time
# 2 - Sum (+) number cube, High num Win
# 3 - Check number (input(6-36))

import random

Player1_cube1=random.randint(1,6)
Player1_cube2=random.randint(1,6)
Player1_cube3=random.randint(1,6)
Player1_cube4=random.randint(1,6)
Player1_cube5=random.randint(1,6)
Player1_cube6=random.randint(1,6)
Player1=Player1_cube1+Player1_cube2+Player1_cube3+Player1_cube4+Player1_cube5+Player1_cube6
print(Player1)

Player2_cube1=random.randint(1,6)
Player2_cube2=random.randint(1,6)
Player2_cube3=random.randint(1,6)
Player2_cube4=random.randint(1,6)
Player2_cube5=random.randint(1,6)
Player2_cube6=random.randint(1,6)
Player2=Player2_cube1+Player2_cube2+Player2_cube3+Player2_cube4+Player2_cube5+Player2_cube6
print(Player2)

a=int(input("Виберіть режим гри: \n1 - Even Odd \n2 - Sum (+) \n3 - Check number\n"))

if a==1:
        if Player1==0 and Player2!=0:
                print("Winer Player1",Player1,Player2)
        elif Player1%2!=0 and Player2%2==0:
                print("Winer Player2",Player1,Player2)
        elif Player1==0 and Player2==0:
                print("Win - Win",Player1,Player2)
        else:
                print("Lose - Lose",Player1,Player2)
elif a==2:
        if Player1>Player2:
                print("Winer Player1",Player1,Player2)
        elif Player1<Player2:
                print("Winer Player2",Player1,Player2)
        else:
                print("Win - Win",Player1,Player2)
elif a==3:
        num=int(input("Enter number of 1 to 36\n"))
        i=min(abs(num-Player1),abs(num-Player2))
        if i==abs(num-Player1):
            print("Winer Player1", Player1,Player2)
        elif i==abs(num-Player2):
            print("Winer Player2", Player1,Player2)
        else:
            print("Win - Win", Player1,Player2)
        


