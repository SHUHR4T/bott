import telebot
import random

from telebot import types

bot = telebot.TeleBot('1894032411:AAHiEK2kQp0FI4v2xFJKWbkZLZGAxXS-jHQ')

# welcome & sticker
@bot.message_handler(commands=['start'])
def start(message):
    sti = open('static/hi.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    
    #  keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Random Son")
    button2 = types.KeyboardButton("Nima Gap ?")
    button3 = types.KeyboardButton('Help')

    markup.add(button1, button2, button3)

    bot.send_message(message.chat.id, "Salom <b>{0.first_name}</b> !\nMen <b>{1.first_name}</b> botman".format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)

#  help
@bot.message_handler(commands=['help'])
def mess(message):
    bot.send_message(message.chat.id, "Admin/Creator 👨‍💻 : @SHUHR47")

@bot.message_handler(content_types=['text'])
def buttons(message):
    sti2 = open('static/debil.webp', 'rb')
    if message.chat.type == 'private':
        if message.text == 'Random Son':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Nima Gap ?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Yaxshi", callback_data='good')
            item2 = types.InlineKeyboardButton("Yomon", callback_data='bad')
 
            markup.add(item1, item2)

            bot.send_message(message.chat.id, "O'zingchi ?" , reply_markup=markup)
        
        elif message.text == 'Help':
            bot.send_message(message.chat.id, "Admin / Creator 👨‍💻 : @SHUHR47")

        else :
            bot.send_sticker(message.chat.id, sti2)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, '👌')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, '🤷‍♂️')


            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="O'zingchi ?",
                reply_markup=None)

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)