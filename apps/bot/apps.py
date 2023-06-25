import requests.exceptions
from django.apps import AppConfig
from django.conf import settings
import telegram
import django.core.exceptions


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bot'

    def ready(self):
        try:
            bot_token = settings.BOT_TOKEN
            webhook_url = settings.WEBHOOK_URL
            if bot_token and webhook_url:
                bot = telegram.Bot(token=bot_token)
                bot.set_webhook(f"{webhook_url}/bot/handle_telegram_webhook/")
                print("Webhook set successfully for bot: {}".format(bot.get_me().username))
            else:
                print("Please set BOT_TOKEN and WEBHOOK_URL in settings.py to run the bot")
        except telegram.error.RetryAfter:
            pass
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your internet connection")
        except django.core.exceptions.ImproperlyConfigured:
            print("Improperly configured. Please check your settings")
        except telegram.error.Unauthorized:
            print("Unauthorized. Please check your bot token")
        except telegram.error.InvalidToken:
            print("Invalid token. Please check your bot token")
