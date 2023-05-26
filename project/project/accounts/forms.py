from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               validators=[MinLengthValidator(3, "Username must be at least 3 characters long.")])

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                                max_length=20,
                                label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
                                max_length=20,
                                label='')

    class Meta:
        model = User
        fields = ("username", "password1")
        # fields = '__all__'
