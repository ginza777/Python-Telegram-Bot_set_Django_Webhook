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
import time



def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text( str(_("@shoxnur2001  100 dollar qarz ber  ")),reply_markup=qarz_berish())

    return state.ANOTHER


def another(update: Update, context: CallbackContext):
    query = update.callback_query
    print(query.data)
    query.answer("oq tosh qora tosh qarz bermagan qo'toqbosh")
    query.edit_message_text(str(_("👍 1000 so'mdan akajonlar")))
    return state.ANOTHER