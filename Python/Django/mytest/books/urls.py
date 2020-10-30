from django.conf.urls import url

from views import *

urlpatterns = [

    url(r'^home$',books_home),
    url(r'^$',books_base)

]