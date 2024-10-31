'''Завдання 1: Дескриптор для кешування результату методу
Створіть дескриптор, який кешує результат виклику методу класу.
Кеш має бути валідним тільки під час одного запуску інстанції класу
і має очищатися при кожному новому створенні інстанції класу.'''

class Adder:
    def __init__(self, value):
        self.value = value

    def __get__(self, owner, instance):
        return f'Green'

    def __set__(self, owner, value):
        self.value = value

class Some:
    sad = Adder('Hello')
    def __init__(self, value):
        self.value = value
        self.add = Adder(self.value)

    def __str__(self):
        return str(self.value)

    def show(self):
        print(self.add)

a = Some('Hello')
print(a)
print(a.sad)
# a.sad = 'World'
# print(a.sad)

# class CacheInfo:
#     def __init__(self, cache):
#         self.cache = cache
#         self.cache_func = f"{cache.__name__}_cache_func"
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if not hasattr(instance, self.cache_func):
#             result = self.cache(instance)
#             setattr(instance, self.cache_func, result)
#         return getattr(instance, self.cache_func)
#
#     def __set__(self, instance, value):
#         raise AttributeError("Cannot set attribute")
#
#     def __delete__(self, instance):
#         if hasattr(instance, self.cache_func):
#             delattr(instance, self.cache_func)
#
# class Cache:
#     def __init__(self,value):
#         self.value = value
#
#     @CacheInfo
#     def __cache__(self):
#         print('Number of rooms:', self.value)
#         return self.value
#
# apartment1 = Cache(4)
# print(apartment1.__cache__)
#
# apartment2 = Cache(5)
# print(apartment2.__cache__)
#
# print(apartment1.__cache__)

'''
Living room
Kitchen
Hall
Bedroom
Children's room
Bathroom
Toilet'''

# class MyDescriptor:
#     def __get__(self, instance, owner):
#         return 'Living room, Kitchen, Hall, Bedroom, Children\'s room, Bathroom, Toilet'
#
#     def __set__(self, instance, value):
#         pass
#
#     def __delete__(self, instance):
#         return 'Clearing cache'
#
# class Room(MyDescriptor):
#     def __init__(self, room_name = str, length = float, width = float):
#         self.room_name = ''
#         self.length = length
#         self.width = width
#
#
#     # метод обчислення площі кімнати
#     def calculate_area(self):
#         return f'Площа кімнати {self.room_name}: {self.length * self.width} м2'
#
#
#     # метод обчислення площі всіх кімнат
#     def calculate_total_area(self):
#         return f'Площа всіх кімнат: {self.length * self.width} м2'
#
#     def __str__(self):
#         return self.room_name
#
# living_room = Room('Коридор',  12, 2)
# # print(living_room.calculate_area())
# # print(living_room.calculate_total_area())
# Room.calculate_total_area(living_room)
# kitchen = Room('Кухня', 5,5)
# hall = Room('Зал', 5, 6)
# bedroom = Room('Спальня', 4, 4)
# children_room = Room('Дитяча кімната', 3, 3)
# bathroom = Room('Ванна', 2, 2)
# toilet = Room('Туалет', 2, 1.5)

'''Завдання 2: Дескриптор з перевіркою типу
Розробіть дескриптор, який перевіряє, що значення, яке встановлюється для атрибуту, 
належить до певного типу (наприклад, int, float, str). 
Якщо значення не відповідає вказаному типу, дескриптор має викликати виняток TypeError.'''



'''Завдання 3: Read-only дескриптор
Створіть дескриптор, який дозволяє зробити атрибут класу тільки для читання. 
Якщо намагатися змінити значення атрибуту після його першого встановлення, 
має виникнути виняток AttributeError.'''