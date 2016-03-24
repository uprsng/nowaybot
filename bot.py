# -*- coding: utf-8 -*-
import config
import telebot
import time
import random

def listener(messages):
    msg = ["Боля", "Сложна", "Кек", "Хех", "Мда", "Ээээ?", "Правда потом весь желудок выпердим и кишки", "Зез", "Мем", "ХЕХ", "Шо дел"]
    for m in messages:
        if m.content_type == 'text':
            bot.send_message(m.chat.id, random.choice(msg))

if __name__ == "__main__":
    bot = telebot.TeleBot(config.token)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)    
    while True:
        time.sleep(200)
