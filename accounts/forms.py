"""
Jordyn Kuhn
CIS 218
4-7-2024
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class DateInput(forms.DateInput):
    input_type = "date" 

class CustomUserCreationForm(UserCreationForm):
    """Custom User Creation Form"""
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "date_of_birth",
        )
        widgets = {
            "date_of_birth": DateInput(),
        }

class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""


    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "date_of_birth",
        )
        widgets = {
            "date_of_birth": DateInput(),
        }
        exclude = ('password',)