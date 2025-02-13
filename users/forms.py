from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class UserForm(UserCreationForm):
    captcha = CaptchaField()
    
    email = forms.EmailField(required=True)  # Ensure email is required

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']
    #     labels = {
    #         'username': 'Username',
    #         'email': 'Email',
    #         'password1': 'Password',  # More user-friendly label
    #         'password2': 'Confirm Password'
    #     }
