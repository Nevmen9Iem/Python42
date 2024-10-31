# S = pi*R^2, pi = 3.1415....,
# R
# ver.1
##r=float(input("r="))
#print("S= ",3.14*r*r)
# ver.2
#print("S= ",3.14*r**2)
# ver.3
##pi=3.14
#print("S= ",pi*r**2)
 
#ver.4
##pii=round(math.pi,2)
##print("S= ",pii*r**2)
#ver.5
##print("S= ",round(math.pi,2)*r**2)


#randint(start,fihish) -> integer -> start <= a <= fihish

import random
##a=random.randint(1,10)
##print(a)
 
#randrange(start,fihish,step)

##b1=random.randrange(1,10)
##b2=random.randrange(0,11,5)
##b3=random.randrange(10)
##print(b1)
##print(b2)
##print(b3)
 
#random()  0 <= c <= 1

##c1=random.random()
##print("c1=",round(c1*100,2))

##a=float(input("a="))
##b=random.randint(1,5)
###a^b+10
##print("b=",b, "result=", a**b+10)

##b=random.randrange(1,100)
##print(b)
##print(b>50)

##a=random.randrange(1,10)
##b=random.randrange(5,15)
##print(a,b)
##print(a>b)

import math

##r=random.random()
##r0=round(r*10,2)
##print("S= ",round(math.pi*math.pow(r0,2),2))

a=random.randrange(1,9)
b=random.randrange(10,100)
print(a,b)
print(str(a)+str(b))
print(a,b,sep="")
