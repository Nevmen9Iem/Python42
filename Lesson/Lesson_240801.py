# print(text.capitalize()) # Всі букви переводи в нижній регістр крім 1-ї
# print(text.lower()) # Всі букви переводи в нижній регістр
# print(text.upper()) # Всі букви переводи в верхній регістр
# print(text.title()) # то саме що ввели
# print(text.isalnum()) # перевіряє чи текст тільки із цифр
# print(text.isalpha()) # перевіряє чи текст тільки із букви
# print(text.isdigit()) # перевіряє чи текст тільки із цифр
# print(text.isspace()) # перевіряє чи є в тексті пробіли

##text = "Phyton175 world hello lesson city mobile. Phyton? Phyton? Phyton"

# Phyton175
##a = input("Text: ")

##for i in range(len(a)):
##    if (a[i].isalpha()):
##        print(ord(a[i]),end=" ")

# Функція replace - міняє слова, букву. reverce

##text = "Phyton175 world hello lesson city mobile. Phyton? Phyton? Phyton"
##new_text1 = text.replace ("Python","Java")
##new_text2 = text.replace("o","@").replace("m","!").replace("w","K")
####new_text3 = text.replace("o","@",3) - # міняє о на @ перших 3 о
##
##print(text[::-1])

##задача міняєм A на W f - i j - m e - y p-s

# text = "The company Apple has found new personal tools for all citizens of New Jersey."
# text2 = text.replace("A","W").replace("f","i").replace("j","m").replace("e","y").replace("p","s")
# text3 = text[::3]
# text4 = 0
# # print(text2)
# # print(text[::-1])
# # print(text3)
# # print(text4)
# summ = 0
# for i in range(len(text3)):
#    if (text3[i].isalpha()):
#        summ = summ + ord(text3[i])
#        print(ord(text3[i]),end=" ")
#
# Задача

##text="The company Apple has found new personal tools for all citizens of New Jersey."
##
##new_text=text.replace("A","W").replace("f","i").replace("j","m").replace("e","y").replace("p","s")
##text_new=new_text[::-1]
##text_text=text_new[::3]
##
##print(text_new)
##print(text_text)
##print()
##
### Кожне третє число текста переводимо в числа і рахуємо їх суму
## 
##summ=0
##
##for i in range(len(text_text)):
##    if(text_text[i].isalpha()):
##        summ=summ+ord(text_text[i])
##        print(ord(text_text[i]), end=" ")
##print("\n")
##print("Total sum", summ)
##
### Перевіряємо чи число ціле
## 
##if summ % 2 == 0:
##    print ("Ціле(Even) >",summ)
##else:
##    print ("Не ціле(Odd) >",summ)

# Задача

##    1  2  3  4  5 
## 1 11 12 13 14 15
## 2 21 22 23 24 25
## 3 31 32 33 34 35
## 4 41 42 43 44 45
## 5 51 52 53 54 55


##import random
##
##c = True
##
##while True:
##    print(
##        "Для старту нажміть > 1\n"
##        "Для завершення нажміть > 0"
##)
##    c = int(input())
##    if c == 1:
##        c = True
##        print("Продовжуємо")
##    elif c == 0:
##        print("Кінець")
##        break
##    a = 5
##    b = 5
##    r = random.randint(2,9)
##    print("r =",r)
##    
##    for i in range(a):
##        for j in range(a):
##            if (i+j)%r==0:
##                print("#",end=" ")
##            else:
##                print(" ",end=" ")
##        print()       

