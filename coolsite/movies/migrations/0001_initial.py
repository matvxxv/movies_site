# Generated by Django 4.0.6 on 2022-09-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Режиссеры',
                'verbose_name_plural': 'Режиссеры',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('name', models.CharField(max_length=255, verbose_name='Название фильма')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('content_photo_first', models.ImageField(null=True, upload_to='photos/content_photo/', verbose_name='Первое фото статьи')),
                ('content_photo_second', models.ImageField(null=True, upload_to='photos/content_photo/', verbose_name='Второе фото статьи')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Последнее редактирование')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('content_source', models.CharField(max_length=255, verbose_name='Источник')),
                ('prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movies.prods', verbose_name='Режиссер')),
            ],
            options={
                'verbose_name': 'Фильмы',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['time_create', 'name'],
            },
        ),
    ]
