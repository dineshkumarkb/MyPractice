# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from users.models import UserInformation

# Register your models here.
admin.site.register(UserInformation)
