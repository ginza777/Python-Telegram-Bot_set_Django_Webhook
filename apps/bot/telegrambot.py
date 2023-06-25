import logging
from django.conf import settings
from telegram import Update, Bot
from telegram.ext import CallbackContext
from django.utils.translation import gettext_lazy as _, activate
from apps.bot import models
from utils.decarators import get_member
from .buttons.inline import *
from .buttons.keyboard import get_phone_number_button
from .state import state

logger = logging.getLogger(__name__)
bot = Bot(token=settings.BOT_TOKEN)


@get_member
def start(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    """Send a message when the command /start is issued."""
    update.message.reply_text(str(_("hello guys")), reply_markup=get_language_button())

    return state.GET_LANGUAGE


@get_member
def get_language(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    tg_user.language = query.data
    context.user_data['language'] = query.data
    tg_user.save()
    activate(tg_user.language)
    query.edit_message_text(str(_("who are you?")), reply_markup=get_position_button())

    return state.ANOTHER

