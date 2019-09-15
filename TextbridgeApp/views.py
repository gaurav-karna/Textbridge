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


def get_from_name(from_number):
    user_list = User.objects.all()
    # make phone number list
    for entry in user_list:
        if from_number == entry.social_auth.extra_data['phone_number']:
            return "{} {}".format(str(entry.first_name), str(entry.last_name)).lower()
    return None


def get_user_friends(from_number):
    user_list = User.objects.all()
    # make phone number list
    friend_dict = {}
    for entry in user_list:
        if from_number == entry.social_auth.extra_data['phone_number']:     # user found, compile all friends
            for friend in entry.social_auth.extra_data.all_friends.data:
                friend_dict[friend.name] = get_to_number(friend.name)
    if friend_dict:
        return friend_dict
    else:
        return None


def get_to_number(to_name: str):
    user_list = User.objects.all()
    for entry in user_list:
        if "{} {}".format(entry.first_name, entry.last_name).lower() == to_name.lower():
            return entry.social_auth.extra_data['phone_number']
    return None


@csrf_exempt
def sms_api(request):
    # Start our TwiML response
    resp = MessagingResponse()
    # getting info from request
    message_body = str(request.POST['Body'])
    to_name = message_body.split('\n')[0]           # user-responsible for first line being first and last name
    from_number = str(request.POST['From'])

    from_name = get_from_name(from_number)
    if from_name is None:
        msg = resp.message("Could not find your number in our system. Please register at https://textbridge.online")
        return HttpResponse(str(resp)) # send failure text with return that number has not been registered with us

    msg = resp.message("Got here! From_Name: {}".format(from_name))
    return HttpResponse(str(resp))
    # returns a dict where keys are friends names, and values are user objects
    user_friends = get_user_friends(from_number)
    if not user_friends:
        msg = resp.message("Could not parse your friend list. Please register at https://textbridge.online")
        return HttpResponse(str(resp))  # friend list could not be parsed (FAILURE)

    to_number = user_friends.get(to_name.lower(), None)
    if to_number is None:
        # send failure text with return saying that user's number could not be found
        msg = resp.message("Could not retrieve recipient's number. Either not registered, or not your friend")
        return HttpResponse(str(resp))

    # successful text redirect
    msg = resp.message("Message from: {}\n{}".format(from_name, message_body), to=to_number)
    return HttpResponse(str(resp))


