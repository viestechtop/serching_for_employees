import telebot
from telebot import types

import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton('Дизайнер', callback_data='designer')
    itembtn2 = types.InlineKeyboardButton('Копирайтер', callback_data='copywriter')
    itembtn3 = types.InlineKeyboardButton('Директолог', callback_data='directologist')
    markup.add(itembtn1, itembtn2, itembtn3)

    bot.send_message(message.chat.id, f'Привет!\n\nСпасибо за отклик.\n'
                                      f'Первый этап на пути к долгой совместной работе - анкетирование.\n\n'
                                      f'Заполни анкету (это займет не более двух минут), '
                                      f'а после этого мы свяжемся с тобой и назначим собеседование.\n\n'
                                      f'Выбери вакансию', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'designer':
                bot.send_message(call.message.chat.id,
                                 'https://docs.google.com/forms/d/e/1FAIpQLSfaJyJNJJd_RgHAPVxhL0qj_n6WvUMgasgQbAwaGljLjIsiHA/viewform')
            elif call.data == 'copywriter':
                bot.send_message(call.message.chat.id,
                                 'https://docs.google.com/forms/d/e/1FAIpQLSfTq8ZBawURshj9WT-Z4oAWZGvYNYnMeqlybs4GZz3KZegnBg/viewform')
            elif call.data == 'directologist':
                bot.send_message(call.message.chat.id,
                                 'https://docs.google.com/forms/d/e/1FAIpQLSdUA3T3mwKj2nryzoxX1sMapUtdCmtsMwBL2M67HCNoxV6x4Q/viewform')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Ссылка на анкету',
                                  reply_markup=None)

    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    bot.polling(none_stop=True)
