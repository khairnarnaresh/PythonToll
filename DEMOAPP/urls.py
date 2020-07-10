from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show , name="Home page"),
    path('', views.hi, name="Home page"),
]