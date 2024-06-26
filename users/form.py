from django import forms 
from .models import Users
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model=Users
        fields=['image', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets={
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',}),
            'username': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.TextInput(attrs={'class': 'form-control',}),
            'password1': forms.TextInput(attrs={'class': 'form-control',}),
            'password2': forms.TextInput(attrs={'class': 'form-control',}),
            }

        
class LogInForm(UserCreationForm):
    class Meta:
        model=Users
        fields=['username','password']
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control',}),
            'password': forms.TextInput(attrs={'class': 'form-control',}),    
            }