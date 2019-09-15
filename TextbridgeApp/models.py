from django.db import models

# Create your models here.


class TextbridgeUser(models.Model):
    Phone_Number = models.CharField(max_length=12, verbose_name='Phone Number', default=None,
                                    help_text='Format your number like: +12345678910')

    Backup_Name = models.CharField(max_length=64, verbose_name='Backup Referring Name', default=None, null=True)
