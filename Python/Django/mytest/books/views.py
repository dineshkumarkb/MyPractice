# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def books_home(request):

    return render(request,'books_home.html')


def books_base(request):

    return HttpResponse("HelloBookPage")
