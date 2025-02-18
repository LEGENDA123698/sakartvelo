from django import forms
from .models import Dishes


class DishForm(forms.ModelForm):
    class Meta:
        model = Dishes
        fields = ['title', 'description', 'choice', 'gram', 'price', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'choice': forms.Select(attrs={'class': 'form-control'}),
            'gram': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '9999'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '9999'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
