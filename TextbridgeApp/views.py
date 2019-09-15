from django.shortcuts import render, redirect
from twilio.rest import Client
from .secrets_twilio import *
from .forms import *
from .models import *
from django.contrib.auth.models import User
import social_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "home.html")


# will only be available if user is logged in via Facebook
# contains link to add/update phone number, and will have messages for successful phone number + friend list updates
@login_required
def login_home(request):
    logged_in_user = request.user.social_auth.filter(provider='facebook').first()
    return render(request, "login_home.html", {'fb_user': logged_in_user})


# will only be available if user is logged in via Facebook
@login_required
def register(request):
    if request.method == "POST":
        phone_to_save = TextbridgeUserForm(request.POST)
        if phone_to_save.is_valid():
            new_phone = phone_to_save.save()
            if (len(new_phone.Phone_Number) != 12) or (not new_phone.Phone_Number.startswith('+1')):
                # informs the user that the phone number is not formatted correctly
                return render(request, "registration_error.html", {
                    'error_message': 'Please format your phone number like: \'+12345678910\' '})
            else:
                logged_in_user = request.user.social_auth.filter(provider='facebook').first()
                logged_in_user.extra_data['phone_number'] = new_phone.Phone_Number
                logged_in_user.save()
                return login_home(request)
        else:
            return render(request, "registration_error.html", {
                'error_message': 'Please format your phone number like: \'+12345678910\' '})
    else:
        # ensure that the same form can be used to edit their phone number
        return render(request, "register.html", {'phone_form': TextbridgeUserForm()})


# delets the account from database
def delete_account(request):
    to_delete = User.objects.filter(email=request.user.email).first()
    to_delete.delete()
    return redirect('index')


# will only be available if user is logged in via Facebook and registers their phone number
def registration_success(request):
    return render(request, "login_home.html", {})


@csrf_exempt
def sms_api(request):
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("{}".format(str(request.POST)))

    return HttpResponse(str(resp))

