from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               max_length=20,
                               validators=[MinLengthValidator(3, "Username must be at least 3 characters long.")])

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                                max_length=20,
                                label='',
                                validators=[MinLengthValidator(6, 'Password must be at least 6 characters long.')])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
                                label='', )

    def clean(self):
        cleaned_data = super().clean()
        password2 = self.data.get('password2')

        if len(password2) < 6:
            self.add_error('password2', '')

        return cleaned_data

    class Meta:
        model = User
        fields = ("username", "password1")
        # fields = '__all__'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
