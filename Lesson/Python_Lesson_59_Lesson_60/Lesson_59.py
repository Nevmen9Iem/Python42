# Дескриптори

class VerboseAttribute:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        value = obj.__dict__[self.name]
        return value.upper()

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

class PhoneValidation(VerboseAttribute):
    def __set__(self, obj, value):
        if ('+380' in value) and (len(value) == 13):
            obj.__dict__[self.name] = value
        else:
            obj.__dict__[self.name] = '+380631234567'

class Book:
    title = VerboseAttribute('title')
    author = VerboseAttribute('author')
    phone_number = PhoneValidation('phone_number')

book = Book()
book.title = 'A Byte of Python'
book.phone_number = '+380639124589'
print(book.title)
print(book.phone_number)

# Напишіть дескриптор, який дозволяє зчитати атрибут лише один раз.

class OneTimeReadDescription:
    def __init__(self, name):
        self.name = name
        self.accessed = False

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

    def __get__(self, obj, objtype):
        if self.accessed:
            raise Exception('Access denied you use your one try to access')
        else:
            self.accessed = True
            return obj.__dict__[self.name]

class SecretData:
    secret_attribute = OneTimeReadDescription('secret_attribute')

some_secret_element = SecretData()
some_secret_element.secret_attribute = '123'
some_secret_element.secret_attribute1 = '456'
print(some_secret_element.secret_attribute)
print(some_secret_element.secret_attribute1)
# input()
# print(some_secret_element.secret_attribute)


# Метакласи

class SomeClass1:
    pass

some_class = SomeClass1()

class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class SomeClass(metaclass=Meta):
    pass

a = SomeClass()
print(SomeClass.attr)
print(a.attr)

object

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        self.args = args

    # def __str__(self):
    #     return f'{self.args}'

a = Singleton(5)
b = Singleton(1)
print(a is b)

print(a)

c = Singleton(6)
print(a)