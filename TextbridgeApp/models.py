from django.db import models

# Create your models here.


class TextbridgeUser(models.Model):
    Phone_Number = models.CharField(max_length=12, verbose_name='Phone Number',
                                    help_text='Format your number like: +12345678910')

    Friend_List = models.TextField(max_length=65536)  # will be populated upon Facebook authentication
