# import telebot
# import datetime
#
# bot = telebot.TeleBot('6540157313:AAFkm6NYUXqT8N_Nf72l-hg_mjfiKqU0ntI')
#
#
# # @bot.message_handler(commands=['start'])
# # def start(message):
# #     bot.send_message(message.chat.id, 'Привет', parse_mode='html')
# #
# #
# # bot.polling(none_stop=True)
#
# def my_function(message):
#     current_date = datetime.datetime.now().strftime("%Y-%m-%d")
#     result = "Результат функции с текущей датой: " + current_date
#     return result
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     # Вызываем функцию при вводе команды /start
#     result = my_function(message)
#     bot.reply_to(message, result)
#
# # Запуск бота
# bot.polling()

import telebot
import datetime
# from misis_po_kabanova.tests.my_function import MyFunction

bot = telebot.TeleBot('') # добавить
# my_func = MyFunction.get_top_songs()


# def my_function(message):
#     return my_func


# @bot.message_handler(commands=['get'])
# def get(message):
#     result = my_function(message)
#     bot.reply_to(message, result)


# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, {message.from_user.first_name}'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
#
# @bot.message_handler(commands=['results'])
# def get(message):
#
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
#
# @bot.message_handler(commands=['id'])
# def get_id(message):
#     mess = f'ID = {message.chat.id}'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
# # Запуск бота
# bot.polling(none_stop=True)