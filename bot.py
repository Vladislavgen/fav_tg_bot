# -*- coding: utf-8 -*-
import telebot
import datetime
from telebot import types
token = '1221249595:AAENfywP9LTew9ciIcdM0ajHDtarBJNuG-k'
bot = telebot.TeleBot(token)
countries = {'Россия' : 'Москва', 'Белорусь' : 'Минск', "США" : "Вашингтон", "Англия" : "Лондон"}
countries_keys = list(countries.keys())
commands = {'activate' : 'Activate redirection', 'list' : 'List redirection', 'remove' : 'Remove redirection',
            'deactivate' : 'Deactivate redirection', 'me' : 'Account information', 'filter' : 'Set message filter',
            'filters' : 'list filters applied to a redirection',
            'transformation' : 'automatically replace words/phrases in reposted messages',
            'transformations' : 'list transformations applied to a redirection',
            'add_gateway' : 'setup redirections from channels you dont have invitation link for',
            'remove_gateway' : 'disconnect Telegram Account from the bot',
            'chats' : 'get numerical ids of channels/groups/bots/people', 'clone' : 'clone chat history'}
commands_keys = list(commands.keys())


def log(message, answer):
    print("\n ------")
    print(datetime.datetime.now())
    print("Сообщение от {0} {1}. (id = {2} \n ID сообщения: {4} \n текст сообщения:{3} \n ID чата {5}".format(message.from_user.first_name, message.from_user.username, str(message.from_user.id), message.text, message.message_id, message.chat.id))
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
    2. Команда /menu -Возможности бот'''
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

@bot.message_handler(commands=['channel'])
def channel(message):
    print(message.text)
    raw_message = str(message.text).split()
    print(raw_message)
    command = raw_message[0]
    forward_to = raw_message[1]
    forward_from = raw_message[3]
    action = raw_message[2]

    bot.forward_message(forward_to, forward_from, "57")
    bot.send_message(message.chat.id, "Подписался")
    log(message, "Подписался")


# @bot.message_handler(commands=['activate'])
# def activate(message):
#     text = "Activate redirection"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['list'])
# def lixt(message):
#     text = "List redirection"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['remove'])
# def remove(message):
#     text = "remove redirection"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['deactivate'])
# def deactivate(message):
#     text = "deactivate redirection"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['me'])
# def me(message):
#     text = "account information"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['filter'])
# def filter(message):
#     text = "set message filter"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['filters'])
# def filters(message):
#     text = "list filters applied to a redirection"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['transformation'])
# def transformation(message):
#     text = "automatically replace words/phrases in reposted messages"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['transformations'])
# def transformations(message):
#     text = "list transformations applied to a redirection"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['add_gateway'])
# def add_gateway(message):
#     text = "setup redirections from channels you don't have invitation link for"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['remove_gateway'])
# def add_gateway(message):
#     text = "disconnect Telegram Account from the bot"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['chats'])
# def add_gateway(message):
#     text = "get numerical ids of channels/groups/bots/people"
#     bot.send_message(message.chat.id, text)
#     log(message, text)
#
# @bot.message_handler(commands=['clone'])
# def add_gateway(message):
#     text = "clone chat history"
#     bot.send_message(message.chat.id, text)
#     log(message, text)


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
        text_for_admin = message.from_user.first_name + " Добавил канал"
        bot.send_message(message.chat.id, text)
        bot.send_message("879499877", text_for_admin)
        log(message, text,)

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

    elif message.text in countries_keys:
        text = f"Страна: {message.text} \nСтолица: " + countries.get(message.text)
        bot.send_message(message.chat.id, text, message)
        log(message, text)

    elif message.text in commands_keys:
        text = f"Ваша команда: {message.text} \nВывод: " + commands.get(message.text)
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


