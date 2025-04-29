from django.db import models
from auth_app.models import User
from menu_app.models import Dishes

# заказ весь
class ResultSolution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(Dishes, through='OrderItem', related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    comment = models.TextField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_time = models.TimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

# Модель для связки конкретных блюд в заказе
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_items")
    order = models.ForeignKey(ResultSolution, on_delete=models.CASCADE, related_name='order_items')
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.dish.title} x {self.quantity}"
    
    

class Street(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

