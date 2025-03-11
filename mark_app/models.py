from django.db import models
from auth_app.models import User
from django.utils import timezone

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish_rating = models.PositiveIntegerField(default=0)
    service_rating = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.dish_rating} / {self.service_rating}"
