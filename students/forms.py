# forms.py
from django import forms
from .models import Student

import logging

logger = logging.getLogger(__name__)


class MatricNumberForm(forms.Form):
    matric_number = forms.CharField(max_length=11)



class StudentRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Student
        fields = ['username', 'password', 'password_confirm', 'matric_number', 'faculty', 'department', 'phone_number', 'email', 'gender']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        matric_number = cleaned_data.get("matric_number")
        faculty = cleaned_data.get("faculty")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        if not matric_number:
            raise forms.ValidationError("Matric number is required.")

        if not faculty:
            raise forms.ValidationError("Faculty is required.")

        return cleaned_data

 
 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
