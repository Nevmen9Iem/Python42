import telebot
from google.cloud import bigquery
from google.oauth2 import service_account
## import bq


##bot = telebot.TeleBot('7515066181:AAHYFTOmitgucja82BPGT9AJ1aOCz4NBmOk')

##@bot.message_handler(commands=['start'])
##def start(message):
##    bot.send_message(message.chat.id, '<b><u>Hello, Python Bot!!!</u></b>', parse_mode='html')
##
##
##@bot.message_handler(content_types=['text'])
##def user_text(message):
##    if message.text == "Hi":
##        bot.send_message(message.chat.id, 'Hi! Hi!' + message.from_user.first_name)
##    elif message.text == "Num":
##        num = random.randint(1, 1000)
##        bot.send_message(message.chat.id, num)
##    elif message.text == "Show":
##        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMiZuMrfzC3qHix1XRC2E60rc9KxvcAArMOAAJZ_JlLTTH_Vlaigg42BA')
##    elif message.text == "Photo":
##        ph = open('E:/Фотки/IMAG0008.jpg', 'rb')
##        bot.send_photo(message.chat.id, ph)
##    else:
##        bot.send_message(message.chat.id, 'Erorr')

##
##@bot.message_handler(content_types=['sticker'])
##def user_sticker(message):
##    sticker_id = message.sticker.file_id
##    bot.send_message(message.chat.id, sticker_id)
##
##
##bot.infinity_polling()


bot=telebot.TeleBot("7515066181:AAHYFTOmitgucja82BPGT9AJ1aOCz4NBmOk")
credentials=service_account.Credentials.from_service_account_file("/Users/andriisumnevych/Library/Mobile Documents/com~apple~CloudDocs/Python/ITStep/itstep-382618-558382b49c6f.json")
project_id="itstep-382618"
client=bigquery.Client(credentials=credentials,project=project_id)
@bot.message_handler(commands=['start'])
def start(message):
    msg=bot.send_message(message.chat.id,"Привет, "+message.from_user.first_name)
 
@bot.message_handler(content_types=['text'])
def info(message):
    if message.text.lower()=="sum":
        query_job=client.query("""
                                SELECT 
                                round(sum(tb.payment_sum),2) AS sum_total
                                FROM `itstep-382618`.itstep_bot.data_tb AS tb  
                               """)
        results=query_job.result()
        bot.send_message(message.chat.id,results)
    elif message.text.lower()=="gsum":
        query_job=client.query("""
                                SELECT 
                                tb.period,
                                round(sum(tb.payment_sum),2) AS sum_total
                                FROM `itstep-382618`.itstep_bot.data_tb AS tb
                                GROUP BY tb.period
                                ORDER BY 2 DESC
                                LIMIT 5 
                               """)
        results=query_job.result()
        bot.send_message(message.chat.id,results)
 
bot.infinity_polling()



