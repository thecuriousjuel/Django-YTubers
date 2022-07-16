print('-'*20, __file__, '-'*20)

from django.urls.resolvers import URLPattern
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about')
]

