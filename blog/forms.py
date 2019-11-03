from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import user_registrated
from django import forms
from django.forms.widgets import PasswordInput
from .models import AdvUser


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Email address")
    password1 = forms.CharField(label="Password", widget=PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label="Password", widget=PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введённые пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)
        else:
            return self.cleaned_data


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm, isinstance=user)
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password', 'password2',
                  'first_name', 'last_name', 'send_messages')