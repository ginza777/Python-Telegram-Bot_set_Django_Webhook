from django.conf import settings
import os
from queue import Queue
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler, PicklePersistence, CallbackQueryHandler, \
    MessageHandler, Filters
from .views import *
def setup_group(token):
    bot = Bot(token=token)
    queue = Queue()
    # create the dispatcher
    if not os.path.exists(os.path.join(settings.BASE_DIR, "media", "state_record")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media", "state_record"))
    dp = Dispatcher(bot, queue, workers=4, use_context=True, persistence=PicklePersistence(
        filename=os.path.join(
            settings.BASE_DIR, "media", "state_record", "conversationbot"
        )
    ),  # to store member state
                    )

    states = {
        # you can add more states here

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
    dp.add_handler(conversation_handler)
    return dp