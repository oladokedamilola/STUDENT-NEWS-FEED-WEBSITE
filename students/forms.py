from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class StudentRegistrationForm(UserCreationForm):
    matric_number = forms.CharField(max_length=11, required=True)

    class Meta:
        model = Student
        fields = ('username', 'matric_number', 'password1', 'password2')

    def clean_matric_number(self):
        matric_number = self.cleaned_data.get('matric_number')
        student = Student.objects.filter(matric_number=matric_number).first()
        if not student:
            raise forms.ValidationError("Invalid matric number.")
        return matric_number

    def save(self, commit=True):
        user = super().save(commit=False)
        matric_number = self.cleaned_data.get('matric_number')
        student = Student.objects.get(matric_number=matric_number)
        user.matric_number = matric_number
        user.email = student.email
        if commit:
            user.save()
        return user
