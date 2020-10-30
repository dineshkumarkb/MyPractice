# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()

class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    date = models.DateField()
    publisher =  models.ForeignKey(Publisher)



