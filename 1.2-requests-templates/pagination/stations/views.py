from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpRequest
import csv


PAGE_SIZE = 7

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request: HttpRequest):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_num = int(request.GET.get("page", 1))

    bus_station_list = []
    with open(settings.BUS_STATION_CSV, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_station_list.append(row)

    paginator = Paginator(bus_station_list, PAGE_SIZE)
    page = paginator.get_page(page_num)

    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
