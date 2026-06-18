from django.db import models

# Create your models here.

class DailyQuote(models.Model):
    # Kun tartin raqami (1 dan 365 gacha)
    day_number = models.PositiveIntegerField(unique=True, help_text='Yilning nechanchi kuni (1-365)')
    # Iboraning o'zi
    text = models.TextField(verbose_name="Kun iborasi")

    def __str__(self):
        return f"{self.day_number}-kun iborasi"