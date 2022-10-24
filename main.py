{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMjt3hlvsVtKyCLC82+V7uX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jsyrota/chemodanbot/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DRWwD1tGzdJa",
        "outputId": "e087b527-3f9e-44dd-b144-e0a3599aedcb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Python 3.7.15\n"
          ]
        }
      ],
      "source": [
        "!python3 --version"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip3 install pytelegrambotapi"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CnZ26EC_zl9B",
        "outputId": "648e83b5-1b29-4030-a319-ff7ce34d8011"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pytelegrambotapi\n",
            "  Downloading pyTelegramBotAPI-4.7.1.tar.gz (213 kB)\n",
            "\u001b[K     |████████████████████████████████| 213 kB 13.9 MB/s \n",
            "\u001b[?25hRequirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from pytelegrambotapi) (2.23.0)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->pytelegrambotapi) (1.24.3)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->pytelegrambotapi) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->pytelegrambotapi) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->pytelegrambotapi) (2022.9.24)\n",
            "Building wheels for collected packages: pytelegrambotapi\n",
            "  Building wheel for pytelegrambotapi (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pytelegrambotapi: filename=pyTelegramBotAPI-4.7.1-py3-none-any.whl size=196988 sha256=f277b66cfc24d62ac7975865e5b1eb1b057c0b56f3225b39813be1caa758c24d\n",
            "  Stored in directory: /root/.cache/pip/wheels/84/72/5f/8a7b3ca1ef1250002cf3bac48e0c72c5ee5c9596a5b1295dc1\n",
            "Successfully built pytelegrambotapi\n",
            "Installing collected packages: pytelegrambotapi\n",
            "Successfully installed pytelegrambotapi-4.7.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from telebot.util import string\n",
        "import telebot\n",
        "from telebot import types\n",
        "from telebot.types import Message\n",
        "\n",
        "# Создаем экземпляр бота\n",
        "\n",
        "bot = telebot.TeleBot('token')\n",
        "global message_type\n",
        "global thanks\n",
        "#global answer\n",
        "# Функция, обрабатывающая команду /start\n",
        "\n",
        "@bot.message_handler(commands=[\"start\"])\n",
        "\n",
        "def start(m, res=False):\n",
        "\n",
        "        # Добавляем две кнопки\n",
        "\n",
        "        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)\n",
        "\n",
        "        item1=types.KeyboardButton(\"Предложить пост\")\n",
        "\n",
        "        item2=types.KeyboardButton(\"Указать на ошибку\")\n",
        "\n",
        "        item3=types.KeyboardButton(\"Написать сообщение\")\n",
        "\n",
        "        markup.add(item1)\n",
        "\n",
        "        markup.add(item2)\n",
        "\n",
        "        markup.add(item3)\n",
        "\n",
        "        bot.send_message(m.chat.id, 'Вас приветствует администрация канала.\\nЧем мы можем вам помочь?',  reply_markup=markup)\n",
        "\n",
        "@bot.message_handler()\n",
        "# Получение сообщений от пользователя\n",
        "\n",
        "def handle_text(message):\n",
        "  global message_type\n",
        "  global thanks\n",
        "  global userAnswer\n",
        "  if message.text.strip() == \"Предложить пост\":\n",
        "    userAnswer = 'Огромное спасибо за стремление сделать свой вклад в развитие канала. Поделитесь вашей идеей:'\n",
        "    message_type = 'предложить пост'\n",
        "    thanks = 'Благодарим за ваше предложение. Мы обязательно рассмотрим его в ближайшее время.'\n",
        "\n",
        "  elif message.text.strip() == \"Указать на ошибку\":\n",
        "    userAnswer = 'Мы умеем признавать свои ошибки и очень рады вашему стремлению помочь. Укажите, пожалуйста, пост и место где вы увидели ошибку:'\n",
        "    message_type = 'указать на ошибку'\n",
        "    thanks = 'Спасибо за внимательность к нашим постам. Мы рассмотрим ваше замечание в ближайшее время.'\n",
        "\n",
        "  elif message.text.strip() == \"Написать сообщение\":\n",
        "    userAnswer = 'Мы всегда рады любой обратной связи! Оставьте ваше сообщение:'\n",
        "    message_type = 'написать сообщение'\n",
        "    thanks = 'Мы благодарны за ваше сообщение и ответим вам в кратчайшие сроки.'\n",
        "  bot.register_next_step_handler(message, send_answer)\n",
        "\n",
        "def send_answer(message: Message):\n",
        "  bot.send_message(message.chat.id, userAnswer)\n",
        "  bot.register_next_step_handler(message, send_poslanie)\n",
        "\n",
        "def send_poslanie(message: Message):\n",
        "  message_worked = message.text\n",
        "  message_sender_id = message.from_user.id\n",
        "  if message.from_user.username is None:\n",
        "    message_sender_user = \"пользователя без юзера\"\n",
        "  else:\n",
        "    message_sender_user = '@' + message.from_user.username\n",
        "  if message.from_user.first_name is None:\n",
        "    message_sender_name = \"без имени\"\n",
        "  else:\n",
        "    message_sender_name = \"с именем \" + message.from_user.first_name\n",
        "  if message.from_user.last_name is None:\n",
        "    message_sender_lastname = ' '\n",
        "  else:\n",
        "    message_sender_lastname = message.from_user.last_name\n",
        "  bot.send_message(-1001756857166, f\"Новое сообщение от {message_sender_user} {message_sender_name} {message_sender_lastname} и ID {message_sender_id}.\\nОн хочет {message_type}: \\n{message_worked}\")\n",
        "  bot.send_message(message.chat.id, thanks)\n",
        "\n",
        "\n",
        "# Запускаем бота\n",
        "\n",
        "bot.infinity_polling()"
      ],
      "metadata": {
        "id": "VHxpKCBbzsj9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from telebot.util import string\n",
        "import telebot\n",
        "from telebot import types\n",
        "from telebot.types import Message\n",
        "\n",
        "\n",
        "bot = telebot.TeleBot('5347907276:AAGu3i12aVav2glSoLBpVXp0fEXfsp4q9J0')\n",
        "\n",
        "users = {}\n",
        "\n",
        "\n",
        "@bot.message_handler(commands=[\"start\"])\n",
        "def start(m, res=False):\n",
        "  markup=types.InlineKeyboardMarkup(row_width=1)\n",
        "\n",
        "  markup.add(\n",
        "    types.InlineKeyboardButton(\"Предложить пост\", callback_data=\"suggest_post\"),\n",
        "    types.InlineKeyboardButton(\"Указать на ошибку\", callback_data=\"bug_report\"),\n",
        "    types.InlineKeyboardButton(\"Написать сообщение\", callback_data=\"send_msg\")\n",
        "  )\n",
        "\n",
        "  bot.send_message(m.chat.id, 'Вас приветствует администрация канала \"Чемоданчик пруфов\".\\nЧем мы можем вам помочь?',  reply_markup=markup)\n",
        "\n",
        "\n",
        "@bot.message_handler()\n",
        "def handle_text(message):\n",
        "  if message.from_user.id in users.keys():\n",
        "    message_sender_id = message.from_user.id\n",
        "    if message.from_user.username is None:\n",
        "      message_sender_user = \"пользователя без юзера\"\n",
        "    else:\n",
        "      message_sender_user = '@' + message.from_user.username\n",
        "    if message.from_user.first_name is None:\n",
        "      message_sender_name = \"без имени\"\n",
        "    else:\n",
        "      message_sender_name = \"с именем \" + message.from_user.first_name\n",
        "    if message.from_user.last_name is None:\n",
        "      message_sender_lastname = ' '\n",
        "    else:\n",
        "      message_sender_lastname = message.from_user.last_name\n",
        "\n",
        "    bot.send_message(-1001756857166, f\"Новое сообщение от {message_sender_user} {message_sender_name} {message_sender_lastname} и ID {message_sender_id}.\\nОн хочет {users[message.from_user.id]}: \\n{message.text}\")\n",
        "    \n",
        "    del users[message.from_user.id]\n",
        "\n",
        "@bot.callback_query_handler(func=lambda call: call.data == ('suggest_post'))    \n",
        "def callback_suggest_post(call):\n",
        "  bot.send_message(call.message.chat.id, 'Огромное спасибо за стремление сделать свой вклад в развитие канала. Поделитесь вашей идеей:')\n",
        "  users[call.from_user.id] = 'предложить пост'\n",
        "\n",
        "\n",
        "@bot.callback_query_handler(func=lambda call: call.data == ('bug_report'))    \n",
        "def callback_bug_report(call):\n",
        "  bot.send_message(call.message.chat.id, 'Мы умеем признавать свои ошибки и очень рады вашему стремлению помочь. Укажите, пожалуйста, пост и место где вы увидели ошибку:')\n",
        "  users[call.from_user.id] = 'указать на ошибку'\n",
        "\n",
        "\n",
        "@bot.callback_query_handler(func=lambda call: call.data == ('send_msg'))    \n",
        "def callback_send_msg(call):\n",
        "  bot.send_message(call.message.chat.id, 'Мы всегда рады любой обратной связи! Оставьте ваше сообщение:')\n",
        "  users[call.from_user.id] = 'написать сообщение'\n",
        "\n",
        "\n",
        "bot.infinity_polling()"
      ],
      "metadata": {
        "id": "91aFxjgEz_qa"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}