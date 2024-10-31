##if<logic>:
##    <operation>
##else:
##    <operation>

#cinema->movie->place->pop-corn->

##a=int(input("Num: "))

##if a<50:
##    print("<50")
##else:
##    print(">50")

##if a>0 and a<50:
##    print("0-50")
##else:
##    print(">50")

##a=int(input("Num: "))
##
##if a<0:
##    print("negative number")
##elif a>0 and a<50:
##        print("<50")
##else:
##    print(">50")

# Завдання 1

##import random
##
##a=random.randint(1,200)
##print(a)
##
##if a<100:
##    print("a<100")
##elif a>=100:
##    print("a>=100")
##else:
##    print(f"Erorr!")

# Завдання 2

##import random
##
##a= random.randint(1,200)
##b= random.randint(1,200)
##if a<b:
##    print("a<b",a,b)
##elif a==b:
##    print("a=b",a,b)
##else:
##    print("a>b",a,b)

# Завдання 3

##a=int(input("a = "))
##b=int(input("b = "))
##
##print("Select number: 1 +, 2 -, 3 *, 4 /")
##
##c=int(input("Select number: "))
##
##if c==1:
##    print("Result: a + b =", a+b)
##elif c==2:
##    print("Result: a - b =", a-b)
##elif c==3:
##    print("Result: a * b =", a*b)
##elif c==4:
##    print("Result: a / b =", a/b)
##else:
##    print("Error")

# Завдання 4

##a=int(input("Num a = "))
##b=int(input("Num b = "))
##
##print("Select action: 1 +, 2 -, 3 *, 4 /")
##
##c=input("Select action: ")
##
##if c=="+":
##    print("Result: a + b =", a+b)
##elif c=="-":
##    print("Result: a - b =", a-b)
##elif c=="*":
##    print("Result: a * b =", a*b)
##elif c=="/":
##    print("Result: a / b =", a/b)
##else:
##    print("Error")

# Завдання 5

##import random
##
##a=int(input("Num: "))
##b=random.randint(-100,100)
##print(b)
##
##if a>b:
##    print("Win Player")
##elif a<b:
##    print("Win bot")
##else:
##    print("Win - Win")

##a=int(input("Num: "))
##b=random.randint(-100,100)
##
##if a<b:
##    print("Result: a < b", a,b)
##elif a>b:
##    print("Result: a > b", a,b)
##else:
##    print("Result: a = b", a,b)

# Завдання 6 (Гра: Камінь, ножниці, бумага)

##K-1
##H-2
##B-3

##import random
##
##a=int(input("a ="))
##b=random.randint(1,3)

##if a==1 and b ==1:
##    print("Win-Win", "K", "K")
##elif a==1 and b ==2:
##    print("Win-Player", "K", "H")
##elif a==1 and b ==3:
##    print("Win-Player", "K", "B")
##
##elif a==2 and b ==1:
##    print("Win-Bot", "H", "K")
##elif a==2 and b ==2:
##    print("Win-Win", "H", "H")
##elif a==2 and b ==3:
##    print("Win-Player", "H", "B")
##
##elif a==3 and b ==1:
##    print("Win-Bot", "B", "K")
##elif a==3 and b ==2:
##    print("Win-Bot", "B", "H")
##elif a==3 and b ==3:
##    print("Win-Win", "B", "B")
##
##else:
##    print("Erorr")

#ver.2

##import random
##
##a=int(input("a ="))
##b=random.randint(1,3)
##
##if a==1 and b ==1 or a==2 and b ==2 or a==3 and b ==3:
##    print("Win-Win",a,b)
##elif a==1 and b ==2 or a==1 and b ==3 or a==2 and b ==3:
##    print("Win-Player",a,b)
##elif a==2 and b ==1 or a==3 and b ==1 or a==3 and b ==2:
##    print("Win-Bot",a,b)
##else:
##    print("Erorr",a,b)
