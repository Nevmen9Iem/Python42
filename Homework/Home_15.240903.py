# Задача 1

# Дано пари key_value:

#    type: A, class: High, Price:1000, Level: 5, Room:25, Fee: Yes

#        а) Необхідно створити словник, як мінімум 3 способами;
#        b) Додати до словника, нової пари Discount: 0.2;
#        c) Замінити значення у парі Price, з 1000 на 1500;
#        d) Видалити ключ Fee;
#        e) Створити список, використовуючи крім вище зазначеного словника, ще такі пари:

#    type: A, class: Middle, Price:700, Level: 2, Room:10, Discount: 0.1
#    type: B, class: High, Price:1200, Level: 7, Room:38, Discount: 0
#    type: B, class: High, Price:1200, Level: 8, Room:39, Discount: 0.2
#    type: C, class: Low, Price:600, Level: 3, Room:16, Discount: 0.3

#        f) Для створеного списку використовуючи filter() та lambda функцію покажіть список у якому Price >800;
#        h) Для створеного списку використовуючи filter() та lambda функцію покажіть список у якому Discount=0;
#        i) Для створеного списку використовуючи filter() та lambda функцію покажіть список у якому class=High.

my_dict = {'type': 'A','class': 'High','Price': 1000,'Level': 5,'Room': 25,'Fee': 'Yes'}
print('a.1) > ', my_dict)

my_dict_1 = dict(type = 'A', class_ = 'High', Price = 1000, Level = 5, Room = 25, Fee = 'Yes')
print('a.2) > ', my_dict_1)

my_dict_2 = dict([('type', 'A'), ('class', 'High'), ('Price', 1000), ('Level', 5), ('Room', 25), ('Fee', 'Yes')])
print('a.3) > ', my_dict_2)

my_key = ['type', 'class', 'Price', 'Level', 'Room', 'Fee']
my_value = ['A', 'High', 1000, 5, 25, 'Yes']
my_dict_3 = dict(zip(my_key, my_value))
print('a.4) > ', my_dict_3)

my_key1 = ['type', 'class', 'Price', 'Level', 'Room', 'Fee']
my_value1 = ['A', 'High', 1000, 5, 25, 'Yes']
my_dict_4 = {key1: value1 for key1, value1 in zip(my_key1, my_value1)}
print('a.5) > ', my_dict_4)

my_dict_1['Discount'] = 0.2
print('b) > ', my_dict_1)

my_dict_1['Price'] = 1500
print('c) > ', my_dict_1)

del my_dict['Fee']
print('d) > ', my_dict)

my_dict_1.pop('Fee')
print('d.1) > ', my_dict_1)

my_dict_new = ([my_dict_1.copy(),
                dict(type = 'A', class_ = 'Middle', Price = 700, Level = 2, Room = 10, Discount = 0.1),
                dict(type = 'B', class_ = 'High', Price = 1200, Level = 7, Room = 38, Discount = 0),
                dict(type = 'B', class_ = 'High', Price = 1200, Level = 8, Room = 39, Discount = 0.2),
                dict(type = 'C', class_ = 'Low', Price = 600, Level = 3, Room = 16, Discount = 0.3)])
print('e) > ', my_dict_new)
num = 0
for l in my_dict_new:
    num += 1
    print(f'e.{num}) > {l}')

my_dict_f = list(filter(lambda i: i['Price'] > 800, my_dict_new))
print('f) > ', my_dict_f)
num = 0
for l in my_dict_f:
    num += 1
    print(f'f.{num}) > {l}')

my_dict_h = list(filter(lambda i: i['Discount'] == 0, my_dict_new))
print('h) > ', my_dict_h)

my_dict_i = list(filter(lambda i: i['class_'] == 'High', my_dict_new))
print('i) > ', my_dict_i)
num = 0
for l in my_dict_i:
    num += 1
    print(f'i.{num}) > {l}')


