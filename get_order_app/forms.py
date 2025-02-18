from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = ResultSolution
        fields = ['comment', 'delivery_date', 'delivery_time']
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
            'delivery_time': forms.TimeInput(attrs={'type': 'time'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
        
class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['name']
