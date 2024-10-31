import random

import telebot

# def write_file(res):
#     with open('/Users/andriisumnevych/Documents/lesson_19.12092024.txt', "a+", encoding='utf-8') as file_in:
#         file_in.write(str(res) + "\n")
# ver.1
# while True:
#     t = int(input("1 - Start, 2 - Exit: "))
#     if t==2:
#         break
#     elif t==1:
#         a=int(input("a = "))
#         b=random.randint(1,3)
#
#         if a==1 and b==1 or a==2 and b==2 or a==3 and b==3:
#             res = "Win-Win", a, b
#             write_file(res)
#             print("Win-Win",a,b)
#         elif a==1 and b==2 or a==1 and b==3 or a==2 and b==3:
#             res = "Win-Player", a, b
#             write_file(res)
#             print("Win-Player",a,b)
#         elif a==2 and b==1 or a==3 and b==1 or a==3 and b==2:
#             res = "Win-Bot", a, b
#             write_file(res)
#             print("Win-Bot",a,b)
#         else:
#             print("Erorr",a,b)
# ver.2
# a = int(input("Num 1 = "))
# b = int(input("Num 2 = "))
# c = int(input("Select: 1 = +, 2 = -, 3 = *, 4 = / "))
#
# if c==1:
#     ab = a + b
#     write_file(ab)
#     print("Result: a + b =", a+b)
# elif c==2:
#     ab = a - b
#     write_file(ab)
#     print("Result: a - b =", a-b)
# elif c==3:
#     ab = a * b
#     write_file(ab)
#     print("Result: a * b =", a*b)
# elif c==4:
#     ab = a / b
#     write_file(ab)
#     print("Result: a / b =", a/b)
# else:
#     print("Error")
# ver.3
# def writefile(ab):
#     with open('/Users/andriisumnevych/Documents/lesson_19.txt', "a+", encoding='utf-8') as file_in:
#         file_in.write(str(ab) + '\n')
#
#
# t = True
# while t == True:
#     c = int(input("Select : 1 - '+', 2 - '-', 3 - '*', 4 - '/', 5 - Exit: "))
#     a = int(input("Input action number = "))
#     b = int(input("Input action number = "))
#     if c == 1:
#         ab = a + b
#         writefile(ab)
#         print(ab)
#     elif c == 2:
#         ab = a - b
#         writefile(ab)
#         print(ab)
#     elif c == 3:
#         ab = a * b
#         writefile(ab)
#         print(ab)
#     elif c == 4:
#         ab = a / b
#         writefile(ab)
#         print(ab)
#     elif c == 5:
#         print("Exit? [y/n]")
#         d = input("Answer = ")
#         if d == "n":
#             t = True
#         else:
#             t = False
#     else:
#         print("Error")
# with open('/Users/andriisumnevych/Documents/lesson_19.txt', "a+", encoding='utf-8') as file_read:
#     file_read.seek(0)
#     print(file_read.read())
# /usr/local/bin/python3 -m pip install pyTelegramBotAPI
# Telegram bot
# <b>text</b> bold
# <em>text</em> italic
# <i>text</i> italic
# <u>text</u> underline

bot = telebot.TeleBot('7515066181:AAHYFTOmitgucja82BPGT9AJ1aOCz4NBmOk')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b><u>Hello, Python Bot!!!</u></b>', parse_mode='html')


@bot.message_handler(content_types=['text'])
def user_text(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, 'Hi! Hi!' + message.from_user.first_name)
    elif message.text == "Num":
        num = random.randint(1, 1000)
        bot.send_message(message.chat.id, num)
    elif message.text == "Show":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMiZuMrfzC3qHix1XRC2E60rc9KxvcAArMOAAJZ_JlLTTH_Vlaigg42BA')
    elif message.text == "Photo":
        ph = open('E:/Фотки/IMAG0008.jpg', 'rb')
        bot.send_photo(message.chat.id, ph)
    else:
        bot.send_message(message.chat.id, 'Erorr')


@bot.message_handler(content_types=['sticker'])
def user_sticker(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, sticker_id)


bot.infinity_polling()
