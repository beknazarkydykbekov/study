import telebot
from telebot import types
from config import token
from parser import information 
from parser import main_info
from parser import list_img

bot = telebot.TeleBot(token)

bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hey mate, let's parse the insta")

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    chat_id = c.message.chat.id 
    income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    b1 = types.KeyboardButton('Posts')
    income_keyboard.add(b1)

def send_data(message):
    chat_id = message.chat.id
    entry = message.text
    if entry == 'Posts':
        try:
            bot.send_message(chat_id, information, main_info)
        except:
            bot.send_message(chat_id, 'some problem has occccurred')

bot.polling()