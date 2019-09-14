from django.shortcuts import render, redirect
from twilio.rest import Client
from .forms import *

# Create your views here.


def index(request):
    return render(request, "home.html", {})


# will only be available if user is logged in via Facebook
# contains link to add/update phone number, and will have messages for successful phone number + friend list updates
def login_home(request):
    return render(request, "login_home.html", {})


# will only be available if user is logged in via Facebook
def register(request):
    if request.method == "POST":
        user_to_save = TextbridgeUserForm(request.POST)
        if user_to_save.is_valid():
            if len(user_to_save.Phone_Number) != 12:
                # informs the user that the phone number is not formatted correctly
                return render(request, "registration_error.html", {})
            else:
                user_to_save.save()
        return render(request, "login_home.html", {})
    else:
        # ensure that the same form can be used to edit their phone number
        return render(request, "register.html", {})


# will only be triggered by button on login home that is only seen when person is logged in via facebook
def parse_friend_list(request):
    pass


# will only be available if user is logged in via Facebook and registers their phone number
def registration_success(request):
    return render(request, "login_home.html", {})
