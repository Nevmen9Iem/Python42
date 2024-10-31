# Декоратор в рамках ООП
import time


# def debug(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'Calling {func.__name__}({args}, {kwargs}) Result: {result}')
#         return result
#     return wrapper
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f'Calling {func.__name__}({args}, {kwargs}\n Time: {end_time - start_time} seconds')
#         return result
#     return wrapper
#
# class Calculator:
#     @debug
#     def add(self, x, y):
#         return x + y
#
#     @timer
#     def multiply(self, x):
#         return x * x
#
#     def simple(selfself, n):
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
#
# calc = Calculator()
# print(calc.add(2, 3))
# print(calc.multiply(42))
# print(calc.simple(1152499))


# Декоратори в рамках ООП
# import time
#
#
# def debug(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Calling: {func.__name__}({args}, {kwargs}) Result: {result}")
#         return result
#
#     return wrapper
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Calling: {func.__name__}({args}, {kwargs}\n Time: {end_time - start_time}")
#         return result
#
#     return wrapper
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         f = open('results.txt', 'at')
#         f.write(f"Calling: {func.__name__}({args}, {kwargs}\n Time: {end_time - start_time}\n\n")
#         f.close()
#         return result
#     return wrapper
#
#
# class Calculator:
#     @debug
#     def add(self, x, y):
#         return x + y
#
#     @timer
#     def square(self, x):
#         return x * x
#
#     @logger
#     def simple(self, n):
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
#
# calc = Calculator()
# print(calc.add(2, 3))
# print(calc.square(42))
# print(calc.square(41))
# print(calc.simple(115249))


'''Завдання 4
Напишіть декоратор uppercase, 
який перетворює результат методу в рядок у верхньому регістрі.
'''

# class Human:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def display_name(self):
#         return f'{self.name} {self.surname}'
#
#     @property
#     def display_name_uppercase(self):
#         return self.display_name().upper()
#
# human = Human('John', 'Doe')
# print(human.display_name_uppercase)
#
# '''ver2'''
# def uppercase(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
# class Human:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def display_name(self):
#         return f'{self.name} {self.surname}'
#
#     @uppercase
#     def display_name_uppercase(self):
#         return self.display_name()
#
# human = Human('John', 'Doe')
# print(human.display_name_uppercase())
#
# '''ver3'''
# def uppercase(func):
#     def wrapper(*args, **kwargs):
#         # Викликаємо оригінальну функцію і отримуємо результат
#         result = func(*args, **kwargs)
#         # Перетворюємо результат у верхній регістр
#         return result.upper() if isinstance(result, str) else result
#     return wrapper
# # Приклад використання декоратора
# class Greeting:
#     @uppercase
#     def say_hello(self, name):
#         return f"Hello, {name}!"
# # Тестування
# greeting = Greeting()
# print(greeting.say_hello("Олег"))  # Виведе: HELLO, ОЛЕГ!

# Керовані атрибути та властивості

# class Attraction:
#     human_list = {}
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Attraction.human_list[self.name] = self.age # Додати властивість до списку
#     ''' Метод для отримання властивості '''
#     @property # декоратор для властивості
#     def age(self):
#         return self.__age
#     ''' Метод для встановлення властивості '''
#     @age.setter # декоратор для властивості
#     def age(self, user_age):
#         ''' При встановленні властивості перевіряємо вік користувача '''
#         if user_age < 18:
#             self.__age = 0
#         else:
#             self.__age = user_age
#
#
# a1 = Attraction('John', 19)
# a2 = Attraction('Jane', 17)
# a3 = Attraction('Jack', 18)
# print(Attraction.human_list)

'''5
Напишіть клас Person, у якому властивість full_name повертає та 
приймає повне ім'я, але зберігає окремо ім'я та прізвище.
'''

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name


person = Person('John', 'Doe')
print(person.full_name)
print(person.first_name)
print(person.last_name)