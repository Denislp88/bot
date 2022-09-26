import time
from telegram import Bot

chat_id = 123 #замените на свое значение, подробнее ниже
bot = Bot("5402596551:AAGguUw_3pWadyA8nxVVpiG24vUcpAv_Ezo")


def send_random_cat():
    url = f'https://cataas.com/cat?t=${time.time()}'
    bot.send_photo(chat_id, url)


def main() -> None:
    send_random_cat()
    print('Cat has been sent')


if __name__ == "__main__":
    main()