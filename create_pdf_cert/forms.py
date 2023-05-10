from django import forms
from .models import Cert

class InputInfoForm(forms.ModelForm):
    name  = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'name',
        })
    )

    course  = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'course',
        })
    )

    class Meta:
        model = Cert
        fields = ('name', 'course')

