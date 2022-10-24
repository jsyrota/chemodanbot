from telebot.util import string
import telebot
from telebot import types
from telebot.types import Message


bot = telebot.TeleBot('5347907276:AAGu3i12aVav2glSoLBpVXp0fEXfsp4q9J0')

users = {}


@bot.message_handler(commands=["start"])
def start(m, res=False):
  markup=types.InlineKeyboardMarkup(row_width=1)

  markup.add(
    types.InlineKeyboardButton("Предложить пост", callback_data="suggest_post"),
    types.InlineKeyboardButton("Указать на ошибку", callback_data="bug_report"),
    types.InlineKeyboardButton("Написать сообщение", callback_data="send_msg")
  )

  bot.send_message(m.chat.id, 'Вас приветствует администрация канала "Чемоданчик пруфов".\nЧем мы можем вам помочь?',  reply_markup=markup)


@bot.message_handler()
def handle_text(message):
  if message.from_user.id in users.keys():
    message_sender_id = message.from_user.id
    if message.from_user.username is None:
      message_sender_user = "пользователя без юзера"
    else:
      message_sender_user = '@' + message.from_user.username
    if message.from_user.first_name is None:
      message_sender_name = "без имени"
    else:
      message_sender_name = "с именем " + message.from_user.first_name
    if message.from_user.last_name is None:
      message_sender_lastname = ' '
    else:
      message_sender_lastname = message.from_user.last_name

    bot.send_message(-1001756857166, f"Новое сообщение от {message_sender_user} {message_sender_name} {message_sender_lastname} и ID {message_sender_id}.\nОн хочет {users[message.from_user.id]}: \n{message.text}")
    
    del users[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == ('suggest_post'))    
def callback_suggest_post(call):
  bot.send_message(call.message.chat.id, 'Огромное спасибо за стремление сделать свой вклад в развитие канала. Поделитесь вашей идеей:')
  users[call.from_user.id] = 'предложить пост'


@bot.callback_query_handler(func=lambda call: call.data == ('bug_report'))    
def callback_bug_report(call):
  bot.send_message(call.message.chat.id, 'Мы умеем признавать свои ошибки и очень рады вашему стремлению помочь. Укажите, пожалуйста, пост и место где вы увидели ошибку:')
  users[call.from_user.id] = 'указать на ошибку'


@bot.callback_query_handler(func=lambda call: call.data == ('send_msg'))    
def callback_send_msg(call):
  bot.send_message(call.message.chat.id, 'Мы всегда рады любой обратной связи! Оставьте ваше сообщение:')
  users[call.from_user.id] = 'написать сообщение'


bot.infinity_polling()
