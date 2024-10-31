# file_text = open(file_name, mode)
    # mode (режими)
    # 1. r -> читання (read)
    # 2. w -> записування (write)
    # 3. a -> добавляння (append)
    # 4. r+ -> прочитати та записати (read + wread)
    # 5. w+ ->
    # 6. a+ -> читання та добавляння
    # 7. rb -> відкриття двоічного файла
# file_text = close() - закритя файла
# with open(file_name, mode) as file_text:
#     <body file>

# file_text = open("/Users/andriisumnevych/Documents/testpython.txt","r")
# file_read = file_text.read()
# print(file_read)
# file_read.close()

# with open('/Users/andriisumnevych/Documents/testpython.txt', 'a') as file_text:
#     # file_read = file_text.read()
#     file_text.write('Hello User!!!')
#     # file_read = file_text.read()
#     # print(file_read)

# with open('/Users/andriisumnevych/Documents/testpython.txt', 'r') as file_text:
#     file_read = file_text.read()
#     # file_text.write('Hello User!!!')
#     # file_read = file_text.read()
#     print(file_read)

# readline - читання 1 лінії
# readlines - читання по лініям у форматі списка

# with open('/Users/andriisumnevych/Documents/testpython.txt', 'r') as file_text:
#     file_read = file_text.readlines()
#     # file_text.write('Hello User!!!')
#     # file_read = file_text.read()
#     print(file_read)

# len

# with open('/Users/andriisumnevych/Documents/testpython.txt', 'r') as file_text:
#     file_read = file_text.read()
#     # file_text.write('Hello User!!!')
#     # file_read = file_text.read()
#     print(len(file_read))

# with open("fila_name", "r") as file_text, open("file_name2","w") as file_text:

# Задача - записати в файл 10 рандомних чисел

# import random
#
# list_num = [random.randint(10,99) for i in range(10)]
# str_list = str(list_num)
# str_list = ''.join(str_list)
# print(str_list)
#
# with open('/Users/andriisumnevych/Documents/testpython.txt', 'w+') as file_text:
#     file_text.write(str_list)
import random
# with open("/Users/andriisumnevych/Documents/testpython1.txt", "a") as file_text:
#     # file_read=file_text.read()
#     list_num = [random.randint(10, 99) for i in range(10)]
#     list_str = list(map(str, list_num))
#     str_list = ", ".join(list_str)
#     file_text.write(str_list + '\n')
    # file_read=file_text.read()
    # print(file_read)

# 2. Задача - підрахувати суму файлу

# ver.1

# with open("/Users/andriisumnevych/Documents/testpython1.txt","r") as file_text:
#     (file_read)=file_text.read() # read(number) => number letter from text
#     list_text=file_read.split()
#     ln=[int(i.replace(",","")) for i in list_text]
#     print(sum(ln))
#     print(list_text)

# ver.2

with open("/Users/andriisumnevych/Documents/testpython.txt","r") as file_text:
    (file_read)=file_text.read() # read(number) => number letter from text
    list_text=file_read.split()
    list_map=list(map(lambda i: int(i.replace(",","")),list_text))
    print(list_map)