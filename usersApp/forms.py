from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
