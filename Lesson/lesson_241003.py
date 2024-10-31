# Інкапсуляція

# public - доступна всередині класу (name)
# protected - доступна у відкритому доступі (_cover)
# private - доступна тільки у відкритому класі (__password)

# class Mobile:
#     imei = '123'
#     color = 'grey'
#     os = 'Android'
#     model = 'Pixel'
#     name = 'default'
#
#
#     def change_imei(self, new_imei):
#         self.imei = new_imei
#
#     def show_imei(self):
#         return self.imei
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#     def show_color(self):
#         return self.color
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     def show_name(self):
#         return self.name
#
# pixel7 = Mobile()
#
#
# print(pixel7.show_color())
# print(pixel7.show_imei())
# print(pixel7.show_name())
# pixel7.color = 'green'
# pixel7.imei = '456'
# pixel7.name = 'qwerty'
# print(pixel7.show_color())
# print(pixel7.show_imei())
# print(pixel7.show_name())


# class Mobile:
#     __imri = '123'
#     __password = 'qwerty'
#     _color = 'grey'
#     _cover = 'black'
#     os = 'Android'
#     model = 'Pixel'
#     name = 'default'
#
#     def change_imei(self, new_imei):
#         self.__imri = new_imei
#
#     def show_imei(self):
#         return self.__imri
#
#     def change_color(self, new_color):
#         self._color = new_color
#
#     def show_color(self):
#         return self._color
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     def show_name(self):
#         return self.name


# Написати 2 методи з методами доступу до них ( один приватний і один захищений)
# Написати 2 поля з методами доступу до них ( один приватний і один захищений)


# class Car:
#     __brand = 'Mercedes'
#     _model = 'Vito'
#
#     def change_brand(self, new_brand):
#         self.__brand = new_brand
#
#     def show_brand(self):
#         return self.__brand
#
#     def change_model(self, new_model):
#         self._model = new_model
#
#     def show_model(self):
#         return self._model
#
#
# car_showroom = Car()
# car_showroom.__brand = 'Ford'
# car_showroom._model = 'Transit'
#
# print(car_showroom.show_brand())
# print(car_showroom.show_model())


# Успадкування

# class Human:
#     name = 'John'
#     surbname = 'Doe'
#     age = 30
#
#     def eat(self):
#         return 'I am eating'
#
#     def speak(self):
#         return 'I am speaking'
#
#
# class Builder(Human):
#     def builder(self):
#         return 'I am builder'
#
#
# class Sailor(Human):
#     name = 'Jack'
#
#     def speak(self):
#         return ('I am sailor')
#
#     def smoking(self):
#         return 'Bad idea!'
#
#
# class SeaBuilder(Builder, Sailor):
#     pass
#
#
# class Football_player(Human):
#     club = 'Chornomorets'
#     position = 'The attacker'
#
#     def years(self):
#         return 25
#
#     def city(self):
#         return 'Odesa'
#
# class Manager(Builder, Football_player):
#     pass
#
# class Coach(Sailor, Football_player):
#     pass
#
# john = Human()
# print(john.name)
# print(john.eat())
#
# bender = Builder()
# print(bender.name)
# print(bender.speak())
# print(bender.builder())
#
# papay = Sailor()
# print(papay.name)
# print(papay.speak())
# print(papay.smoking())
#
# seal = SeaBuilder()
# print(seal.name)
# seal.builder()
#
# football = Football_player()
# print(football.name)
# print(football.years())
# print(football.speak())
# print(Manager().city())
# print(Coach().club)
#
# # Ще одну професію з 2-ма методами та 2 полями
# # На основі цієї професії зробити два суміжні (з Builder та Sailor)
#
# print(ord('С'))
# print(ord('C'))
#
#
# class Money:
#     currency = 'default'
#     banknotes = 'paper'
#     coins = 0.05
#     change_rate = ''
#
#
# class USADollar(Money):
#     currency = 'USD'
#     banknotes = 'bucks'
#     coins = 'nickels'
#
# class Product(Money):
#     price = 10
#
#     def discount(self, add_discount):
#         self.price -= add_discount