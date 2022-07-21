from django import forms
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','email','username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'strong password'}),
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
        }