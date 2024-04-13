from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import User  # Assuming your custom user model is in the same app


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter Username",
        "class": "form-control"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "example@gmail.com",
        "class": "form-control"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter Password",
        "class": "form-control"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat Password",
        "class": "form-control"
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter Username"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter Password"
    }))

# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
# from django import forms
#
# from .models import Profile
#
#
# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]
#
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         "placeholder": "Enter Username",
#         "class": "form-control"
#     }))
#
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         "placeholder": "example@gmail.com",
#         "class": "form-control"
#     }))
#
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         "placeholder": "Enter Password",
#         "class": "form-control"
#     }))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         "placeholder": "Repeat Password",
#         "class": "form-control"
#     }))
#
#
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control",
#         "placeholder": "John Doe"
#     }))
#
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         "class": "form-control",
#         "placeholder": "Enter Password"
#     }))
#
