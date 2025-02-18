from django.db import models

class Table_Category(models.Model): 
    number = models.CharField(max_length=5)

    def __str__(self):
        return self.number            
            
class Event_Category(models.Model): 
    event = models.CharField(max_length=30)
    
    def __str__(self):
        return self.event
    
class Dish_Category(models.Model): 
    dish = models.CharField(max_length=80)
    
    def __str__(self):
        return self.dish


class Street_Category(models.Model): 
    street = models.CharField(max_length=100)
    
    
    
    
