from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
]