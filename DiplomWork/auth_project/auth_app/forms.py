from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=100, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(label='Пароль', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Проверка на существование пользователя
        if username and password:
            if not User.objects.filter(username=username).exists():
                raise forms.ValidationError(f"Пользователь {username} не найден.")

            user = authenticate(username=username, password=password, backend='django.contrib.auth.backends.ModelBackend')
            if user is None:
                raise forms.ValidationError("Неверный пароль.")
            else:
                cleaned_data['user'] = user  # Сохраняем пользователя в cleaned_data

        return cleaned_data


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя',
                               max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Введите имя пользователя'
                               }))
    email = forms.EmailField(label='Email',
                             max_length=100, required=True,
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'Введите email'
                             }))
    password = forms.CharField(label='Пароль',
                               min_length=8, max_length=100,
                               required=True,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Введите пароль'
                               }))
    confirm_password = forms.CharField(label='Подтверждение пароля',
                                       min_length=8, max_length=100,
                                       required=True,
                                       widget=forms.PasswordInput(attrs={
                                           'placeholder': 'Повторите пароль'
                                       }))

    class Meta:
        model = User
        fields = ['username', 'email']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"Пользователь {username} уже существует.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(f"Пользователь с {email} уже существует.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Пароли не совпадают.")
        return cleaned_data