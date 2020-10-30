# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.db import models



class Restaurant(models.Model):

    name = models.CharField(max_length=25,null=False,unique=True)


class MenuItem(models.Model):

    db_table = 'menuitem'
    name = models.CharField(max_length=100,null=False,unique=True)
    name = models.CharField(max_length=100,null=False,unique=True)
    price = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    r_id = models.ForeignKey(Restaurant,to_field='id',primary_key=True)
