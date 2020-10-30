# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def stream_insights(request):

    #return HttpResponse("test stream page")

    return render(request,'Mypage.html')
