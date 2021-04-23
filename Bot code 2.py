# -*- coding: utf-8 -*-
# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('x')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки
oven_zod = ["Вот он, любитель оповещать всех в комментариях, что он первый. Не забудь сегодня сделать то же самое", "2"]
telec_zod = ["3", "4"]
bliznecy_zod = ["Когда ты уже поймешь, что мы не в театре, хватит примерять на себя разные роли. Тебе всё равно никто за это не похлопает", "6"]
rak_zod = ["7", "8"]
lev_zod = ["Обычно ты боишься людей под знаком Скорпион, сегодня будет не исключение", "11"]
deva_zod = ["11", "12"]
vesy_zod = ["Я б на твоем месте помолилась, чтоб тебя опять не притянуло к очередному Овну", "14"]
scorpion_zod = ["15", "16"]
strelec_zod = ["17", "18"]
kozerog_zod = ["Козерог - это диагноз", "20"]
vodoley_zod = ["21", "22"]
ryby_zod = ["23", "24"]
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, хочешь узнать свой гороскоп на сегодня? Выбери свой знак, я за пару секунд разложу карты и предскажу, что тебя ждет впереди")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac_oven')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac_telec')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac_bliznecy')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac_rak')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac_lev')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac_deva')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac_vesy')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac_scorpion')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac_strelec')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac_kozerog')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac_vodoley')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac_ryby')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac_oven": 
        # Формируем гороскоп
        msg = random.choice(oven_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_telec": 
        # Формируем гороскоп
        msg = random.choice(telec_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_bliznecy": 
        # Формируем гороскоп
        msg = random.choice(bliznecy_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_rak": 
        # Формируем гороскоп
        msg = random.choice(rak_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_lev": 
        # Формируем гороскоп
        msg = random.choice(lev_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_deva": 
        # Формируем гороскоп
        msg = random.choice(deva_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg) 
    if call.data == "zodiac_vesy": 
        # Формируем гороскоп
        msg = random.choice(vesy_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_scorpion": 
        # Формируем гороскоп
        msg = random.choice(scorpion_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_strelec": 
        # Формируем гороскоп
        msg = random.choice(strelec_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_kozerog": 
        # Формируем гороскоп
        msg = random.choice(kozerog_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_vodoley": 
        # Формируем гороскоп
        msg = random.choice(vodoley_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zodiac_ryby": 
        # Формируем гороскоп
        msg = random.choice(ryby_zod) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)