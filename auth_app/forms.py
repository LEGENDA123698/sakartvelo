from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['place_of_residence', 'home', 'apartment']
        widgets = {
            'home': forms.NumberInput(attrs={'min': 1, 'max': 999}),
            'apartment': forms.NumberInput(attrs={'min': 1, 'max': 9999}),
        }