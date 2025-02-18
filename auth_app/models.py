from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    place_of_residence = models.CharField(max_length=500, blank=True)
    home = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(999)])
    apartment = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(9999)])

    def __str__(self):
        return self.username
    '''
        def save(self, *args, **kwargs):
        """
        Перед сохранением проверяем, что home и apartment содержат только цифры.
        Если нет, не сохраняем.
        """
        if self.home.isdigit() and self.apartment.isdigit():  # Проверяем оба поля
            super().save(*args, **kwargs)
    '''
        
    