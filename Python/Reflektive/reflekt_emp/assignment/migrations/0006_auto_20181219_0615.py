# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-19 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0005_auto_20181219_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dept',
            field=models.CharField(default='New employee', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='eff_date',
            field=models.DateField(default='2019-09-09'),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='salary',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='detail_salary', to='assignment.Employee'),
        ),
    ]