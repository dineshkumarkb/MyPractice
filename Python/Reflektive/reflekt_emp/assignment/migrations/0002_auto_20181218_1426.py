# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-18 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]