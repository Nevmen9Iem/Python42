# dict [key: value]

dt_1 = {"p1": "Movie", "p2": "Sci-Fi", "p3": "Ster wars", "p4": 2019, "p5": "Part 7"}
dt_2 = {"p2": "Horror", "p4": 2020, "p6": "USA, UA"}
##print(dt_1["p1"])

##for i,j in dt_1.items():
##    print("key:",i,"value:",j)

# .get (або просто =) - добавити

##dt_1["p6"] = 100
##print(dt_1)

# .update - обновити, замінити значення

##dt_1.update([("p1","Game"),("p4",2020)])
##print(dt_1)
##
##dt_1.update(dt_2)
##print(dt_1)

# del / .pop - delete, .clear - all delete

##del dt_1['p6']
##print(dt_1)
##dt_1.pop('p6')
##print(dt_1)
##dt_1.clear()
##print(dt_1)

# .keys - Вивід ключів

##keyList = list(dt_1.keys())
##print(keyList)
##print()

# .values - Вивід значення

##valuesList = list(dt_1.values())
##print(valuesList)
##print()
##
##key_values_list = list(dt_1.items())
##print(key_values_list)

# .copy - копіювати словник (= - обєднує словники, а не копіює)

##dt_2 = dt_1.copy()
##print(dt_1)

# users_list = [
# {'name':'Jack', 'role':'admin','year':2010, 'salary':120},
# {'name':'Anna', 'role':'superadmin','year':2015, 'salary':130},
# {'name':'Mark', 'role':'user','year':2022, 'salary':60},
# {'name':'Dan', 'role':'viewer','year':2019, 'salary':100}]

##print(users_list)
##
##users_salary = list(filter(lambda i: i['salary']>80 and i['year']>2017, users_list))
##print(users_list)
##
##for a in users_salary:
##    for i,j in a.items():
##        print(i," ",j)

# .sorted

##sort_salary = sorted(users_list, key = lambda i: i ['salary'])
##print(sort_salary)

# users_list2 = users_list.copy()
# print(users_list2)
#
# users_list2[3].update([('role', 'user')])
# print(users_list2)
#
# users_list3 = users_list2.copy()
# users_list3[3].update([('salary', 150)])
# print(users_list3)

# Задача

# dict => login and pass for users
# function login and pass
# YES / NO

def log_pass(a, b):
    log_pass = {"login1": "admin", "pass1": 1111, "login2": "user", "pass2": 2222}
    value_list = list(log_pass.values())

    if a in value_list:
        # print("yes")
        # print(value_list.index(a)+1)
        if b == value_list[value_list.index(a) + 1]:
            print("YES")
        else:
            print("Error pass")
    else:
        print("No user in system")


# -----main()---------
a = input("Login = ")
b = int(input("Pass = "))

log_pass(a, b)