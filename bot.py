# -*- coding: utf-8 -*-

import telebot
token = '1221249595:AAENfywP9LTew9ciIcdM0ajHDtarBJNuG-k'
bot = telebot.TeleBot(token)




# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)
#     print(message)
#     print(message.chat.id)
#     print(message.text)



@bot.message_handler(content_types=["text"])
def answer_to_hi(message):

    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Привет собака")


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['help'])
def help(message):
    text = '''
    Добро пожаловать к нам в чат
    Функции бота:
    1. Команда /help -Информация о возможностях
    '''
    bot.send_message(message.chat.id, text)









if __name__ == '__main__':
     bot.polling(none_stop=True)


