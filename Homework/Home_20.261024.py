'''Завдання 1
Створіть функцію, яка повертає список з усіма простими числами від 0 до 1000.
Використовуючи механізм декораторів, підрахуйте, скільки секунд знадобилося для обчислення усіх простих чисел.
Виведіть на екран кількість секунд та прості числа.'''

import time
from select import select

# def time_decorator(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f'Виконано за {round(end_time - start_time, 4)} секунд')
#     return wrapper
#
#
# @time_decorator
# def prime_numbers():
#     primes = []
#     for num in range(0, 1000):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime and num > 2:
#             primes.append(num)
#     print(primes)
#     return primes
#
# prime_numbers()

'''Завдання 2
Додайте до першого завдання можливість передавати
межі діапазону для пошуку усіх простих чисел.'''

# import time
#
#
# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f'Виконано за {round(end_time - start_time, 2)} секунд')
#         return result
#
#     return wrapper
#
#
# def add_range(func):
#     def inner():
#         num1 = int(input('Введіть число початку діапазону: '))
#         num2 = int(input('Введіть число кінця діапазону: '))
#         return func(num1, num2)
#
#     return inner
#
#
# @add_range
# @time_decorator
# def prime_numbers(num1, num2):
#     primes = []
#     for num in range(num1, num2 + 1):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime and num > 2:
#             primes.append(num)
#     print(primes)
#     return primes
#
#
# prime_numbers()

'''Завдання 3
Щороку ваша компанія надає різним державним установам
фінансову звітність. Залежно від установи, формати звітності
різні. Використовуючи механізм декораторів вирішіть питання
звітності для установ.'''

def generate_report(data):
    return data
def format_a(func):
    def wrapper(data):
        report = func(data)
        return f"Формат А: {report}"
    return wrapper
def format_b(func):
    def wrapper(data):
        report = func(data)
        return f"Формат Б: {report}"
    return wrapper
def format_c(func):
    def wrapper(data):
        report = func(data)
        return f"Формат В: {report}"
    return wrapper
@format_a
def report_a(data):
    return generate_report(data)
@format_b
def report_b(data):
    return generate_report(data)
@format_c
def report_c(data, ):
    return generate_report(data)
report_data = {"year": 2023, "debits": 1000000, "credits": 800000}
print(report_a(report_data))
print(report_b(report_data))
print(report_c(report_data))
