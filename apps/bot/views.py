import json
from django.http import JsonResponse
from telegram import Bot, Update
from apps.bot.privatechat.setup import setup_private
from apps.bot.supergroup.setup import setup_group
from django.conf import settings


def handle_telegram_webhook(request):
    token = settings.BOT_TOKEN
    bot = Bot(token=token)
    update = Update.de_json(json.loads(request.body.decode('utf-8')), bot)
    try:
        if update.message.chat.type == 'private':
            dp = setup_private(token)
            dp.process_update(update)
        elif update.message.chat.type == 'supergroup':
            dp = setup_group(token)
            dp.process_update(update)

    except Exception as e:
        if update.callback_query.message.chat.type == 'private':
            dp = setup_private(token)
            dp.process_update(update)
        elif update.callback_query.message.chat.type == 'supergroup':
            dp = setup_group(token)
            dp.process_update(update)

    return JsonResponse({'status': 'ok'})


def set_telegram_webhook(request):
    token = settings.BOT_TOKEN
    bot = Bot(token=token)
    bot.set_webhook(f"{settings.WEBHOOK_URL}/bot/handle_telegram_webhook/")
    return JsonResponse({'status': 'ok'})
