from django import forms
from .models import CustomeUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomeUser     # Replace with your user model
        fields = ['email', 'role', 'password']
        widgets = {'password': forms.PasswordInput}