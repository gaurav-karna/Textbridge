from django import forms
from .models import *


class TextbridgeUserForm(forms.ModelForm):
    class Meta():
        model = TextbridgeUser

        fields = [
            'Phone_Number',
        ]
