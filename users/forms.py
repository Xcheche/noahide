from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password1',
            'password2': 'Confirm Password'
        }
