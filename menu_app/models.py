from django.db import models
from auth_app.models import User
from choice_app.models import Dish_Category

class Dishes(models.Model): 
    title = models.CharField(max_length=500)
    description = models.TextField()
    choice = models.ForeignKey(Dish_Category, on_delete=models.CASCADE, related_name='dishes', null=True, blank=True)
    gram = models.CharField(max_length=4)
    price = models.CharField(max_length=4)
    photo = models.ImageField(upload_to="photos_for_food_media/", blank=True, null=True)
    
    def __str__(self):
        return self.title
    '''
        def save(self, *args, **kwargs):
        """
        Перед збереженням переконуємося, що choice містить лише цифри.
        Якщо ні, просто не зберігаємо.
        """
        if self.gram.isdigit():  # Перевіряємо, чи тільки цифри
            super().save(*args, **kwargs)
            
        if self.price.isdigit():  # Перевіряємо, чи тільки цифри
            super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    #def get_absolute_url(self):
        #return reverse('do-task-detail', kwargs={'pk': self.pk}
    '''