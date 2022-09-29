import time
from telegram import Bot

chat_id = 141929465 #замените на свое значение, подробнее ниже
bot = Bot("5448621471:AAFJQxh9U1RWL21y2QT9utQB2h4QdZkiK-c")


def send_random_cat():
    url = f'https://cataas.com/cat?t=${time.time()}'
    bot.send_photo(chat_id, url)

    bot.send_photo(chat_id, photo=open('img/cat.jpg', 'rb'))   #берет фотку с директорий


def main() -> None:
    send_random_cat()
    print('Cat has been sent')



if __name__ == "__main__":
    main()