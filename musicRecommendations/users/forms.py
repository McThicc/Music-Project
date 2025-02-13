from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200, 
        required=True,
        help_text=None,
        label='Email'
    )
    username = forms.CharField(
        max_length=16, 
        required=True,
        help_text=None,
        label='Username'
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text=None,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        help_text=None,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')