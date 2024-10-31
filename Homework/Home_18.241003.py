# Завдання 1

# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте
# - клас CoffeeMachine (містить інформацію про кавомашину),
# - клас Blender (містить інформацію про блендер),
# - клас MeatGrinder (містить інформацію про м’ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

# class Device:
#     def __init__(self, brand, model, year, price):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.price = price
#
#
#     def get_info(self):
#         return f"Виробник: {self.brand}\nСерія: {self.model}\nРік: {self.year}\nЦіна: {self.price}"
#
# class CoffeeMachine(Device):
#     def __init__(self, brand, model, year, price, guarantee, capacity): # Інформація про кавомашину
#         super().__init__(brand, model, year, price)
#         self.guarantee = guarantee # Гарантія
#         self.capacity = capacity # Обсяг в літрах
#
#     def brew_coffee(self):
#         return f"Зварена кава з {self.brand} {self.model}. Літри: {self.capacity}L"
#
#
# class Blender(Device):
#     def __init__(self, brand, model, year, price, power): # Інформація про блендер
#         super().__init__(brand, model, year, price)
#         self.power = power # Споживана потужність в ватах
#
#     def blend(self):
#         return f"Змішування інгредієнтів {self.brand} {self.model}. Потужність: {self.power}kW"
#
# class MeatGrinder(Device):
#     def __init__(self, brand, model, year, price, number_of_knives, size):
#         super().__init__(brand, model, year, price)
#         self.number_of_knives = number_of_knives
#         self.size = size
#
#     def grind_meat(self):
#         return f"Подрібнення м'яса в {self.brand} {self.model}. Кількість ножів: {self.number_of_knives}, Розмір: {self.size}"
#
#
# coffee_machine = CoffeeMachine("SuperCoffe", "XC1000", 2020, 15000, 3, 2)
# blender = Blender("Bosch", "XC2000", 2021, 5000, 1.5)
# meat_grinder = MeatGrinder("ProGrinder", "MG2000", 2023, 12000, 2, 'XXL')
# print(coffee_machine.brew_coffee())
# print(coffee_machine.get_info())
# print(blender.get_info())
# print(blender.blend())
# print(meat_grinder.get_info())
# print(meat_grinder.grind_meat())

# Завдання 2

# Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте
# - клас Frigate (містить інформацію про фрегат),
# - клас Destroyer (містить інформацію про есмінець),
# - клас Cruiser (містить інформацію про крейсер).
# Кожен із класів має містити необхідні для роботи методи.


# class Ship:
#     def __init__(self, name, length, water_tonnage, year_built, max_speed):
#         self.name = name  # Назва
#         self.length = length  # Довжина
#         self.water_tonnage = water_tonnage  # Водний тоннаж
#         self.year_built = year_built  # Рік випуску
#         self.max_speed = max_speed  # Максимальна швидкість
#
#     def get_info(self):
#         return f"Назва: {self.name}\nДовжина: {self.length}\nВодозміщення: {self.water_tonnage}\nРік виготовлення: {self.year_built}\nМаксимальна швидкість: {self.max_speed}"
#
#
# class Frigate(Ship):
#     def __init__(self, name, length, water_tonnage, year_built, max_speed, radius_of_action):
#         super().__init__(name, length, water_tonnage, year_built, max_speed)
#         self.radius_of_action = radius_of_action
#
#
# class Destroyer(Ship):
#     def __init__(self, name, length, water_tonnage, year_built, max_speed, radius_of_action):
#         super().__init__(name, length, water_tonnage, year_built, max_speed)
#         self.radius_of_action = radius_of_action
#
#
# class Cruiser(Ship):
#     def __init__(self, name, length, water_tonnage, year_built, max_speed, number_of_underwater_bombs):
#         super().__init__(name, length, water_tonnage, year_built, max_speed)
#         self.number_of_underwater_bombs = number_of_underwater_bombs
#
#
# frigate = Frigate("Гетьман Сагайдачний", 58, 80000, 2000, 65, 300)
# destroyer = Destroyer("Січь", 112, 120000, 1998, 45, 800)
# cruiser = Cruiser("Отаман", 170.0, 150000, 2005, 50, 400)
# print(frigate.get_info())
# print(destroyer.get_info())
# print(cruiser.get_info())

# Завдання 3

# Запрограмуйте клас Money (об’єкт класу оперує однією
# валютою) для роботи з грошима.
# У класі мають бути передбачені:
# - поле для зберігання цілої частини грошей (долари, євро, гривні тощо)
# - і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money.
# Реалізуйте метод для зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля


# class Money:
#     def __init__(self, dollars=0, cents=0): # долари, копійки
#         self.dollars = dollars
#         self.cents = cents
#         self._normalize()  # Нормалізуємо суму
#     def _normalize(self): # нормалізуємо суму
#         if self.cents >= 100: # якщо копійки більше 100
#             self.dollars += self.cents // 100 # долари додаємо до доларів
#             self.cents = self.cents % 100 # копійки додаємо до копійок
#         elif self.cents < 0: # Якщо копійки менше нуля, зменшуємо долари.
#             borrow_dollars = (-self.cents + 99) // 100 # знижуємо долари
#             self.dollars -= borrow_dollars # долари зменшуємо до доларів
#             self.cents = (self.cents + 100 * borrow_dollars) % 100 # копійки зменшуємо до копійок
#     def display(self): # виводимо суму на екран
#         return f"${self.dollars}.{self.cents}"
#     def set_amount(self, dollars, cents): # задаємо значення частини
#         self.dollars = dollars
#         self.cents = cents
#         self._normalize()
#     def add(self, other): # додаємо інший об'єкт Money
#         self.dollars += other.dollars
#         self.cents += other.cents
#         self._normalize()
#
# class Product:
#     def __init__(self, name, price: Money):
#         self.name = name
#         self.price = price
#     def display(self): # виводимо інформацію про продукт
#         return f"Продукт: {self.name}, Ціна: {self.price.display()}"
#     def discount(self, amount: Money): # Зменшує ціну на задану суму.
#         if self.price.dollars == 0 and self.price.cents == 0:
#             print("Неможливо застосувати знижку до товару з ціною $0.00.")
#             return
#         self.price.add(Money(-amount.dollars, -amount.cents))
#         if self.price.dollars < 0 or (self.price.dollars == 0 and self.price.cents < 0):
#             print(f"Знижка перевищує ціну. Ціна після знижки: {self.price.display()}")
#             self.price.set_amount(0, 0)  # Якщо знижка перевищує ціну, ставимо ціну 0
#
# # Приклад використання
# # Створюємо об'єкти Money
# price1 = Money(25, 50)  # $10.50
# price_discount = Money(4, 15)    # $3.25
# # Створюємо продукт
# product = Product("Помідор", price1)
# print(product.display())  # Виводимо інформацію про продукт
# # Зменшуємо ціну продукту
# product.discount(price_discount)
# print(product.display())  # Виводимо нову інформацію про продукт після знижки
# # Застосовуємо занадто велику знижку
# product.discount(Money(30, 0))  # Знижка $8.00
# print(product.display())  # Перевіряємо фінальну ціну