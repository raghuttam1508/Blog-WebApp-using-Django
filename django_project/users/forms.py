from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()

    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]
