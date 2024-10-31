# Home 1

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
    def __add__(self, number):
        return Circle(self.radius + number)

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"
        # return self.radius


c1 = Circle(5)
c2 = Circle(3)

print(c1 == c2)
c1 += 8
print(c1)

''' типи ООП - качинотипізація '''
from turtledemo.clock import datum

''' Приклад качиної типізації'''

# class Duck:
#     def eat(self):
#         return 'Duck eat'
#
# class Dog:
#     def eat(self):
#         return 'Dog eat'
#
# class Cat(Duck):
#     def eat(self):
#         return 'Cat eat'
#
# def food_injektor(animal):
#     print(animal.eat())
#
#
# donald = Duck()
# guffie = Dog()
# kitty = Cat()
#
# food_injektor(donald)
# food_injektor(guffie)
# food_injektor(kitty)

# CRUD

# Приклад перевантаження методів

# class Animal:
#     def eat(self):
#         return 'Animal eat'
#
# class Duck(Animal):
#         def eat(self):
#             return 'Duck eat'
#
# class Dog(Animal):
#         def eat(self):
#             return 'Dog eat'
#
# class Cat(Animal):
#         def eat(self):
#             return 'Cat eat'
#
# def food_injektor(animal):
#     print(animal.eat())
#
#
# donald = Duck()
# guffie = Dog()
# kitty = Cat()
#
# food_injektor(donald)
# food_injektor(guffie)
# food_injektor(kitty)

# Приклад МРО

# class Animal:
#     def eat(self):
#         return 'Animal eat'
#
#     def show_a(self):
#         return 'a'
#
# class Bear(Animal):
#     def eat(self):
#         return 'Bear eat'
#     def show_b(self):
#         return 'b'
#
# class Cat(Animal):
#     def eat(self):
#         return 'Cat eat'
#     def show_c(self):
#         return 'c'
#
# class Duck(Bear, Cat):
#     def eat(self):
#         return 'Duck eat'
#     def show_d(self):
#         return 'd'
#
# class Elephant(Animal):
#     def eat(self):
#         return 'Elephant eat'
#     def show_e(self):
#         return 'e'
#
# class Fox(Cat):
#     def eat(self):
#         return 'Fox eat'
#
# class Owl(Duck, Elephant, Fox):
#     def eat(self):
#         return 'Owl eat'
#
#
# def food_injektor(animal):
#     print(animal.eat())
#
#
# donald = Duck()
# kitty = Cat()
#
# food_injektor(donald)
# food_injektor(kitty)

# @staticmethod

# class Pen:                              # Class клас (креслення, рецепт)
#     model = 'Ballpen'                   # Поля класу
#     producer = 'BIC'
#
#     @staticmethod
#     def pen_strong(lenght, strength):
#         if lenght > strength:
#             return 'Broken'
#         else:
#             return 'Passed'
#
#     def __init__(self, color, width):   # метод ініціалізації\магічний метод\метод об'єкта класу
#         self.color = color
#         self.width = width
#         # self.color                    # поле обєкта класу
#
#     def draw(self):                     # метод обєкта класу
#         return (f'{self.color} line')
#
# parker = Pen('Black', 2)
# print(parker.draw())
#
# print(parker.pen_strong(2, 3))
# print(Pen.pen_strong(2, 3))
#
# '''
# Приймає cls як перший аргумент і може працювати з атрибутами класу.
# '''
#
# class Pen:                              # Class клас (креслення, рецепт)
#     model = 'Ballpen'                   # Поля класу
#     producer = 'BIC'
#
#     @staticmethod
#     def change_model(cls, model):
#         cls.model = model
#
#     def __init__(self, color, width):   # метод ініціалізації\магічний метод\метод об'єкта класу
#         self.color = color
#         self.width = width
#         # self.color                    # поле обєкта класу
#
#     def draw(self):                     # метод обєкта класу
#         return (f'{self.color} line')
#
# parker = Pen('Black', 2)
# print(parker.draw())
# print(parker.model)
# Pen.change_model('Fountainpen')
# abc = Pen('Black', 2)
# print(abc.draw())
# print(abc.model())
#
# print(parker.model)

# class Pen1:  # Class клас (креслення, рецепт)
#     model = 'ballpen'  # Поле класу
#     producer = 'BIC'  # Поле класу
#
#     @classmethod
#     def change_model(cls, model):
#         cls.model = model
#
#     def __init__(self, color, width):  # метод ініціалізації \ магічний метод \ метод обʼекту класу
#         self.color = color
#         self.width = width
#         self.model = Pen1.model
#         # self.color                   # поле обʼекту класу
#
#     def draw(self):                     # метод обʼекту класу
#         return (f'{self.color} line')
#
# parker = Pen1('blue', 2)
# print(parker.draw())
# print(parker.model)
# Pen1.change_model('Fountain pen')
# abc = Pen1('blue', 2)
# print(abc.draw())
# print(abc.model)
#
# print(parker.model)