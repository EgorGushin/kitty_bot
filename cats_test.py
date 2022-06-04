import os
import requests  # Импортируем библиотеку для работы с запросами

from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
token_env = os.getenv('TOKEN')
bot = Bot(token=token_env)
# Адрес API сохраним в константе
chat_id = 305734921
URL = 'https://api.thecatapi.com/v1/images/search'  
# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()

# Рассмотрим структуру и содержимое переменной response
# print(response)

# Посмотрим, какого типа переменная response
# print(type(response))

# response - это список. А какой длины?
# print(len(response))

# Посмотрим, какого типа первый элемент
random_cat_url = response[0].get('url')
bot.send_photo(chat_id, random_cat_url)