from account.models import *
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['role']
