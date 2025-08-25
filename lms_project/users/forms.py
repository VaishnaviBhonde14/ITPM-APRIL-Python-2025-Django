from django import forms
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser     # Replace with your user model
        fields = ['email', 'role', 'password']
        widgets = {'password': forms.PasswordInput()}

