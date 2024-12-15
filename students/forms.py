from django import forms
from .models import *

import logging

logger = logging.getLogger(__name__)


class MatricNumberForm(forms.Form):
    matric_number = forms.CharField(max_length=9)


class StudentRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match.')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_image', 'phone_number']
