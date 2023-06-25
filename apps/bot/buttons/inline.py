from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from django.utils.translation import gettext_lazy as _
from core.settings.base import LANGUAGES
def get_language_button():
    buttons = [
        [
            InlineKeyboardButton(str(_("🇺🇿 O'zbekcha")), callback_data='uz'),
            InlineKeyboardButton(str(_("🇷🇺 Русский")), callback_data='ru'),
            InlineKeyboardButton(str(_("🇺🇸 English")), callback_data='en'),
        ]
    ]

    return InlineKeyboardMarkup(buttons)

def get_position_button():
    buttons = [
        [
            InlineKeyboardButton(str(_("Button1")), callback_data='button1'),
            InlineKeyboardButton(str(_("Button2")), callback_data='button2'),
        ]
    ]
    return InlineKeyboardMarkup(buttons)





#visitor


