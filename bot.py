# -*- coding: utf-8 -*-
import telebot
import datetime
from telebot import types
token = '1221249595:AAENfywP9LTew9ciIcdM0ajHDtarBJNuG-k'
bot = telebot.TeleBot(token)


def log(message, answer):
    print("\n ------")
    print(datetime.datetime.now())
    print("Сообщение от {0} {1}. (id = {2} \n ID сообщения: {4}".format(message.from_user.first_name, message.from_user.username, str(message.from_user.id), message.text, message.message_id))
    print(answer)

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)
#     print(message)
#     print(message.chat.id)
#     print(message.text)


@bot.message_handler(commands=['help'])
def help(message):
    text = '''
    Добро пожаловать к нам в чат
    Функции бота:
    1. Команда /help -Информация о возможностях
    2. Команда /menu -Возможности ботf'''
    bot.send_message(message.chat.id, text)
    log(message, text)

@bot.message_handler(commands=['menu'])
def menu(message):
    text = """
    Доступные команды бота
    1. In developing
    2. In developing"""
    bot.send_message(message.chat.id, text)
    log(message, text)



@bot.message_handler(content_types=["text"])
def answer_to_hi(message):

    # if message.text == 'Привет':
    #     bot.send_message(message.chat.id, "Привет собака")
    #     log(message, "Привет собака")

    if message == 'меню':
        # Эти параметры для клавиатуры необязательны, просто для удобства
        text =  "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!"
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button_phone, button_geo)
        bot.send_message(message.chat.id, text, reply_markup=keyboard)
        log(message, text)












if __name__ == '__main__':
     bot.polling(none_stop=True)


