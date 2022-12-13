from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/see/', see, name="see"),
    path('home/',home, name="home"),
    path('home/che/', che, name="che"),
]
