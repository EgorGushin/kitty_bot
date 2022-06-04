import logging
import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater, Filters, MessageHandler
from telegram import ReplyKeyboardMarkup
import requests


load_dotenv()
token_env = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

URL_CAT = 'https://api.thecatapi.com/v1/images/search'
URL_DOG = 'https://api.thedogapi.com/v1/images/search'

def get_new_image_cat():
    try:
        response = requests.get(URL_CAT)
    except Exception as error:
        logging.error(f'Ошибка в get_new_image_cat() при запросе к основному API: {error}')
        new_url = URL_DOG
        response = requests.get(new_url)
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat

def get_new_image_dog():
    try:
        response = requests.get(URL_DOG)
    except Exception as error:
        logging.error(f'Ошибка в get_new_image_dog() при запросе к основному API: {error}')
        new_url = URL_CAT
        response = requests.get(new_url)
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat

def new_cat(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id, 
                             text=f'{name}, посмотри, какого котика я нашел')
    context.bot.send_photo(chat.id, get_new_image_cat())

def new_dog(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id, 
                             text=f'{name}, посмотри, какого пёсика я нашел')
    context.bot.send_photo(chat.id, get_new_image_dog())

def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение 
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')

def start(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat'], ['/newdog']],
                                 resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id, 
                             text=f'Привет, {name}. '
                             f'Нажми на кнопку и я пришлю тебе котика или пёсика.',
                             reply_markup=button)


# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
def main():
    updater = Updater(token=token_env)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(CommandHandler('newdog', new_dog))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
    updater.start_polling()
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()