from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from classifications.models import Category


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'data-id': 1, 'style': 'color: red', 'type': 'text'}))
    message = forms.CharField(widget=forms.Textarea)
