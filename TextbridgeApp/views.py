from django.shortcuts import render, redirect
from twilio.rest import Client

# Create your views here.


def index(request):
    return render(request, "home.html", {})


def register(request):
    return render(request, "register.html", {})


def registration_success(request):
    return render(request, "registration_success.html", {})
