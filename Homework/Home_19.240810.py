# class Device:
#     def __init__(self, brand, model, power, year):
#         self.brand = brand
#         self.model = model
#         self.power = power  # Споживана потужність в ватах
#         self.year = year
#
#     def get_info(self):
#         return (f"Brand: {self.brand}, Model: {self.model}, "
#                 f"Power: {self.power}W, Year: {self.year}")
#
#
# class CoffeeMachine(Device):
#     def __init__(self, brand, model, power, year, capacity, has_milk_frother):
#         super().__init__(brand, model, power, year)
#         self.capacity = capacity  # Обсяг в літрах
#         self.has_milk_frother = has_milk_frother  # Чи є молочний струйник
#
#     def brew_coffee(self):
#         return f"Brewed coffee from {self.brand} {self.model}. Capacity: {self.capacity}L"
#
#     def get_info(self):
#         base_info = super().get_info()
#         milk_frother_info = "With milk frother" if self.has_milk_frother else "Without milk frother"
#         return f"{base_info}, Capacity: {self.capacity}L, {milk_frother_info}"
#
#
# class Blender(Device):
#     def __init__(self, brand, model, power, year, jar_capacity):
#         super().__init__(brand, model, power, year)
#         self.jar_capacity = jar_capacity  # Об'єм чаші в літрах
#
#     def blend(self):
#         return f"Blending ingredients in {self.brand} {self.model}. Jar capacity: {self.jar_capacity}L"
#
#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info}, Jar capacity: {self.jar_capacity}L"
#
#
# class MeatGrinder(Device):
#     def __init__(self, brand, model, power, year, is_electric):
#         super().__init__(brand, model, power, year)
#         self.is_electric = is_electric  # Чи електрична м’ясорубка
#
#     def grind_meat(self):
#         return f"Grinding meat with {self.brand} {self.model}. Is electric: {self.is_electric}"
#
#     def get_info(self):
#         base_info = super().get_info()
#         electric_info = "Electric" if self.is_electric else "Manual"
#         return f"{base_info}, Type: {electric_info}"
#
#
# # Приклад використання
# coffee_machine = CoffeeMachine("BrandA", "CM2023", 1500, 2023, 1.5, True)
# blender = Blender("BrandB", "BL2023", 800, 2023, 2.0)
# meat_grinder = MeatGrinder("BrandC", "MG2023", 1200, 2023, True)
# print(coffee_machine.get_info())
# print(coffee_machine.brew_coffee())
# print(blender.get_info())
# print(blender.blend())
# print(meat_grinder.get_info())
# print(meat_grinder.grind_meat())

# 2. Завдання

# class Ship:
#     def __init__(self, name, length, water_tonnage, year_built, max_speed):
#         self.name = name  # Назва корабля
#         self.length = length  # Довжина в метрах
#         self.water_tonnage = water_tonnage  # Водний тоннаж
#         self.year_built = year_built  # Рік побудови
#         self.max_speed = max_speed  # Максимальна швидкість в вузлах
#
#     def get_info(self):
#         return (f"Ship Name: {self.name}, Length: {self.length}m, "
#                 f"Width: {self.water_tonnage}m, Year Built: {self.year_built}, "
#                 f"Max Speed: {self.max_speed} knots")
#
#
# class Frigate(Ship):
#     def __init__(self, name, length, water_tonnage, year_built, max_speed, armament):
#         super().__init__(name, length, water_tonnage, year_built, max_speed)
#         self.armament = armament  # Озброєння
#
#     def engage_enemy(self):
#         return f"{self.name} is engaging the enemy with its armament: {self.armament}"
#
#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info}, Armament: {self.armament}"
#
#
# class Destroyer(Ship):
#     def __init__(self, name, length, water_tonnage, year_built, max_speed, radar_system):
#         super().__init__(name, length, water_tonnage, year_built, max_speed)
#         self.radar_system = radar_system  # Радіолокаційна система
#
#     def launch_missiles(self):
#         return f"{self.name} is launching missiles!"
#
#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info}, Radar System: {self.radar_system}"
#
#
# class Cruiser(Ship):
#     def __init__(self, name, length, water_tonnage, year_built, max_speed, crew_size):
#         super().__init__(name, length, water_tonnage, year_built, max_speed)
#         self.crew_size = crew_size  # Кількість членів екіпажу
#
#     def conduct_operation(self):
#         return f"{self.name} is conducting naval operations with {self.crew_size} crew members."
#
#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info}, Crew Size: {self.crew_size}"
#
#
# # Приклад використання
# frigate = Frigate("HMS Victory", 69.0, 23.0, 1765, 15, "Cannons and Missiles")
# destroyer = Destroyer("USS Arleigh Burke", 154.0, 20.0, 1991, 30, "SPY-1 Radar")
# cruiser = Cruiser("USS Cowpens", 170.0, 20.0, 1991, 32, 500)
# print(frigate.get_info())
# print(frigate.engage_enemy())
# print(destroyer.get_info())
# print(destroyer.launch_missiles())
# print(cruiser.get_info())
# print(cruiser.conduct_operation())


# 3. Завдання


class Money:
    def __init__(self, dollars=0, cents=0):
        self.dollars = dollars
        self.cents = cents
        self._normalize()  # Нормалізуємо суму
    def _normalize(self):
        """ Нормалізує значення грошей, щоб cents були менше 100. """
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100
        elif self.cents < 0:
            # Якщо копійки менше нуля, зменшуємо долари.
            borrow_dollars = (-self.cents + 99) // 100
            self.dollars -= borrow_dollars
            self.cents = (self.cents + 100 * borrow_dollars) % 100
    def display(self):
        """ Виводить суму грошей на екран. """
        return f"${self.dollars}.{self.cents:02d}"
    def set_amount(self, dollars, cents):
        """ Задає значення частини грошей. """
        self.dollars = dollars
        self.cents = cents
        self._normalize()
    def add(self, other):
        """ Додає інший об'єкт Money. """
        self.dollars += other.dollars
        self.cents += other.cents
        self._normalize()

class Product:
    def __init__(self, name, price: Money):
        self.name = name      # Назва продукту
        self.price = price    # Ціна продукту (об'єкт Money)
    def display(self):
        """ Виводить інформацію про продукт. """
        return f"Product: {self.name}, Price: {self.price.display()}"
    def discount(self, amount: Money):
        """ Зменшує ціну на задану суму. """
        if self.price.dollars == 0 and self.price.cents == 0:
            print("Cannot apply discount to a product with a price of $0.00.")
            return
        self.price.add(Money(-amount.dollars, -amount.cents))
        if self.price.dollars < 0 or (self.price.dollars == 0 and self.price.cents < 0):
            print(f"Discount exceeds price. Price after discount: {self.price.display()}")
            self.price.set_amount(0, 0)  # Якщо знижка перевищує ціну, ставимо ціну 0

# Приклад використання
# Створюємо об'єкти Money
price1 = Money(10, 50)  # $10.50
price2 = Money(3, 25)    # $3.25
# Створюємо продукт
product = Product("Coffee", price1)
print(product.display())  # Виводимо інформацію про продукт
# Зменшуємо ціну продукту
product.discount(price2)
print(product.display())  # Виводимо нову інформацію про продукт після знижки
# Застосовуємо занадто велику знижку
product.discount(Money(8, 0))  # Знижка $8.00
print(product.display())  # Перевіряємо фінальну ціну
