from django.db import models

# Create your models here.


class Contacts(models.Model):
    first_name = models.CharField(max_length=150,)
    last_name = models.CharField(max_length=150, default='Lastname')
    mobile = models.CharField(max_length=255,)
    email = models.EmailField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)