from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        JA = ("ja", "japanese")
        EN = ("en", "english")
        KR = ("kr", "korean")
    
    class CurrencyChoices(models.TextChoices):
        Won = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(max_length = 150, editable=False,)
    last_name = models.CharField(max_length = 150, editable=False,)
    name = models.CharField(max_length=150, default="",)
    avatar = models.ImageField(blank=True)
    is_host = models.BooleanField(default=False,)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices,)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices,)