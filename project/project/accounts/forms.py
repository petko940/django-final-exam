from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
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


class UsernameChangeForm(UserChangeForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
        self.fields['password'].help_text = ''

    class Meta:
        model = User
        fields = ('username',)


class AccountPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = ''
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'
        self.fields['new_password2'].help_text = ''

    class Meta:
        model = User
