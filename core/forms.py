from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . import models


class CustomUserForm(UserCreationForm):
    pass