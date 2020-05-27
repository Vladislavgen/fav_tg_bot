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


if __name__ == '__main__':
     bot.polling(none_stop=True)

