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







@bot.message_handler(content_types=["text"])
def answer_to_hi(message):
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


    elif message.text in countries_keys:
        text = f"Страна: {message.text} \nСтолица: " + countries.get(message.text)
        bot.send_message(message.chat.id, text, message)
        log(message, text)

    elif message.text in commands_keys:
        text = f"Ваша команда: {message.text} \nВывод: " + commands.get(message.text)
        bot.send_message(message.chat.id, text, message)
        log(message, text)












if __name__ == '__main__':
     bot.polling(none_stop=True)


