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
from utils.decarators import get_member
from django.utils.translation import gettext_lazy as _, activate



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
    query.edit_message_text(str(_("Ismingizni kiriting: ")))
    return state.GET_NAME

@get_member
def get_name(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    tg_user.name = update.message.text
    tg_user.save()
    update.message.reply_text(str(_("enter your phone number")), reply_markup=get_phone_number_button())

    return state.GET_NAME




















#commands functions
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Help!')

def topusers_command(update: Update, context: CallbackContext):
    update.message.reply_text('Top users!')

def adminpanel_command(update: Update, context: CallbackContext):
    update.message.reply_text('Admin panel!')

def contact_admin_command(update: Update, context: CallbackContext):
    update.message.reply_text('Contact admin!')

def settings_command(update: Update, context: CallbackContext):
    update.message.reply_text('Settings!')

def lang_command(update: Update, context: CallbackContext):
    update.message.reply_text('Language!')

def my_groups_command(update: Update, context: CallbackContext):
    update.message.reply_text('My groups!')

def groups_statistic_command(update: Update, context: CallbackContext):
    update.message.reply_text('Groups statistic!')

def send_ads_command(update: Update, context: CallbackContext):
    update.message.reply_text('Send ads!')

def add_admin_command(update: Update, context: CallbackContext):
    update.message.reply_text('Add admin!')