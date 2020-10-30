# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse



def root_page(request):

    mydict = {'fname':'Dinesh','lname':'Kumar'}
    return render(request,'app1/index.html',context=mydict)