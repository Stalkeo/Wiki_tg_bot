import telebot
import random
from telebot import types
# Загружаем список интересных фактов
f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('compliments.txt', 'r', encoding='UTF-8')
compliments  = f.read().split('\n')
f.close()
# Создаем бота
bot = telebot.TeleBot('5694228118:AAE6rU2EadQ5BL2NIlj-9QxhkQPCWWKwtpY')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Комплимент")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Чтоб получить комплимент или узнать о себе факт, используй кнопки ниже:',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Комплимент':
            answer = random.choice(compliments)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)