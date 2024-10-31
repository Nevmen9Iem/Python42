# Завдання 1

# Реалізуйте клас «Автомобіль». Збережіть у класі: назву
# моделі, рік випуску, виробника, об’єм двигуна, колір машини,
# ціну. Реалізуйте методи класу для введення-виведення даних
# та інших операцій.

# class Car:
#     def __init__(self, model, year, company, volume, color, price):
#         self.model = model
#         self.year = year
#         self.company = company
#         self.volume = volume
#         self.color = color
#         self.price = price
#
#     def __str__(self):
#         return f"Company: {self.company}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}\nVolume: {self.volume}\nPrice: {self.price}"
#
#
# def input_car():
#     print("Please enter car model, year, company, volume, color and price: ")
#     model = input("Enter model: ")
#     year = int(input("Enter year: "))
#     company = input("Enter company: ")
#     volume = float(input("Enter volume: "))
#     color = input("Enter color: ")
#     price = float(input("Enter price: "))
#     return Car(model, year, company, volume, color, price)
#
#
# car = input_car()
# print(car)

# Завдання 2

# Реалізуйте клас «Книга». Збережіть у класі: назву книги,
# рік видання, видавця, жанр, автора, ціну. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

# class Book:
#     def __init__(self, title, year, publisher, genre, author, price):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def __str__(self):
#         return f"Title: {self.title}\nYear: {self.year}\nPublisher: {self.publisher}\nGenre: {self.genre}\nAuthor: {self.author}\nPrice: {self.price}"
#
# def input_book():
# print("Please enter book title, year, publisher, genre, author and price: ")
#     title = input("Enter title: ")
#     year = int(input("Enter year: "))
#     publisher = input("Enter publisher: ")
#     genre = input("Enter genre: ")
#     author = input("Enter author: ")
#     price = float(input("Enter price: "))
#     return Book(title, year, publisher, genre, author, price)
#
#
# book = input_book()
# print(book)

# Завдання 3
# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

# class Stadium:
#     def __init__(self, name, date, country, city, capacity):
#         self.name = name
#         self.date = date
#         self.country = country
#         self.city = city
#         self.capacity = capacity
#
#     def __str__(self):
#         return f"Name: {self.name}\nDate: {self.date}\nCountry: {self.country}\nCity: {self.city}\nCapacity: {self.capacity}"
#
# def input_stadium():
#     print("Please enter stadium name, date, country, city and capacity: ")
#     name = input("Enter name: ")
#     date = input("Enter date: ")
#     country = input("Enter country: ")
#     city = input("Enter city: ")
#     capacity = int(input("Enter capacity: "))
#     return Stadium(name, date, country, city, capacity)
#
# stadium = input_stadium()
# print(stadium)