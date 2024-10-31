# 1. Завдання

##    Напишіть програму,яка покаже всі автоморфні числа в інтервалі від 1 до 10000.
##    Автоморфні числа.
##    Натуральне число називається автоморфним, якщо його запис – це останні цифри його квадрата.

##        Наприклад: 25**2 = 625.

##automorphic = []
##
##for i in range(1,10000):
##    num_of_digits = len(str(i))
##    square = i**2
##    last_digits = square% pow(10,num_of_digits)
##    if last_digits == i:
##        automorphic.append(i)
##
##print("Automorphic number >", automorphic)
##        
        
# 2. Завдання

##    Напишіть програму, яка обчислює суму невідомої кількості натуральних чисел,
##    записану у вигляді символьного рядка.

##        Наприклад:

##        Введення рядок (text, формат string): “1 + 25 + 12 + 34 + 89”.
##        Виведення число (формат integer): 161.

##num_str = "1 + 25 + 12 + 34 + 89"
##
##sum_num = sum([int(i) for i in num_str.split() if i.isdigit()])
##
##print("Sum of numbers >", sum_num)

##3. Завдання
##
##   Напишіть програму, яка на вхід отримує число та два символи,
##   а на виході малює квадрат.
##
##       Користувач вводить число 5,
##
##       - перший символ #,
##       - другий символ @.
##
##       На виході:
##
##       ##@@##@@##
##       @@##@@##@@
##       ##@@##@@##
##       @@##@@##@@
##       ##@@##@@##

##num = int(input("Enter number > "))
##
##symbol_1 = input("Enter symbol 1 > ")
##symbol_2 = input("Enter symbol 2 > ")
##
##for i in range(num):
##        symbol = ""
##        for j in range(num):
##            if (i + j) % 2 == 0:
##                symbol += symbol_1 * 2
##            else:
##                symbol += symbol_2 * 2
##        print(symbol)

# 4. Завдання

##    Дан текст:

##    As of October 2023, several exciting PC games have been released or announced,
##    including titles like "Starfield" an action RPG set in space,
##    and "Lies of P" a dark reimagining of the Pinocchio tale.
##    Upcoming highly anticipated games include "Avowed" and "Hellblade II: Senua's Saga"
##    which are expected to push the boundaries of storytelling and graphics.
##    Keep an eye out for indie games as well,
##    as they often bring fresh and innovative gameplay experiences.
    
##        Необхідно, використовуючи функцію lambda, а також filter, map знайти:

##            a) Суму всіх цифр у тексті.
##            b) Кількість букв у тексті.
##            c) Кількість знаків пунктуації (, : . ‘ “).
##            d) Переведіть усі літери до числа, запишіть їх в один рядок.
##            e) Напишіть функцію, яка залишить усі слова більше 5 літер.

##def words_longer(text):
##    letters = list(filter(lambda x: len(x) > 5, text.split()))
##    letters = " ".join(letters)
##    print("e) Words longer than 5 letters >", letters)
##
##text_list = 'As of October 2023, several exciting PC games have been released or announced, including titles like "Starfield" an action RPG set in space, and "Lies of P" a dark reimagining of the Pinocchio tale. Upcoming highly anticipated games include "Avowed" and "Hellblade II: Senua\'s Saga" which are expected to push the boundaries of storytelling and graphics. Keep an eye out for indie games as well, as they often bring fresh and innovative gameplay experiences.'
##
##text2 = list(text_list)
##
##list_digit = list(filter(lambda i: i.isdigit(), text2))
##num_sum = sum([int(i) for i in list_digit])
##print("a) Sum >", num_sum)
##
##list_alpha = list(filter(lambda i: i.isalpha(), text2))
##num_alpha = len(list_alpha)
##print("b) Alpha >", num_alpha)
##
##punctuation_mark = list(filter(lambda i: i in [',', ':', '.', "'", '"'], text2))
##num_punctuation = len(punctuation_mark)
##print("c) Punctuation >", num_punctuation)
##
##text_ord = list(map(lambda i: ord(i), text2))
##print("d) Text_ord >", text_ord)
##
##words_longer(text_list)

