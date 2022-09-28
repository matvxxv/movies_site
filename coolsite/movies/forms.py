from django import forms
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
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'content_source':forms.TextInput(attrs={"class": 'form-input'}),
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