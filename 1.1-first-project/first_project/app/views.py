from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = None
    msg = f'Текущее время: {datetime.now()}'

    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages,
        'text': msg
    }
    return render(request, template_name, context)


def workdir_view(request):

    file_list = listdir(path='.')

    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time')
    }

    context = {
        'pages': pages,
        'file_list': file_list
    }
    return render(request, template_name, context)
