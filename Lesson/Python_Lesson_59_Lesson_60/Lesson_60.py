print("Lesson 60")

# Створити метаклас який забороняє успадкування

class NoSubClassesMeta(type):
    def __init__(cls, name, bases, namespace):
        for base in bases:
            if isinstance(base, NoSubClassesMeta):
                raise TypeError("Subclassing Not Allowed")
        super().__init__(name, bases, namespace)

class BaseClass(metaclass=NoSubClassesMeta):
    pass

# class DerivedClass(BaseClass):
#     pass

print(BaseClass.__name__)


# Протокол інструкцій

class Meta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return super().__prepare__(name, bases)

    def __new__(metacls, name, bases, namespace):
        return super().__new__(metacls, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)

class MyClass(metaclass=Meta):
    pass

m = MyClass()

