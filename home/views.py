from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Item

from home.utils import menu



data = {
    'title': 'Главная страница',
    'menu': menu,
}


@login_required
def index(request):
    items = Item.objects.all()
    data['items'] = items
    return render(request, 'home.html', context=data)


@login_required
def about(request):
    return render(request, 'about.html', context=data)


