from django.contrib.admin.templatetags.admin_list import pagination
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import request
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import *
from .forms import AddPostForm, RegisterUserForm, LoginUserForm
from .utils import *


# DataMixin в utils.py
# Формируем страницу с постами
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
        # query = self.request.GET.get('q')
        # if query:
        #     results = self.model.objects.filter(Q(name__icontains = query)|Q(prod__name__icontains = query))
        #     if results:
        #         return results
        #     else:
        #         return redirect('nothing')
        # else:
        return Movies.objects.filter(is_published = True)


def search(request):
    try:
        query = request.GET.get('q')
        results = Movies.objects.filter(Q(name__icontains=query) | Q(prod__name__icontains=query) & Q(is_published = True))
        context = {'menu': menu,'posts': results, 'q': query, 'title': query}
        return render(request, 'Movies/index.html', context=context)
    except KeyError:
        return HttpResponseNotFound('<h1>Page not found</h1>')

# Страница с конкретным фильмом (Пост)
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

# Страница "О сайте"
def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'Movies/about.html', context=context)


# Страница с формой добавления статьи
class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'Movies/addpage.html'
    success_url = reverse_lazy('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context


# Страница с формой регистрации
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

# Страница с входом в аккаунт
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

# Страница, появляющаяся после успешного добавления статьи через addpage
def success_page(request):
    context ={
        'menu': menu,
        'title': 'Спасибо!',
    }
    return render(request, 'Movies/success_add_page.html', context=context)


# Выход из аккаунта

def logout_func(request):
    logout(request)
    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

