import random
##
### Функція із постійгим значенням
##def constantvalue():
##    return 2
##
##def multiten(b):
##    return b*10
##
##def randomfunc():
##    a = random.randint(10,99)
##    print(a)
##    return a
##
##    
##
###---------main-------------
##
##a = input("Number = ")
##
##if a.isdigit()==True:
##    print(multiten(int(a))*randomfunc())
##else:
##    Print("NOT")


# select ^2 or ^3

def kvadrat():
    num**2

def kub():
    num**3

#---------main----------

num = int(input("enter number > "))

print("Зробіть вібир:\n1. Квадрат\n2. Куб")

if num == 1:
    print(f"Квадрат = {kvadrat()}")
elif num == 2:
    print(f"Куб = {kub()}")
##else:
##    print("Error")
