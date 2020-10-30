# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,render_to_response

# Create your views here.
def home(request):
    mylist = [1,2,3,4,5]
    myname = "DineshKumar"

    args = {'fname': myname,'myiter':mylist}
    return render(request, 'testapp/login.html', args)


def base(request):

    return render(request, 'base.html')
