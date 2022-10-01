import re
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""
    Бот может здороваться на разных языках.
    Список поддерживаемых приветствий:
    - привет - русский
    - hello - английский
    - hola - испанский
    """)


def ru(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('привет')


def en(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('hello')


def es(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('hola')

def d(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('да')

def not_supported(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Приветствие "{update.message.text}" не поддерживается.')


def get_greeting_filter(greeting: str) -> BaseFilter:
    return Filters.regex(re.compile(f'^{greeting}$', re.IGNORECASE)) & Filters.update.message


def main() -> None:
    updater = Updater("5448621471:AAFJQxh9U1RWL21y2QT9utQB2h4QdZkiK-c")

    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('привет'), ru))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('hello'), en))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('hola'), es))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('да'), d))
    updater.dispatcher.add_handler(MessageHandler(Filters.update.message & Filters.text, not_supported))

    updater.start_polling()

    print('Started')

    updater.idle()


if __name__ == "__main__":
    main()