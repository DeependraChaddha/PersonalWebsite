from django.urls import path
from . import views

urlpatterns=[
    path('', views.home)#when homepage is called(given by empty string '') call the function home in views.py
]