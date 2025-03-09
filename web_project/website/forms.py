from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_svg_image_form_field import SvgAndImageFormField

from . import models


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = models.Category
        exclude = []
        field_classes = {
            "icon": SvgAndImageFormField,
        }


class RegistrationForm(UserCreationForm):
    pass
