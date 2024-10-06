from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Введите Email',
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
                             )
    username = forms.CharField(label='Введите Логин',
                               required=True,
                               help_text='Нельзя вводить символы: @, /, _',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
                               )
    password1 = forms.CharField(label='Введите пароль',
                                required=True,
                                help_text='Пороль не должен быть маленьким',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пороль'})
                                )
    password2 = forms.CharField(label='Подтвердите пароль',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пороль'})
                                )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.Form):
    email = forms.EmailField(label='Введите Email',
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
                             )
    username = forms.CharField(label='Введите Логин',
                               required=True,
                               help_text='Нельзя вводить символы: @, /, _',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
                               )
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.Form):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False
        )
    class Meta:
        model = Profile
        fields = ['img']