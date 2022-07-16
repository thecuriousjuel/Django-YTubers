print('-'*20, __file__, '-'*20)

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'webpages/home.html')


def login(request):
    return render(request, 'webpages/login.html')


def register(request):
    return render(request, 'webpages/register.html')


def about(request):
    return render(request, 'webpages/about.html')

