from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, label='Your name')
    last_name = forms.CharField(max_length=150, label='Your last name')
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    favourite_book = forms.CharField(required=False)
    favourite_genre = forms.CharField(required=False)
    mobile_phone = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['image', 'favourite_book', 'favourite_genre', 'mobile_phone']
