# Кортежі

##tuple1=()
##tuple2=tuple()
##
##print(type(tuple1))
##print(type(tuple2))

##tuple1 = ("admin", "user", "superadmin", "superuser")
##tuple2 = tuple((1,2,3,4,5))

##print(tuple1[2])
##print(tuple2[0])
##print()
##print(len(tuple1))
##print(sum(tuple2))
##
##for i in range(len(tuple1)):
##    print(tuple1[i])

##user1,*user2,user4=tuple1
##print(type(user1))
##print(user2)

##if "admin" in tuple1:
##    print("YES")
##else:
##    print("NO")

##tuple11 = tuple1 + tuple1
##print(tuple11)
##
##for i in range(len(tuple11)):
##    print(tuple11[i], tuple11.count(tuple11[i]))

# Множини

##set1 = {1,2,3}
##set2 = set((1,2,3))
##
##print(set1)
##print(set2)

# intersection

##set1 = {1,2,5,4,3}
##set2 = {2,3}
##print("set1 =", set1)
##print("set2 =", set2)

# & | - елементи

##print(set1 & set2)
##print(set1.intersection(set2))

# union - зєднання сетів

##print(set1 | set2)
##print(set1.union(set2))

# difference - відмінність (різне)

##print(set1 - set2)
##print(set1.difference(set2))
##print(set1.symmetric_difference(set2))

##for i in set1:
##    print(i)

# .update - додати елементи
# .discard - видалити елементи без змін
# .remove - видалити елементи

##print(sorted(set1))
##print(len(set1))
##print(min(set1))
##print(max(set1))
##print(enumerate(set1))
##
##for i,j in enumerate(set1):
##    print(i,j)

# frozenset - замороження списку (не можна додати чи удалити но можна із ним працювати) 

##set1 = frozenset((set1))
##print(set1)

##import random
##
##list_num = [random.randint(10,20) for i in range(20)]
##print(list(list_num))
##print(list(set(list_num)))
##print(tuple(set(list_num)))

text = "Our online English classes feature lots of useful learning materials and activities to help you develop your reading skills with confidence in a safe and inclusive learning environment. Practise reading with your classmates in live group classes, get reading support from a personal tutor in one-to-one lessons or practise reading by yourself at your own speed with a self-study course."

text1=list(set(text.lower()))
text2=list(filter(lambda i: i!=','and i!=' ' and i!=':' and i!="'" and i!='"' and i!="." and i!='-',text1))
print(text2)
print(sorted(text2),"  ", len(text2))
