from django.contrib import admin
from .models import TelegramProfile


# Register your models here.
@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','telegram_id']

