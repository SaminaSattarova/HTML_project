# импорт необходимых библиотек
import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

BOT_TOKEN = '6106499169:AAEPS49EemyNOIsGbIPMvmTk2I3fuBGVKAk'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
    )

logger = logging.getLogger(__name__)

# кнопки
reply_keyboard = [['/developers', '/phones'],
                  ['/information_about_site', '/questions']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard_two = [['/how_long_we_make_this', '/how_does_it_cost'],
                      ['/for_what_it_need', '/another_questions'],
                      ['/back']]
markup_two = ReplyKeyboardMarkup(reply_keyboard_two, one_time_keyboard=False)


# функция ответа бота при его запуске и открытии клавиатуры с кнопками
async def start(update, context):
    await update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
         reply_markup=markup)


# функция ответа бота при введении /help
async def help(update, context):
    await update.message.reply_text(
        "Выберите один из предложенных вариантов вопроса.")


# функция ответа бота при нажатии на кнопку /back
async def back(update, context):
    await update.message.reply_text(
        "Что вас интересует?",
         reply_markup=markup)


# функция ответа бота при нажатии на кнопку /developers
async def developers(update, context):
    await update.message.reply_text(
        "Саттарова Самина и Гончарова Виктория 9Н")


# функция ответа бота при нажатии на кнопку /phones
async def phones(update, context):
    await update.message.reply_text("Самина Саттарова: +7(916)607-6766, "
                                    "Вика: +7(985)909-3310")


# функция ответа бота при нажатии на кнопку /information_about_site
async def information_about_site(update, context):
    await update.message.reply_text(
        "Функции и возможности: в нашем проекте, помимо регистрации и авторизации, "
        "пользователь сможет посмотреть общую информацию о нашем классе и классном руководителе. "
        "Можно будет опсмотреть информацию о различных поездках в интересные места. Плюс ко всему есть "
        "возможность узнать своих будущих одноклассников или просто ребят, обучающихся в нашем классе, "
        "узнать про них и о их увелечениях подробнее. А наш телеграм-бот ответит на все ваши вопросы.")


# функция ответа бота при нажатии на кнопку /questions и вывод второй клавиатуры с кнопками
async def questions(update, context):
    await update.message.reply_text(
        "Что именно вы хотите узнать?", reply_markup=markup_two)


# функция ответа бота при нажатии на кнопку /how_long_we_make_this
async def how_long_we_make_this(update, context):
    await update.message.reply_text(
        "Время написания: проект был дан нам примерно на три месяца. "
        "Большая часть времени - учебное, поэтому по будним дням проектом мы не занимались. "
        "В основном писали его в воскресенье, ведь это наш единственный выходной, а также целых 2 недели, "
        "пока были каникулы. Суммарно, помимо большого колиства сил, "
        "на данный сайт и бот ушло примерно 3 недели времени.")


# функция ответа бота при нажатии на кнопку /how_does_it_cost
async def how_does_it_cost(update, context):
    await update.message.reply_text(
        "По вопросам приобритения писать в личные сообщения, "
        "мы конечно можем договориться, но предвариьельно проект не продается")


# функция ответа бота при нажатии на кнопку /for_what_it_need
async def for_what_it_need(update, context):
    await update.message.reply_text(
        "Цели проекта: у данного проекта были две основные задачи. "
        "Во-первых, это небольшое хранилище памяти и воспоминаний о двух годах совместного обуения "
        "для всего нашего класса. Во-вторых, это отличный путеводитель в лицейскую жизнь для тех ребят, "
        "кто собирается поступать в данное учебное зпведение, а конкретнее в IT-класс, ведь можно интерактивно "
        "познакомиться с будущими одноклассниками и классным руководителем, а также узнать о всех плюсах и "
        "минусах обучения в нашем класе.")


# функция ответа бота при нажатии на кнопку /another_questions
async def another_questions(update, context):
    await update.message.reply_text(
        "По другим вопросам обращаться в лс")


# закрытие клавиатуры при введении /close_keyboard
async def close_keyboard(update, context):
    await update.message.reply_text(
        "Клавиатура с кнопками закрыта, напишите /open, чтобы вновь открыть её",
        reply_markup=ReplyKeyboardRemove()
        )


# открытие клавиатуры при введении /open_keyboard
async def open_keyboard(update, context):
    await update.message.reply_text(
        "Клавиатура с кнопками снова открыта",
        reply_markup=markup)


# запуск функций бота
def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("developers", developers))
    application.add_handler(CommandHandler("phones", phones))
    application.add_handler(CommandHandler("information_about_site", information_about_site))
    application.add_handler(CommandHandler("questions", questions))
    application.add_handler(CommandHandler("how_long_we_make_this", how_long_we_make_this))
    application.add_handler(CommandHandler("how_does_it_cost", how_does_it_cost))
    application.add_handler(CommandHandler("for_what_it_need", for_what_it_need))
    application.add_handler(CommandHandler("another_questions", another_questions))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("open", open_keyboard))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.run_polling()


if __name__ == '__main__':
    main()
