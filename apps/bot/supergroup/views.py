from telegram import Update, Bot
from telegram.ext import CallbackContext
from .state import state
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
bot = Bot(token=settings.BOT_TOKEN)
from apps.bot.buttons.inline  import *
from apps.bot.buttons.keyboard import get_phone_number_button
from apps.bot import models
from django.utils.translation import gettext_lazy as _, activate





def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    print('start sdcdsjndksnckjnkjdsncjnc' )
    update.message.reply_text(str(_("hello guys")))


