from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

from .validators import validate_username


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        max_length=20,
        validators=[
            validate_username,
            # UnicodeUsernameValidator(message="Enter a valid username.")
        ]
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        ),
        max_length=20,
        label='',
        validators=[MinLengthValidator(6, 'Password must be at least 6 characters long.')]
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password'}
        ),
        label='',
    )

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        if username:
            cleaned_data['slug'] = slugify(username)

        password2 = self.data.get('password2')
        if len(password2) < 6:
            self.add_error('password2', '')

        return cleaned_data

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'}
        )
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        )
    )

    error_messages = {
        'invalid_login': "Invalid username or password!",
    }

    def clean_username(self):
        return self.cleaned_data['username'].lower()


class UsernameChangeForm(UserChangeForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        validators=[validate_username]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
        self.fields['password'].label = ''

    class Meta:
        model = User
        fields = ('username',)


class AccountPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'

    class Meta:
        model = User
