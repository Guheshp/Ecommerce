from django import forms
from . models import Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.forms.widgets import PasswordInput, TextInput, EmailInput

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

