# Поліморфізм

# class Grinder:
#
#     def start(self, products):
#         self.products = products
#         if self.products == 'meat':
#             return 'mince'
#         elif self.products == 'branch':
#             return 'sawdust'
#         else:
#             return f'grinded {self.products}'
#
#     @property # геттер
#     def products(self):
#         return self.__id
#
#     @id.setter # сеттер
#     def id(self, id):
#         if Grinder.name == 'default':
#             self.__id = id
#         else:
#             self.__id = 1
#
#     @id.deleter # декларатор
#     def id(self):
#         del self.__id
#
# some_grinder = Grinder()
# print(some_grinder.start('coffe'))
# print(some_grinder.start('meat'))
# print(some_grinder.start('branch'))

# class Grinder:
#     __id = 0
#     name = 'default'
#
#     def start(self, products):  # поліморфний метод
#         self.products = products
#         if self.products == 'meat':
#             return 'mince'
#         elif self.products == 'branch':
#             return 'sawdust'
#         else:
#             return f'grinded {self.products}'
#
#     @property
#     def id(self):
#         return self.__id
#
#     @id.setter
#     def id(self, id):
#         if Grinder.name == 'default':
#             self.__id = id
#         else:
#             self.__id = 1
#
#     @id.deleter
#     def id(self):
#         return self.__id
#
#
# some_grinder = Grinder()
# print(some_grinder.start('coffee'))
# print(some_grinder.start('meat'))
# print(some_grinder.start('branch'))
# print(some_grinder.id)
# some_grinder.id = 3
# print(some_grinder.id)


# class Mobile:
#     __imei = '123'
#     color = 'grey'
#     os = 'Android'
#     model = 'Pixel'
#     name = 'default'
#
#     @property
#     def imei(self):
#         return self.__imei
#
#     @imei.setter
#     def imei(self, imei):
#         if Mobile.name == 'default':
#             self.__imei = imei
#         else:
#             self.__imei = 1
#
#     @imei.deleter
#     def imei(self):
#         return self.__imei
#
# some_mobile = Mobile()
# print(some_mobile.imei)
# some_mobile.imei = "234"
# print(some_mobile.imei)

# class Table: # базовий класс
#     count = 0 # атрибут класу
#
#     def __init__(self, name): # Магічний метод
#         Table.count += 1
#         self.name = name # поле обʼєкту класу
#
#     def __str__(self):
#         return self.name
#
#     def change_name(self, name):
#         self.name = name
#
# wood = Table('wood')
# print(wood.name)
# print(wood.count)
# stone = Table('redwood')
# print(stone.name)
# print(stone.count)
# print(wood)
# print(stone)

# import tkinter
# print(tkinter)

# class OrwellMath:
#     def __init__(self, number):
#         self.number = number
#
#     def __str__(self):
#         return self.number
#
#     def add(self, other):
#         return self.number + other.number + 1
#
#     def __eq__(self, other):
#         if self.number == other.number:
#             return 'Hello'
#         else:
#             return 'Not'
#
# print(int(2) + int(2))
# print(OrwellMath(2) + OrwellMath(2))
#
# print(int(2) == int(2))
# print(OrwellMath(2) == OrwellMath(2))

# Створіть (або використовуйте раніше створений) клас
# «Число». Клас «Число» зберігає всередині одне значення.
# Використовуючи перевантаження операторів, реалізуйте для нього арифметичні операції для роботи з числом
# (операції +, -, *, /).

class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        if hasattr(other, 'value'):
            return self.value + other.value
        else:
            return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

print(Number(3) + Number(2))
print(Number(3) - Number(2))
print(Number(3) * Number(2))
print(Number(3) / Number(2))