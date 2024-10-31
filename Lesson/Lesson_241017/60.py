# Створити MetaClass який забороняє успадкування

# class NoSubclassesMeta(type):
#     def __init__(cls, name, bases, namespace):
#         for base in bases:
#             if isinstance(base, NoSubclassesMeta):
#                 raise TypeError('Cannot subclass NoSubclassesMeta')
#         super().__init__(name, bases, namespace)
#
#
# class BaseClass(metaclass=NoSubclassesMeta):
#     pass
#
# # class DerivedClass(BaseClass):
# #     pass
#
#
# print(BaseClass.__name__)


# class Meta(type):
#     @classmethod
#     def __prepare__(metacls, name, bases):
#         return super().__prepare__(name, bases)
#
#     def __new__(metacls, bases, namespace):
#         return super().__new__(metacls, bases, namespace)
#
#     def __init__(metacls, name, bases, namespace):
#         super().__init__(name, bases, namespace)
#
# class MyClass(metaclass=Meta):
#     pass
#
# m = MyClass()

# Записна книжка
