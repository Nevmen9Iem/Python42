class Borsch:
    ingridients = ['beet', 'cabbage', 'bean', 'potate']
    spices = ['red_pepper', 'chile_pepper', 'garlic']
    meat = 'pork'  # beef, chicken
    value = 3
    date_to_expire = '2024-10-11'
    temperature = 3

    def boiled(self, temperature):
        self.temperature = temperature # атрибут обʼекту класу, аргумент обʼєкту класу, поле обʼєкту класу, змінна обʼєкту класу
        return f'boiled to {temperature} degreece'

    def eat(self):
        return f'eat borsch'

    def show(self):
        return f'you can see current borsch'

    def change_meat(self, new_meat):
        self.meat = new_meat
    # def add_ingredient(self, ingredient):
    #     self.ingridients = Borsch.ingridients
    #     self.ingridients.append(ingredient)


odesa_borsch = Borsch()
print(odesa_borsch.show())
print(odesa_borsch.temperature)
print(odesa_borsch.boiled(100))
print(odesa_borsch.temperature)

kiyv_borsch = Borsch()
kiyv_borsch.temperature = 40  # не робіть так, напряму змінювати поля не дуже ок
print(kiyv_borsch.date_to_expire)
print(kiyv_borsch.ingridients)
# kiyv_borsch.ingridients.append('onion') # це працювати не буде, змінює поле класу
# kiyv_borsch.ingridients.append('carrot') # це працювати не буде, змінює поле класу
# kiyv_borsch.ingridients.append('smoked_pear') # це працювати не буде, змінює поле класу
#
# odesa_borsch.ingridients.append('tomato') # це працювати не буде, змінює поле класу


# print(kiyv_borsch.ingridients)
# print(odesa_borsch.ingridients)
#
# kiyv_borsch.add_ingredient('onion')
# kiyv_borsch.add_ingredient('carrot')
# kiyv_borsch.add_ingredient('smoked_pear')
#
# odesa_borsch.add_ingredient('tomato')
#
# print(kiyv_borsch.ingridients)
# print(odesa_borsch.ingridients)

#Багатострочне коментування виділити та натиснути
# Windows (Ctrl + /) MacOS (Cmd + /)

print(odesa_borsch.meat)
odesa_borsch.change_meat('beef')
print(odesa_borsch.meat)

# ООП

# Інкапсуляція
# Наслідування
# Поліморфізм

# Абстракція


