# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """
    Extends Django's built-in UserCreationForm
    Adds email field
    """
    
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ["username", "email", "password","password2"]

class UserupdateForm(forms.ModelForm):
        """
        Allows updating basic user info
        """
    
    class Meta:
        model = User
        fields = ["username", "email"]