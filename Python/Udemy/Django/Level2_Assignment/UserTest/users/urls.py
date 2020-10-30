from django.conf.urls import url
from django.contrib import admin

from users.views import *

urlpatterns = [

    url(r'^$',users,name='users'),

]