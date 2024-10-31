# Створення та керування поведінкою екземплярів класу.


class Event:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.attendees = []

    def add_attendee(self, person):
        self.attendees.append(person)

    def __repr__(self):
        return f'Event ({self.name}, {self.location})'

    def __str__(self):
        return f'{self.name} at {self.location} with {len(self.attendees)} attendees'


event = Event('Python Workshop', 'Odesa')
event.add_attendee('John Doe')
event.add_attendee('Jane Doe')
print(event)

afterparty = Event('After Party', 'Odesa')
afterparty.add_attendee('Andrii Builuk')
afterparty.add_attendee('Sten Kubrik')
afterparty.add_attendee('Robert Downy')

print(event)
print(afterparty)


class Person:
    some_list = ['123']

    def add_something(self, something):
        self.some_list.append(something)


john = Person()
sten = Person()
print(john.some_list)
john.add_something('456')
print(john.some_list)
print(sten.some_list)

l = [1, 2, 3]
d = l
print(l)
print(d)
l.append(4)
print(l)
print(d)

l = [1, 2, 3]
d = l[:]
print(l)
print(d)
l.append(4)
print(l)
print(d)

l = [1, 2, 3]
d = l.copy()
print(l)
print(d)
l.append(4)
print(l)
print(d)

'''Завдання 1
Створіть клас Course, який інкапсулює інформацію про назву курсу, список студентів та оцінки. 
Додайте метод для виведення середньої оцінки по курсу.'''


class Course:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_grade(self, name, grade):
        self.students[name] = grade

    def average_grade(self):
        total = sum(self.students.values())
        return total / len(self.students)


course = Course("Python Programming")
course.add_grade("Sten Kubrik", 80)
course.add_grade("John Doe", 95)
print(course.average_grade())


class Course:
    _namecourse = ["Programs", "PCcourse", "C++"]
    _students = ["student1", "student2", "student3"]
    _results = [10, 11, 12]

    def res(self):
        return f"{(self._results[0] + self._results[1] + self._results[2]) / len(self._results)}"


c = Course()
print(c.res())

'''Напишіть клас Timer, який використовується для вимірювання часу виконання коду, 
з методами start() та stop(), і який повертає час в секундах, що пройшов.'''
import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        return self.end_time - self.start_time

    def result(self):
        return self.end_time - self.start_time

    def __str__(self):
        result = self.end_time - self.start_time
        return f'{result}'


# t1 = Timer()
# print(t1.start())
# time.sleep(2)
# print(t1.stop())
# # time.sleep(5)
# # print(t1.result())
#
# print(t1)


# Функтори

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        self.memory = 1

    def __call__(self, x):
        self.memory = self.memory + (x * self.factor)
        return x * self.factor

    def __str__(self):
        return f'Just string with memory {self.memory}'

double = Multiplier(2)
print(double)
print(double(5))
print(double(3))
print(double)
