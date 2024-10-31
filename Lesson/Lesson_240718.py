##print(18/7)
##print(18%7)
##print(18//7)

##a=int(input("Number=")
##
##if a%2==0

# Завдання 1

##import random
##
##a=random.randint(1,277)
##
##if a%2==0:
##    print("Even","\nNum =",a)
##else:
##    print("Odd","\nNum =",a)

# Завдання 2

##import random
##
##a=random.randint(1,350)
##
##if a%2==0:
##    print("Odd","\nNum =",a+1)
##else:
##    print("Even","\nNum =",a-1)

#string -> text

##a="Hello Python!!!"
##print(len(a))

# Завдання 3

# ver.1

##a=input("str:")
##b=len(a)
##
##if b%2==0:
##    print("Even","\nNum =",b)
##else:
##    print("Odd","\nNum =",b)

# ver.2

##a=input("str:")
##
##if len(a)%2==0:
##    print("Even","\nNum =",a)
##else:
##    print("Odd","\nNum =",a)

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# H e l l o   P y t h  o  n  !  !  !  !

a="Hello Python!!!!"
print(a[:4]) #a[start:finish-1]
print(a[:len(a):5])
print(a[::-1])

# Завдання 4 (перевіряє чи обернене слово = a)

##a=input("Enter: ")
##b="Hello Python!!!!"
##b==a[::-1]
##if a==b:
##    print(True,a)
##else:
##    print(False,b)

# Завдання 5 (Вивести рандомну букву із текста)

import random

a="Hello Python!!!!"
b=random.randint(0,len(a)-1) #(0 -15)
print(len(a))
print(a[b])

##t=ord('a') # Перевод із букв в цифри
##r=chr(97)  # Перевод із цифр в в букви
##print(t,r)

# Завдання 6

##import random
##
##a=random.randint(65,90)
##print(a)
##print(chr(a))

# лінійне і функціональне програмування

# Завдання 7

##import random
##
##a="Hello Python!!!"
##b=random.randint(0,len(a)-1)
##
##print(b)
##c=ord(a[b])
##print(c)

# Завдання 8 (Обернути число)

##a=input("Num: ")
##b=a[::-1]
##print(b)

#ver.2

##a=47//10=4
##b=47-4*10
##c=7*10+4+74

#ver.3 (математичний)

##a=int(input("Num: "))
##
##a1=a//10
##a2=a-a1*10
##a3=a%10
##a21=a2*10+a1
##a31=a3*10+a1
##
##print("Enter ->",a)
##print(a21)
##print(a31)

# Завдання 9
#(Ввести текст і якщо він парний вивести рандомний символ від 65 до 90,
#а якщо ні то вивести від 33,64)

##import random
##
##a=input("Text: ")
##
##if len(a)%2==0:
##    print(a+chr(random.randint(65,90)))
##else:
##    print(a+chr(random.randint(33,64)))

