import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

BOT_TOKEN = '6106499169:AAEPS49EemyNOIsGbIPMvmTk2I3fuBGVKAk'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['/developers', '/phones'],
                  ['/information_about_site', '/questions']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )


async def help(update, context):
    await update.message.reply_text(
        "Выберите один из предложенных вариантов вопроса.")


async def developers(update, context):
    await update.message.reply_text(
        "Саттарова Самина и Гончарова Виктория 9Н")


async def phones(update, context):
    await update.message.reply_text("Самина: +7(916)607-6766, "
                                    "Вика: +7(985)909-3310")


async def information_about_site(update, context):
    await update.message.reply_text(
        "Время разработки ..., функции и возможности: ...")


async def questions(update, context):
    await update.message.reply_text(
        "Все вопросы можно задать в личных сообщениях по указанным выше номерам телефонов")


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("developers", developers))
    application.add_handler(CommandHandler("phones", phones))
    application.add_handler(CommandHandler("information_about_site", information_about_site))
    application.add_handler(CommandHandler("questions", questions))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.run_polling()


if __name__ == '__main__':
    main()