from django.contrib import admin
from django.utils.safestring import mark_safe

from.models import *

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title','get_content' ,'get_html_photo', 'slug', 'time_create', 'is_published', 'prod')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    search_fields = ('name', 'prod')
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'title', 'content', 'photo','get_html_photo', 'content_photo_first', 'content_photo_second', 'is_published', 'prod', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=100>')
        # mark_safe - выключает экранирование тэгов

    get_html_photo.short_description = 'Миниатюра'
    def get_content(self, object):
        if object.content:
            return object.content[0:70:1]

    get_content.short_description = 'Текст статьи'
class ProdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Movies, MoviesAdmin)
admin.site.register(Prods, ProdsAdmin)