from django.urls import path, include
from django.contrib import admin
from . import views
import django.contrib.auth
from django.conf import settings

urlpatterns = [
    # Here is where all of the routes will be
    # in regards to the web application

    # public paths, open to everyone // self-explanatory
    path('', views.index, name='index'),
    path('/register', views.register, name='register'),
    path('/register_failure', views.register, name='register_failure'),
    path('/parse_friend_list', views.parse_friend_list, name='parse_friend_list'),
]
