'''Завдання 1
До вже реалізованого класу «Дріб» додайте статичний метод,
який при виклику повертає кількість створених об’єктів
класу «Дріб».'''

# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         Fraction._increment_count()
#     _count = 0
#     @staticmethod
#     def _increment_count():
#         Fraction._count += 1
#     @staticmethod
#     def get_count():
#         return Fraction._count
#     def __str__(self):
#         return f"{self.numerator}/{self.denominator}"
#
#
# frac1 = Fraction(1, 2)
# frac2 = Fraction(3, 4)
#
# print(f'Кількість створених об’єктів: {Fraction.get_count()}')
#
# frac3 = Fraction(5, 6)
#
# print(f'Кількість створених об’єктів: {Fraction.get_count()}')


'''Завдання 2
Створіть клас для конвертування температури з Цельсія
у Фаренгейт, і навпаки. У класі має знаходитися два статичні
методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати
кількість підрахунків температури та повернути це значення
статичним методом.'''

# class Temperature:
#     _count = 0
#     @staticmethod
#     def _increment_count():
#         Temperature._count += 1
#     @staticmethod
#     def get_count():
#         return f"Кількість конвертацій: {Temperature._count}"
#     @staticmethod
#     def convert_celsius_to_fahrenheit(celsius):
#         Temperature._increment_count()
#         return round(celsius * 9 / 5 + 32, 2)
#     @staticmethod
#     def convert_fahrenheit_to_celsius(fahrenheit):
#         Temperature._increment_count()
#         return round((fahrenheit - 32) * 5 / 9, 2)
#
#
# temp_celsius = Temperature.convert_fahrenheit_to_celsius(10)
# print(temp_celsius)
# temp_fahrenheit = Temperature.convert_celsius_to_fahrenheit(20)
# print(temp_fahrenheit)
# print(Temperature.get_count())


'''Завдання 3
Створіть клас для конвертування з метричної системи в
англійську, та навпаки. Реалізуйте функціональність у вигляді
статичних методів. Обов’язково реалізуйте конвертування
заходів довжини.'''

# class Length:
#     _count = 0
#     @staticmethod
#     def _increment_count():
#         Length._count += 1
#     @staticmethod
#     def get_count():
#         return f"Кількість конвертацій: {Length._count}"
#     @staticmethod
#     def convert_meters_to_feet(meters):
#         Length._increment_count()
#         return f"Футів {round(meters * 3.281, 2)}"
#     @staticmethod
#     def convert_feet_to_meters(feet):
#         Length._increment_count()
#         return f"Метрів {round(feet / 3.281, 2)}"
#
#
# len1 = Length.convert_feet_to_meters(10)
# len2 = Length.convert_meters_to_feet(20)
# print(len1)
# print(len2)
# print(Length.get_count())