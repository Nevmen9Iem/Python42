# # Створення та керування поведінкою екземплярів класу.
#
# # Функтори
#
# class Event:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#         self.attendees = []
#
#     def add_attendee(self, person):
#         self.attendees.append(person)
#
#     def __repr__(self):
#         return f'Event {self}'
#
#     def __str__(self):
#         return f'{self.name} at {self.location} with {len(self.attendees)} attendees'
#
#
# event = Event('Python Workshop', 'Odesa')
# event.add_attendee('John Doe')
# event.add_attendee('Jane Doe')
# print(event)
#
# afterparty = Event('After Party', 'Odesa')
# afterparty.add_attendee('John Doe')
# afterparty.add_attendee('Jane Doe')
#
# print(event)
# print(afterparty)
#
# class Person:
#     some_list = ['123']
#
#     def add_something(self, something):
#         self.some_list.append(something)
#
#
# john = Person()
# john.add_something('456')
# print(john.some_list)

'''Завдання 1
Створіть клас Course, який інкапсулює інформацію про назву курсу,
список студентів та оцінки.
Додайте метод для виведення середньої оцінки по курсу.'''

'''ver1'''
# class Course:
#     def __init__(self, name, students, grades):
#         self.name = name
#         self.students = students
#         self.grades = grades
#         self.average = sum(grades) / len(grades)
#
#     def __repr__(self):
#         return f'Course {self.name} with {len(self.students)} students'
#
#     def __str__(self):
#         return f'{self.name} with {len(self.students)} students and average {self.average}'
#
# course = Course('Python', ['John', 'Jane'], [5, 4])
# print(course)

'''ver2'''
# class Course:
#     def __init__(self, name):
#         self.name = name

'''Завдання 2'''

# import time
#
#
# class Timer:
#     def __init__(self):
#         self.start_time = None
#         self.end_time = None
#
#     def start(self):
#         self.start_time = time.time()
#
#     def stop(self):
#         self.end_time = time.time()
#         return self.end_time - self.start_time
#
#     def result(self):
#         return self.end_time - self.start_time
#
#     def __str__(self):
#         result = self.end_time - self.start_time
#         return f'{result}'
#
# t1 = Timer()
# t1.start()
# time.sleep(2)
# t1.stop()
# print(t1)

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        self.memory = 1

    def __call__(self, x):
        self.memory = self.memory + (x * self.factor)
        return x * self.factor

    def __str__(self):
        return f'Just string with memory {self.memory}'

duble = Multiplier(2)
print(duble)
'''3'''

'''Створіть функтор Adder, який приймає стартове число і 
додає до нього передане значення.'''

class Adder:
    def __init__(self, start):
        self.start = start

    def __call__(self, value):
        return self.start + value


adder = Adder(10)
print(adder(5))