# Завдання 1.

# Користувач із клавіатури вводить елементи списку:

# [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20].

# Необхідно знайти:

# + a) Скільки разів число 2 є у списку (необхідно при розрахунках рахувати числа за модулем);
# + b) Покажіть максимальне число зі списку;
# + c) Покажіть мінімальне число зі списку;
# + d) Зробіть сортування;
# + e) Порахуйте кількість негативних чисел;
# + f) Порахуйте кількість позитивних чисел;
# + g) Порахуйте кількість нулів 0.

# list_1 = list(map(int, input("Enter numbers > ").split(",")))
# print(type(list_1))
# print(type(list_1[0]))

# number_of_deuces = 0
# index_deuces = 0
# negative_numbers = 0
# positive_numbers = 0
# number_of_zeros = 0

# for i in range(len(list_1)):
#     if list_1[i] == 2 or list_1[i] == -2:
#         index_deuces += 1
#     if list_1[i] < 0:
#         negative_numbers += 1
#     if list_1[i] >= 0:
#         positive_numbers += 1
#     if list_1[i] == 0:
#         number_of_zeros += 1

# print(2 in list_1)
# print("a)", "Idex deuces >", index_deuces)
# print("a)", "Idex deuces_2 >", [i for i, j in enumerate(list_1) if j == 2 or j == -2])
# print("b)", "Max num >", max(list_1))
# print("c)", "Min num >", min(list_1))
# print("d)", "Sort num >", sorted(list_1))
# print("e)", "Negative_numbers >", negative_numbers)
# print("f)", "Positive_numbers >", positive_numbers)
# print("g)", "Number of zeros >", number_of_zeros)

# Завдання 2.

# Користувач із клавіатури вводить елементи списку:

# [5, 0, 1, 5, 10, 11, 15, 3, 18, 7, 2, 10, 8, 21, 19, 36, 5, 47].

# Необхідно знайти:

# + a) Суму всіх чисел, що входять до списку;
# + b) Кількість елементів, що входять до списку;
# + c) Середнє значення елементів списку;
# + d) Показати усі парні значення списку;
# + e) Показати всі непарні значення списку.

# list_1 = list(map(int, input("Enter numbers > ").split(",")))

# even = []
# odd = []
# sum_num = 0
# sum_len = 0

# for i in range(len(list_1)):
#     sum_len += 1
#     sum_num += list_1[i]
#     if list_1[i] % 2 == 0:
#         even.append(list_1[i])
#     else:
#         odd.append(list_1[i])

# print("a)", sum_num)
# print("a1)", sum(list_1))
# print("b)", sum_len)
# print("b1)", len(list_1))
# print("c)", round(sum_num / sum_len, 2))
# print("d)", even)
# print("e)", odd)

# Завдання 3.

# Користувач із клавіатури вводить елементи списку:

# ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second","First","Lamp","Year","Joi n","Jump","Ice","Brother","Free","Word","Year","Page"].

# Необхідно знайти:

# a) - Сортування списку;
# b) + Кількість елементів, що входять до списку;
# c) + Показати кожен третій елемент списку [“Car”, “Word”, ....];
# d) + Додати до списку такі елементи "Play", "Game", "Movie", "Star";
# e) -/+ Видалити зі списку “First”, “Year”, “Ice”, “Street”;
# f) + Показати список у зворотному порядку;
# g) + Створити список, що складатиметься з елементів під індексами 2, 5, 7, 10, 15, 17, 19, 20.

# text = list(input("Enter text > ").split("'"))

# text = ["Car", "Cat", "Dog", "Word", "Street", "Tree", "Free", "Tax", "House", "Second", "First", "Lamp", "Year",
#         "Joi n", "Jump", "Ice", "Brother", "Free", "Word", "Year", "Page"]

# print(text)

# text1 = text.copy()
# print("Text >", text)

# print("a)", text.sort())
# print("b)", len(text))
# print("c)", text[::3])
# text_extend = ["Play", "Game", "Movie", "Star"]
# text1.extend(text_extend)
# print("d) Extend", text1)
# text2 = text.copy()
# text2.remove("First"), text2.remove("Year"), text2.remove("Ice"), text2.remove("Street"), text2.remove("Year")
# print("e) Remove", text2)
# text3 = text.copy()
# print("f)", text3[::-1])

# list1 = [text[2], text[5], text[7], text[10], text[15], text[17], text[19], text[20]]
# print("g)", list1)

# СОРТУВАННЯ НЕ ПРАПЦЮЄ! НЕ МОЖУ ЗРОЗУМІТИ ЧОМУ
# ТАКОЖ Є ПРОБЛЕМА ІЗ remove ЯКЩО ВВОДИТИ ТЕКСТ ЧЕРЕЗ input
