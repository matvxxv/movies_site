from django.db import models
from django.urls import reverse

class Movies(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    name = models.CharField(max_length=255, verbose_name='Название фильма')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    content_photo_first = models.ImageField(upload_to='photos/content_photo/', verbose_name='Первое фото статьи', null=True)
    content_photo_second = models.ImageField(upload_to='photos/content_photo/', verbose_name='Второе фото статьи', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее редактирование')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    prod = models.ForeignKey('Prods', on_delete=models.PROTECT, verbose_name='Режиссер', null=True)
    content_source = models.CharField(max_length=255, verbose_name='Источник')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug': self.slug})


class Prods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссеры'
        verbose_name_plural = 'Режиссеры'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('prod', kwargs = {'prod_slug': self.slug})