import logging
import settings
import ephem
import importlib
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Будем записывать отчет о работе бота в файл bot.log
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {
    'username': settings.PROXY_USERNAME,
    'password': settings.PROXY_PASSWORD
    }
}

def get_constellation(update, context):
    planet = update.message.text.split()[-1].title()
    user = ephem.Observer()
    
    try:
        if planet == 'Earth':
            update.message.reply_text(f'Cannot get constellation of {planet}')
        else:
            planet_class = getattr(ephem, planet)
            planet_compute = planet_class(user.date)
            constellation = ephem.constellation(planet_compute)[-1]
            update.message.reply_text(f'{planet.title()} today is in the {constellation} constellation')
    except AttributeError:
        update.message.reply_text(f'{planet} is not a valid planet')

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, get_constellation))

    logging.info("Бот стартовал")

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == "__main__":
    main()
