##Завдання 1.
##
##    Користувач вводить з клавіатури чотири числа, необхідно знайти мінімальне та
##    максимальне число.
##
##        Наприклад:
##
##    Користувач вводить: 5, 8, -2, 10.
##    На виході отримує: min number = – 2, max number = 10.

##print("Enter four numbers from the keyboard:")
##
##num1=int(input("Number 1 = "))
##num2=int(input("Number 2 = "))
##num3=int(input("Number 3 = "))
##num4=int(input("Number 4 = "))
##
##num_min=min(num1,num2,num3,num4)
##print("Minimum number: ",num_min)
##
##num_max=max(num1,num2,num3,num4)
##print("Maximum number: ",num_max)

##Завдання 2.
##
##    Користувач вводить з клавіатури час у секундах, який минув з початку доби. Необхідно
##    порахувати, скільки годин, хвилин та секунд пройшло після опівночі.
##
##        Наприклад:
##
##    Користувач вводить: 2500; Результат: 00:41:40.
##    Користувач вводить: 10002; Результат: 02:46:42.

##time=int(input("Enter the time in seconds that has passed since the beginning of the day: "))
##
##h=int(time/60/60) # Перетворюємо секунди в години
##m=int((time-(h*60*60))/60) # Вираховуємо хвилини
##s=int(time%60) # Залишок від хвилин = секунди
##
##print(f"It's past midnight: {h}:{m}:{s}")

### ver.2
##
##import time
##
##t=int(input('Время в секундах: '))
##h=t//3600
##m=(t%3600)//60
##s=t%60
##a=time(h,m,s,)
##print('V1. После полуночи прошло:','{0:=02}:{1:=02}:{2:=02}'.format(h,m,s))
##print('V2. После полуночи прошло:',a)
##print('\n')

##Завдання 3.
##
##    Користувач вводить тризначне число, необхідно знайти:
##    а) дзеркальне число;
##    б) суму цих трьох чисел;
##    в) добуток цих трьох чисел;
##    г) різницю між цими трьома числами за модулем.
##
##        Наприклад: 582
##
##    а) 285; б) 582 + 285 = 867; в) 582 * 285 = 165 870; г) |582 – 285| = 297.

##num=input("Enter a three-digit number: ")
##
##print("A =",num[::-1])
##print("B =",int(num)+int(num[::-1]))
##print("C =",int(num)*int(num[::-1]))
##print("C =",int(num)-int(num[::-1]))

##Завдання 4.
##
##    Натуральне число називається числом Армстронга, якщо сума цифр числа, зведеного в n-у
##    ступінь, де n - кількість цифр у числі, дорівнює самому числу. Напишіть програму, яка
##    покаже на виході, чи є дане число, числом Армстронга.
##
##        Наприклад:
##
##    153 = 13+53+33, число Армстронга.
##    111= 13+13+13, не є числом Армстронга.

##import random
##
##number=random.randint(100,1000)
##print(number)
##
### ver.1
##
##a=number//100
###print(a**3)
##b=number//10%10
### print(b**3)
##c=number%10
### print(c**3)
##
##if number==a**3+b**3+c**3:
##    print("Armstrong's number:",number)
##else:
##    print("Is not an Armstrong number:",number)
##
### ver.2
##
##if number==(number//100)**3+(number%100//10)**3+(number%10)**3:
##    print("Armstrong's number:",number)
##else:
##    print("Is not an Armstrong number:",number)
##
##Завдання 5.
##
##    Користувач вводить двозначне число необхідно віддзеркалити це число, а також зробити
##    перевірку, чи ці обидва числа є парними; обидва числа непарні; одне парне, інше не парне.
##
##        Приклад:
##
##    Введення: 26, дзеркальне число 62. Висновок: Обидва числа парні.
##    Введення: 38, дзеркальне число 83. Висновок: Одне парне, друге не парне.
##    Введення: 17, дзеркальне число 71. Висновок: Обидва непарні.

##a=input("Enter a two-digit number from 10 to 99: ")

# ver.1

##num=a[::-1]
###print(num)
##num1=int(num[0])
###print(num1)
##num2=int(num[1])
###print(num2)
##
##if num1%2==0 and num2%2==0:
##    print(f"Input: {a}, mirror number {num}. Conclusion: Both numbers are even.")
##elif num1%2==0 and num2%2!=0 or num1%2!=0 and num2%2==0:
##    print(f"Input: {a}, mirror number {num}. Conclusion: One is even, the other is not even.")
##else:
##    print(f"Input: {a}, mirror number {num}. Conclusion: Both are odd.")

#ver.2

##if int(a[::-1][0])%2==0 and int(a[::-1][1])%2==0:
##    print(f"Input: {a}, mirror number {int(a[::-1])}. Conclusion: Both numbers are even.")
##elif int(a[::-1][0])%2==0 and int(a[::-1][1])%2!=0 or int(a[::-1][0])%2!=0 and int(a[::-1][1])%2==0:
##    print(f"Input: {a}, mirror number {int(a[::-1])}. Conclusion: One is even, the other is not even.")
##else:
##    print(f"Input: {a}, mirror number {int(a[::-1])}. Conclusion: Both are odd.")

##Завдання 6.
##
##    Користувач вводить два числа a, b. Якщо обидва числа позитивні, тоді буде розрахунок за
##    формулою a*b + c, де число з (визначається у випадковому порядку з інтервалу від 0 до
##    1000), якщо обидва числа є негативними, тоді буде розрахунок за формулою a*b*c, якщо
##    хоча б одне число негативне тоді буде розрахунок за формулою a * c + b * c.

##import random

### ver.1
##
##a=int(input("Enter num A: "))
##b=int(input("Enter num B: "))
##
##if a>0 and b>0:
##    c=random.randint(0,1000)
##    print(f"A={a}, B={b}, C={c} (a*b+c) Result: {(a*b)+c}")
##elif a>0 and b<0 or a<0 and b>0:
##    c=random.randint(0,1000)
##    print(f"A={a}, B={b}, C={c} (a*c+b*c) Result: {(a*b)+(b*c)}")
##else:
##    c=random.randint(0,1000)
##    print(f"A={a}, B={b}, C={c} (a*b*c) Result: {a*b*c}")

### ver.2
##
##a=int(input("Enter num A: "))
##b=int(input("Enter num B: "))
##c=random.randint(0,1000)
##
##if a>0 and b>0:
##    print(f"A={a}, B={b}, C={c} (a*b+c) Result: {(a*b)+c}")
##elif a>0 and b<0 or a<0 and b>0:
##    print(f"A={a}, B={b}, C={c} (a*c+b*c) Result: {(a*b)+(b*c)}")
##else:
##    print(f"A={a}, B={b}, C={c} (a*b*c) Result: {a*b*c}")
