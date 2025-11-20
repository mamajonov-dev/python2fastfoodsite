from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['address', 'phone', 'qabul_qiluvchi']
