# 1. Завдання

# Створіть за допомогою генератора списків список, які виведе всі значення з інтервалу, початок і кінець якого створюється у випадковому порядку.

# Підказка: при вирішенні використовуємо random, як варіант використовувати перший random в інтервалі від 0 до 10, а другий random від 50 до 60.

# Для отриманого списку порахуйте:

#        a) Суму чисел;
#        b) Максимальне число;
#        c) Мінімальне число;
#        d) Зробіть сортування за спаданням;
#        e) Порахуйте суму чисел з цього інтервалу, які поділяються на 3 та 7;
#        f) Знайдіть середнє значення чисел зі списку.

##import random
##
##a = random.randint(0, 10)
##b = random.randint(50, 60)
##
##i = 0
##num_list = []
##num_list2 = []
##
##for i in range(a, b):
##    num_list.append(i)
##    # print(i,end=" ")
##    if i % 3 == 0 and i % 7 == 0:
##        num_list2.append(i)
##
##print(num_list)
##
##print("a) Сума чисел >", sum(num_list))
##print("b) Максимальне число >", max(num_list))
##print("c) Мінімальне число >", min(num_list))
### num_list.sort(reverse=True)
##print("d) Сортування за спаданням >", num_list[::-1])
##print("Числа які поділяються на 3 та 7 >", num_list2)
##print("e) Сума чисел, які поділяються на 3 та 7 >", sum(num_list2))
##print("Кількість чисел в списку >", len(num_list))
##print("f) Середнє значення чисел зі списку >", sum(num_list) / len(num_list))

# 2. Завдання

# Користувач із клавіатури вводить текст:

#        Python is a popular programming language known for its simplicity and readability. It has a wide range of applications and is used for web development, data analysis, artificial intelligence, and more. Python's extensive libraries and frameworks make it highly versatile, and its beginner-friendly syntax allows new programmers to quickly learn and start coding. Its community-driven approach and vast resources make Python a go-to language for both beginner and experienced developers.

# Необхідно знайти:

#        a) Загальна кількість символів, що входять до тексту;
#        b) Вивести слова довжина яких більше 8;
#        c) Вивести слова довжина яких більша або дорівнює 4 і менше 8;
#        d) Порахувати скільки разів зустрічається “and” у тексті;
#        e) Порахуйте скільки слів у тексті;
#        f) Порахуйте скільки речень у тексті;
#        g) Порахуйте скільки разів зустрічається буква “p” та “P” у тексті.

# text = input("Enter text: ")
text = "Python is a popular programming language known for its simplicity and readability. It has a wide range of applications and is used for web development, data analysis, artificial intelligence, and more. Python's extensive libraries and frameworks make it highly versatile, and its beginner-friendly syntax allows new programmers to quickly learn and start coding. Its community-driven approach and vast resources make Python a go-to language for both beginner and experienced developers."
print(text)
print(type(text))
text_list = text.split()
print(text_list)
print(type(text_list))
print("a) Кількість символів в текстів >", len(text))

long_word = []
short_word = []

for i in range(len(text_list)):
    # print(text[i], end="")
    if len(text_list[i]) > 8:
        long_word.append(text_list[i])
    if len(text_list[i]) >= 4 and len(text_list[i]) < 8:
        short_word.append(text_list[i])

print("b) Слова довжина яких більше 8 >", len(long_word))
print("Слова більше 8 символів >", long_word)
print("c) Слова довжина яких більша або дорівнює 4 і менше 8 >", len(short_word))
print("Слова від 4 до 8 символів >", short_word)
print("d) Кількість разів зустрічається “and” у тексті >", text.count("and"))
print("e) Кількість слів у тексті >", len(text_list))
print("f) Кількість речень у тексті >", text.count("."))
print("g) Кількість разів зустрічається буква “p” та “P” у тексті >", text.count("p") + text.count("P"))