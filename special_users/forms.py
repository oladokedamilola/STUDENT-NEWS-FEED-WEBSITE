from django import forms
from .models import CreatorApplication

class CreatorApplicationForm(forms.ModelForm):
    class Meta:
        model = CreatorApplication
        fields = ['title', 'main_content']
        labels = {
            'title': 'Application Title',
            'main_content': 'Detailed Content',
        }
        widgets = {
            'main_content': forms.Textarea(attrs={'rows': 6, 'cols': 40, 'placeholder': 'Describe your application here...'}),
        }
