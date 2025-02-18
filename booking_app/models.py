from django.db import models
from auth_app.models import User
from choice_app.models import Table_Category, Event_Category



class Booking_Table(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    choice_table = models.ForeignKey(Table_Category, on_delete=models.CASCADE)
    choice_event = models.ForeignKey(Event_Category, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
