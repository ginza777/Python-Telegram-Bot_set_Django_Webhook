from telegram import KeyboardButton, ReplyKeyboardMarkup
from django.utils.translation import gettext_lazy as _

def get_phone_number_button():
    con_keyboard = KeyboardButton(text=str(_("send_contact")), request_contact=True)
    return ReplyKeyboardMarkup([[con_keyboard]],resize_keyboard=True,one_time_keyboard=True)
