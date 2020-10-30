# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInformation(models.Model):

    name = models.CharField(max_length=128)
    address =  models.CharField(max_length=700)
    email = models.EmailField(unique=True)
    zipcode = models.IntegerField()
