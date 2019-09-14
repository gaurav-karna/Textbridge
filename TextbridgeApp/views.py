from django.shortcuts import render, redirect
from twilio.rest import Client
from .forms import *

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "home.html")


# will only be available if user is logged in via Facebook
# contains link to add/update phone number, and will have messages for successful phone number + friend list updates
@login_required
def login_home(request):
    return render(request, "login_home.html")


# will only be available if user is logged in via Facebook
@login_required
def register(request):
    if request.method == "POST":
        phone_to_save = TextbridgeUserForm(request.POST)
        user_to_save = request.user
        if phone_to_save.is_valid():
            if (len(phone_to_save.Phone_Number) != 12) or (not phone_to_save.Phone_Number.startswith('+1')):
                # informs the user that the phone number is not formatted correctly
                return render(request, "registration_error.html", {
                    'error_message': 'Please format your phone number like: \'+12345678910\' '})
            else:
                user_to_save.phone_number = phone_to_save.Phone_Number
                user_to_save.save()
        else:
            return render(request, "registration_error.html", {
                'error_message': 'Please format your phone number like: \'+12345678910\' '})
        return render(request, "login_home.html")
    else:
        # ensure that the same form can be used to edit their phone number
        return render(request, "register.html", {'phone_form': TextbridgeUserForm()})


# will only be triggered by button on login home that is only seen when person is logged in via facebook
# def parse_friend_list(request):
#     pass


# will only be available if user is logged in via Facebook and registers their phone number
def registration_success(request):
    return render(request, "login_home.html", {})
