import json
import os
from queue import Queue

from django.conf import settings
from django.http import JsonResponse

from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler, PicklePersistence, CallbackQueryHandler, \
    MessageHandler, Filters

from .state import state
from .telegrambot import *


def setup(token):
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
        state.GET_LANGUAGE: [
            CallbackQueryHandler(get_language, pattern='uz|ru|en'),
        ]
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


def handle_telegram_webhook(request):
    token = settings.BOT_TOKEN
    bot = Bot(token=token)
    update = Update.de_json(json.loads(request.body.decode('utf-8')), bot)
    dp = setup(token)
    try:
        if update.message.chat.type == 'private':
            dp.process_update(update)
    except Exception as e:
        dp.process_update(update)
    return JsonResponse({'status': 'ok'})


def set_telegram_webhook(request):
    token = settings.BOT_TOKEN
    bot = Bot(token=token)
    bot.set_webhook(f"{settings.WEBHOOK_URL}/bot/handle_telegram_webhook/")
    return JsonResponse({'status': 'ok'})
