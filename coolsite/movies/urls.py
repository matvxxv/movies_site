from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *
from coolsite import settings

urlpatterns = [
    path('', MoviesHome.as_view(), name = 'home'),
    path('search/', search, name='search'),
    path('about/', about, name = 'about'),
    path('addpage/', AddPage.as_view(), name = 'add_page'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name = 'post'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('logout/', logout_func, name='logout'),
    path('success/', success_page, name = 'success'),
]