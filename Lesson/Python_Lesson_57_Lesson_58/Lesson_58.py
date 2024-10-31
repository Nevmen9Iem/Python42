# Декоратори в рамках ООП
import time


def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Calling: {func.__name__}({args}, {kwargs}) Result: {result}")
        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Calling: {func.__name__}({args}, {kwargs}\n Time: {end_time - start_time}")
        return result

    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        f = open('results.txt', 'at')
        f.write(f"Calling: {func.__name__}({args}, {kwargs}\n Time: {end_time - start_time}\n\n")
        f.close()
        return result

    return wrapper


class Calculator:
    @debug
    def add(self, x, y):
        return x + y

    @timer
    def square(self, x):
        return x * x

    @logger
    def simple(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


calc = Calculator()
print(calc.add(2, 3))
print(calc.square(42))
print(calc.square(41))
print(calc.simple(115249))


def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        upper_result = result.upper()
        print(upper_result)
        return upper_result

    return wrapper


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @uppercase
    def display_name(self):
        return f'{self.name} {self.surname}'


sten = Human('Sten', 'Kubrik')
print(sten.display_name())


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def display_name(self):
        return f'{self.name} {self.surname}'

    @property
    def display_name_uppercase(self):
        return self.display_name().upper()


human = Human('John', 'Doe')
print(human.display_name_uppercase)


# Керовані атрибути та властивості

class Attraction:
    human_list = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Attraction.human_list[self.name] = self.age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, user_age):
        if user_age < 18:
            self.__age = 0
        else:
            self.__age = user_age


a1 = Attraction('John', 19)
a2 = Attraction('Sten', 17)
a3 = Attraction('Den', 18)
print(Attraction.human_list)

'''Напишіть клас Person, у якому властивість full_name повертає та приймає 
повне ім'я, але зберігає окремо ім'я та прізвище.'''


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @full_name.setter
    def full_name(self, name):
        self.name, self.surname = name.split()

p1 = Person('Andrii', 'Builuk')
print(p1.full_name)
p1.full_name = 'Sten 123'
print(p1.full_name)
print(p1.name)
print(p1.surname)
