from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import request
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import *
from .forms import AddPostForm, RegisterUserForm, LoginUserForm
from .utils import *


class MoviesHome(DataMixin,ListView):
    paginate_by = 3
    model = Movies
    template_name = 'Movies/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Главная страница')
        context |= c_def
        return context

    # Добавить поиск по режиссеру

    def get_queryset(self):
        query = self.request.GET.get('search_film')
        if query:
            a = Movies.objects.filter(name__icontains = query)
            if a:
                return a
        else:
            return Movies.objects.filter(is_published = True)


class ShowPost(DataMixin,DetailView):
    model = Movies
    context_object_name = 'post'
    template_name = 'Movies/post.html'
    slug_url_kwarg = 'post_slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context['post'])
        context['text1'] = context['post'].content.split('\r\n\r\n')[0:3]
        context['text2'] = context['post'].content.split('\r\n\r\n')[3:]
        context |= c_def
        return context


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'Movies/about.html', context=context)

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'Movies/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'Movies/register.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Регистрация')
        context |= c_def
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'Movies/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Авторизация')
        context |= c_def
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_func(request):
    logout(request)
    return redirect('home')
def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

