from django.contrib import admin
from.models import *

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'photo', 'slug', 'time_create', 'is_published', 'prod')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    search_fields = ('name', 'prod')
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}



class ProdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Movies, MoviesAdmin)
admin.site.register(Prods, ProdsAdmin)