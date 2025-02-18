from django import forms
from .models import Booking_Table

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking_Table
        fields = ['name', 'choice_table', 'choice_event', 'date', 'time', 'number_of_people', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'number_of_people': forms.NumberInput(attrs={
                'type': 'number', 'min': 1, 'max': 12, 'required': True
            }),
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Добавьте комментарий...'}),
        }
