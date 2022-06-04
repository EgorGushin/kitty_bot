from telegram import Bot

# Здесь укажите токен, 
# который вы получили от @Botfather при создании бот-аккаунта
bot = Bot(token='5305053035:AAHg-b2_mSGjOUVOJKH6pSU0livRCyzeMNU')
# Укажите id своего аккаунта в Telegram
chat_id = 154428177
text = 'Люблю Женьку-какашка' 
# Отправка сообщения
bot.send_message(chat_id, text) 