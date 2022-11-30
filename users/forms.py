from django import forms
from django.contrib.auth.models import User

from .models import Customer

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


class EditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('phone','address','pin_code')
        widgets = {
            'phone': forms.NumberInput(attrs={'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'placeholder': 'Address'}),
            'pin_code': forms.NumberInput(attrs={'placeholder': 'Pin Code'}),
        }