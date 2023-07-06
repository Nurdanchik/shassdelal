# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import (
#     CallbackContext,
#     Updater,
#     PicklePersistence,
#     MessageHandler,
#     CallbackQueryHandler,
#     Filters,
#     CommandHandler
# )
# from cred import TOKEN
# from menu import main_menu_keyboard,course_menu_keyboard
# from key_buttons import tele_button

# def start(update:Update, context: CallbackContext):
#     update.message.reply_text(
#         f"Welcome {update.effective_user.username}",
#         reply_markup=main_menu_keyboard()
#     )
# def o_nas(update:Update, context: CallbackContext):
#     update.message.reply_text(
#         """You'va picked information of us button.We are one of the best IT courses in KG.
#         Statistic says that one of 100 studnts here passes to good IT companies.To the
#         best students we guarantilly give a chance to work here.Working here you are taking 
#         very good experience that gives you a chance to progress from 0 to junior,then probably
#         to middle level.'As a student that used to study here I can say it worthes to study here' 
#         - says almost every second student here.It costs 16000 soms,yeah,not small payment,but 
#         it worthes,believe us!""",
#         reply_markup=main_menu_keyboard()
#     )
# ONAS = tele_button[0]

# def resive_course_menu(update:Update, context: CallbackContext):
#     update.message.reply_text(
#         f"Viberite kurs",
#         reply_markup=course_menu_keyboard()
#     )

# COURSE_MENU = tele_button[1]
    

# updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(MessageHandler(
#     Filters.regex(COURSE_MENU),
#     resive_course_menu
# ))
# updater.dispatcher.add_handler(MessageHandler(
#     Filters.regex(ONAS),
#     resive_course_menu
# ))
# updater.start_polling()
# updater.idle()
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    Filters,
    CommandHandler
)
from cred import TOKEN
from menu import main_menu_keyboard, course_menu_keyboard
from key_buttons import tele_button
from key_buttons import button

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Welcome {update.effective_user.username}",
        reply_markup=main_menu_keyboard()
    )

def back(update: Update, context: CallbackContext):
      update.message.reply_text(
        """Okey!You're sent back!""",
        reply_markup=main_menu_keyboard()
    )
BACKAT = button[3]
      
def o_nas(update: Update, context: CallbackContext):
    update.message.reply_text(
        """You've picked the 'Information of Us' button. We are one of the best IT courses in KG.
        Statistics show that one out of 100 students here gets the opportunity to work in good IT companies.
        For the best students, we guarantee a chance to work here. Working here provides valuable experience
        that allows you to progress from a beginner to a junior level, and potentially to a middle level.
        As a student who has studied here, I can confidently say that it's worth studying here.
        The cost of the course is 16,000 soms. Yes, it's not a small investment, but it's definitely worth it!""",
        reply_markup=main_menu_keyboard()
    )
def gde_mi(update: Update, context: CallbackContext):
        update.message.reply_text(
        """https://go.2gis.com/lccmx7
           above is our location in 2gis!
           but if you wonder about our certain location:
           ​Ибраимова, 115/1,Bishkek.""",
        reply_markup=main_menu_keyboard()
    )
def pythoninf(update: Update, context: CallbackContext):
        update.message.reply_text(
"""Профессия Python-разработчик
На Python пишут веб-приложения и нейросети, проводят научные вычисления и автоматизируют процессы.
Язык просто выучить, даже если вы никогда не программировали. На курсе вы создадите Telegram-бота,
полноценный магазин и аналог популярной соцсети для портфолио, а Центр карьеры поможет найти
работу Python-разработчиком.""",
        reply_markup=course_menu_keyboard()
    )
def javainf(update: Update, context: CallbackContext):
        update.message.reply_text(
"""Онлайн-курс 'Инженер по тестированию'

Обучение на русском языке

Получите востребованную профессию инженера по тестированию и навыки для тестирования мобильных и веб-приложений.

На программе изучите основы ручного и автоматизированного тестирования, научитесь быстро находить баги,
разрабатывать тест-кейсы, работать с баг-трекинговыми системами, создавать эффективные тестовые 
сценарии. Вы также изучите основы программирования, необходимые для написания автотестов и настройки
систем автоматизированного тестирования. И, если захотите, сможете продолжить развиваться в программировании.""",
        reply_markup=course_menu_keyboard()
    )
def uiuxinf(update: Update, context: CallbackContext):
        update.message.reply_text(
"""Профессия Художник компьютерной графики
Вы узнаете, как создавать арт-проекты для игр, кино и рекламы. 
Научитесь делать уникальный визуал, даже если у вас нет опыта в компьютерной графике. 
Опытный CG-художник будет курировать вас и даст обратную связь.
Добавите в портфолио 20 работ — сможете устроиться в студию, работать
на фрилансе или стать NFT-художником.""",
        reply_markup=course_menu_keyboard()
    )       
UIUXBEK = button[2]
JAVABEK = button[1]
PYTHON = button[0]

def resive_course_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Viberite kurs",
        reply_markup=course_menu_keyboard()
    )
COURSE_MENU = tele_button[1]
ONAS = tele_button[0]
 
updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ONAS),
    o_nas
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_MENU),
    resive_course_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    pythoninf
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JAVABEK),
    javainf
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(UIUXBEK),
    uiuxinf
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACKAT),
    back
))
updater.start_polling()
updater.idle()


