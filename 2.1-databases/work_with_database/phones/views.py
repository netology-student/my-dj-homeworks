from django.shortcuts import render, redirect
from django.http import HttpRequest

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request: HttpRequest):
    sort = request.GET.get('sort', 'name')

    if sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price').values()
    elif sort == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price').values()
    else:
        phone_objects = Phone.objects.all().order_by('name').values()

    template = 'catalog.html'
    context = {}
    context['phones'] = phone_objects
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    context = {}

    phone_objects = Phone.objects.filter(slug=slug)
    if len(phone_objects) != 0:
        context['phone'] = phone_objects[0]

    return render(request, template, context)
