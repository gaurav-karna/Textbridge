from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    # Here is where all of the routes will be
    # in regards to the web application

    # public paths, open to everyone // self-explanatory
    path('', views.index, name='index'),
    path('login_home/', views.login_home, name='login_home'),
    path('register/', views.register, name='register'),
    path('register_failure/', views.register, name='register_failure'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('sms/', views.sms_api, name='sms_api')
]
