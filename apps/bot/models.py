from django.db import models


class Language(models.TextChoices):
    UZBEK = "uz", "Uzbek",
    RUSSIAN = "ru", "Russian",
    ENGLISH = "en", "English",


class TelegramProfile(models.Model):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, choices=Language.choices, default=Language.UZBEK,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.telegram_id}"


class Group(models.Model):
    group_id = models.PositiveBigIntegerField(unique=True)
    group_name = models.CharField(max_length=255, null=True)
    group_username = models.CharField(max_length=255, null=True, blank=True)
    group_language = models.CharField(max_length=255, choices=Language.choices, default=Language.UZBEK,null=True,blank=True)
    admin_id=models.PositiveBigIntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.group_name} {self.group_username} {self.group_id} {self.group_language}"

