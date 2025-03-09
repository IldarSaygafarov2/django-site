from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_svg_image_form_field import SvgAndImageFormField

from . import models
from .models import CustomUser


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = models.Category
        exclude = []
        field_classes = {
            "icon": SvgAndImageFormField,
        }


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "phone_number",
            "avatar",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.EmailInput(attrs={"class": "form-control"}),
            "avatar": forms.FileInput(attrs={"class": "form-control"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser
