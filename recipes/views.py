
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Lucas Trindade Langaro',
    })

def recipe(request,id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Lucas Trindade Langaro',
    })