# Завдання 1 +

# ver.1

##number = int(input("Enter a number: "))
##if number == 1:
##    print("0")
##elif number == 0:
##    print("1")
##else:
##    print("Error. Enter the number 0 or 1!")

# ver.2

##a=int(input("Num: "))
##print("Result",0**a)

# ver 2.1

##a=int(input("Num: "))
##print("Result",1-a)

# Завдання 2 +

##import math
##
##a=float(input("Enter numbers a: "))
##b=float(input("Enter numbers b: "))
##c=float(input("Enter numbers c: "))
##print("a =",a)
##print("b =",b)
##print("c =",c)
##print(a+b+c)
##print(a*b*c)
### ver.1
##print(round(pow((a*b*c),1/3),2))
### ver.2
##print(round(math.cbrt(a*b*c),2))

# Завдання 3 +

##a=float(input("Enter a: "))
##b=float(input("Enter b: "))
##area=a*b*0.5
##print("Area:",round(area,2))

# Завдання 4 +

##cel=input("Вкажіть температуру в градусах цельсій: ")
##far=float(cel)*1.8000+32
##print("Температура у Фаренгейтах: ",round(far,2))


# Завдання 5 +

##import random
##import math
##
##a=random.randrange(1,10)
##b=random.randrange(11,99)
##c=random.randrange(1,100)
##result=math.sqrt(a**2+b**2)/c*((a*b*c)/(a+b+c))
##print(round(result,2))
##print(a,b,c)

#ver.2

##import random
##
##a=random.randint(1,10)
##b=random.randint(11,99)
##c=random.randint(1,100)
##
##t1=(a**2+b**2)**(1/2)
##t12=t1/c
##
##t3=a*b*c
##t4=a+b+c
##t34=t3/t4
##
##print("Result= ",round(t12*t34,2))

# Завдання 6 +

##import random
##
##a=int(input("Ener a: "))
##b=int(input("Ener b: "))
##c=random.randrange(10,1000)
##print(c)
##c1=a<c<b or a>c>b
##print(c1)

