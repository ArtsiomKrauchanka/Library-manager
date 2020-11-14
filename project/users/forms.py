from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, label='Your name')
    last_name = forms.CharField(max_length=150, label='Your last name')
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']