from django.urls import path
from .views import *

urlpatterns = [
    path('', MoviesHome.as_view(), name = 'home'),
    path('about/', about, name = 'about'),
    path('addpage/', addpage, name = 'add_page'),
    path('login/', login, name = 'login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name = 'post')
]