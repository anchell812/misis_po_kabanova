import telebot
import datetime
import os

token = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(token)
chat_id = 219512885


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, '+message.from_user.first_name, parse_mode='html')


def my_function(message):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    result = "Топ треков на дату: " + current_date
    return result


@bot.message_handler(commands=['date'])
def mdate(message):
    result = my_function(message)
    bot.send_message(message.chat.id, result, parse_mode='html')


@bot.message_handler(content_types=['text'])
def echo_all(message):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    bot.send_message(message.chat.id, "Топ песен на: "+current_date)
    bot.send_document(message.chat.id, open(r'tests/reposts/results.txt', 'rb'))


# Запуск бота
bot.polling(none_stop=True)

