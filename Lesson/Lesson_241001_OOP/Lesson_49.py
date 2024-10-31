# Функції

def solution(something):
    return something


print(solution('Hello World'))
print(solution('Hello World'))
print(solution('Hello World'))

# ООП

s = "Hello World"
print(s, type(s))


class First:
    data = '123'  # атрибут класу, аргумент класу, поле класу, змінна класу

    # атрибут, назва атрибуту, відповідає на питання хто, що, скільки, коли
    def create(self):  # метод класу, функція класу
        return First.data
    # метод, назва методу, відповідає на що робив, що зробив


variable_name = 'snake_style'  # імена змінних
variableName = 'camelCase'  # імена класів

variablename = 'nostylecase'  # не пишіть так, ніколи
one = First()
print(one.data)
print(one.create())

l = []
l = list()
l.append(1)


class Borsch:
    ingridients = ['beet', 'cabbage', 'bean', 'potate']
    spices = ['red_pepper', 'chile_pepper', 'garlic']
    meat = 'pork'  # beef, chicken
    value = 3
    date_to_expire = '2024-10-11'
    temperature = 3

    def boiled(self, temperature):
        self.temperature = temperature
        return f'boiled to {temperature} degreece'

    def eat(self):
        return f'eat borsch'

    def show(self):
        return f'you can see current borsch'
