from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SpecialUser

class SpecialUserCreationForm(UserCreationForm):
    class Meta:
        model = SpecialUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        password_confirm = cleaned_data.get("password2")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
