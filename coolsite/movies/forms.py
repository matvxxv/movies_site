from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    # Метод вызывается перед созданием полей формы
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prod'].empty_label = 'Режиссер не выбран'

    class Meta:
        model = Movies
        fields = ['name','slug' ,'title', 'content', 'photo', 'content_photo_first','content_photo_second','content_source', 'prod']  # __all__ - Кроме тех, что заполняются автоматически
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название фильма...'}),
            'slug': forms.TextInput(attrs={'class': 'form-input','placeholder':'URL...'}),
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Заголовок'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder': 'Текст статьи...'}),
            'content_source':forms.TextInput(attrs={"class": 'form-input','placeholder': 'Источник...'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Длина превышает 100 символов')

        return title

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 100:
            raise ValidationError('Длина превышает 100 символов')

        return name

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login_form', 'placeholder': 'Username...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login_form', 'placeholder': 'Password...'}))