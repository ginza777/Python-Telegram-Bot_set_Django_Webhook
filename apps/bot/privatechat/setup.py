import os
from queue import Queue
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler, PicklePersistence, CallbackQueryHandler,MessageHandler, Filters
from .views import *

def setup_private(token):
    bot = Bot(token=token)
    queue = Queue()
    # create the dispatcher
    if not os.path.exists(os.path.join(settings.BASE_DIR, "media", "state_record")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media", "state_record"))
    dp = Dispatcher(bot, queue, workers=4, use_context=True, persistence=PicklePersistence(
        filename=os.path.join(
            settings.BASE_DIR, "media", "state_record", "conversationbot"
        )
    ))
    states = {
        state.GET_LANGUAGE: [CallbackQueryHandler(get_language, pattern='uz|ru|en'),],
        state.GET_NAME: [MessageHandler(Filters.text, get_name),],


    }
    entry_points = [CommandHandler('start', start), ]
    fallbacks = [
        MessageHandler(Filters.all, start),
    ]
    conversation_handler = ConversationHandler(
        entry_points=entry_points,
        states=states,
        fallbacks=fallbacks,
        persistent=True,
        name="conversationbot",
    )

    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help_command))
    dp.add_handler(CommandHandler('topusers',topusers_command))
    dp.add_handler(CommandHandler('adminpanel',adminpanel_command))
    dp.add_handler(CommandHandler('contact_admin',contact_admin_command))
    dp.add_handler(CommandHandler('settings',settings_command))
    dp.add_handler(CommandHandler('lang',lang_command))
    dp.add_handler(CommandHandler('my_groups',my_groups_command))
    dp.add_handler(CommandHandler('groups_statistic',groups_statistic_command))
    dp.add_handler(CommandHandler('send_ads',send_ads_command))
    dp.add_handler(CommandHandler('add_admin',add_admin_command))
    dp.add_handler(conversation_handler)

    return dp
