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

    if message.text == 'меню':
        # Эти параметры для клавиатуры необязательны, просто для удобства
        text =  "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!"
        #Создаем объект клавиатура задем размер и автоматический re-size по ширине
        keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        #Кнопка номер один: номер телефона
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        #Кнопка номер два: Местоположение пользователя
        button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        #Добавление кнопок в объект клавиатура
        keyboard.add(button_phone, button_geo)
        #Отправка сообщения с созданной ранее клавиатурой
        bot.send_message(message.chat.id, text, reply_markup=keyboard)
        #Логирование
        log(message, text)


    elif str(message.text).title() == 'Бот':
         text = "TEXT"
         keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
         button_channel1 = types.KeyboardButton(text="Добавить канал")
         button_channel2 = types.KeyboardButton(text="Убрать канал")
         button_info = types.KeyboardButton(text="Информация")
         button_list = types.KeyboardButton(text="Список каналов")
         keyboard.add(button_channel1, button_channel2, button_info, button_list)
         bot.send_message(message.chat.id, text, reply_markup=keyboard)

         log(message, text)

    elif message.text == 'Добавить канал':
        text = "Добавил канал"
        bot.send_message(message.chat.id, text, message)
        log(message, text)

    elif message.text == 'Убрать канал':
        text = "Убрал канал"
        bot.send_message(message.chat.id, text, message)
        log(message, text)

    elif message.text == 'Информация':
        text = "Предоставляю ИНФОРМАЦИЮ"
        bot.send_message(message.chat.id, text, message)
        log(message, text)

    elif message.text == 'Список каналов':
        text = "1)2ch/Двач"
        bot.send_message(message.chat.id, text, message)
        log(message, text)
#
#     elif message.text:
#         bot.reply_to(message, "Сам {!s}".format(message.text))
#         log(message, message.text)
#
#
#
#
#
#
#
#
# @bot.edited_message_handler(func=lambda message: True)
# def edit_message(message):
#     bot.edit_message_text(chat_id=message.chat.id,
#                           text= "Сам {!s}".format(message.text),
#                           message_id=message.message_id + 1)
#     log(message, message.text)












if __name__ == '__main__':
     bot.polling(none_stop=True)


