from django import forms
from .models import Dish_Category

class DishCategoryForm(forms.ModelForm):
    class Meta:
        model = Dish_Category
        fields = ['dish']
        widgets = {
            'dish': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва категорії'}),
        }
        labels = {
            'dish': ''
        }
