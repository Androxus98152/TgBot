import pydub as pydub
import telebot
from pydub import AudioSegment
import urllib
import speech_recognition


# class SpeechRecognition:
#     pass


# Здесь нужно вставить токен, который дал BotFather при регистрации
# Пример: token = '2007628239:AAEF4ZVqLiRKG7j49EC4vaRwXjJ6DN6xng8'
token = '6212964467:AAFDzjpCIWXH-6oII3KKIJRrDMn1E99HylA'

# В этой строчке мы заводим бота и даем ему запомнить токен
bot = telebot.TeleBot(token)

# Пишем первую функцию, которая отвечает "Привет" на команду /start
# Все функции общения приложения с ТГ спрятаны в функции под @
@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, 'Рад видеть на моем первом проекте')

# Запускаем бота. Он будет работать до тех пор, пока работает ячейка (крутится значок слева).
# Остановим ячейку - остановится бот
bot.polling()


def oga2wav(filename):
    # Переименование формата: 'sample.oga' -> 'sample.wav'
    new_filename = ...
    # Читаем файл с диска с помощью функции AudioSegment.from_file()
    audio = ...
    # Экспортируем файл в новом формате
    audio.export(..., format=...)
    # Возвратим в качестве результата функции имя нового файла
    return ...

url = "https://drive.google.com/uc?export=view&id=1aBZnHgsjg7XIVlvpYasOOJ8hurp7V6Ww"
filename = "skillbox_voice_sample.ogg"
urllib.request.urlretrieve(url, filename)