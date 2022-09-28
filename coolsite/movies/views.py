from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import request
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import *
from .forms import AddPostForm

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Предложить статью', 'url_name': 'add_page'},
        {'title': 'Войти', 'url_name': 'login'}]


class MoviesHome(ListView):
    model = Movies
    template_name = 'Movies/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['prod_selected'] = 0
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


class ShowPost(DetailView):
    model = Movies
    context_object_name = 'post'
    template_name = 'Movies/post.html'
    slug_url_kwarg = 'post_slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f'{context["post"]}'
        context['text1'] = context['post'].content.split('\r\n\r\n')[0:3]
        context['text2'] = context['post'].content.split('\r\n\r\n')[3:]
        return context


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'Movies/about.html', context=context)

# class AddPage(CreateView):
#     form_class = AddPostForm
#     template_name = 'Movies/addpage.html'
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Добавление статьи'
#         return context

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    context = {
        'form': form,
        'menu': menu,
        'title': 'Добавление статьи',
    }

    return render(request, 'Movies/addpage.html', context=context)

def login(request):
    ...

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

