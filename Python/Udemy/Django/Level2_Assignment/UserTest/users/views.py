# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from users.models import UserInformation
from users.forms import SignIn

# Create your views here.


def index(request):

    return render(request,'users/index.html')


def users(request):

    form = SignIn()

    user_data = UserInformation.objects.order_by("name")

    op_data = {'user_info':user_data,'form':form}

    if request.method == 'POST':
        user_form = SignIn(request.POST)

        if user_form.is_valid():
            sign_in = UserInformation.objects.get_or_create(name=user_form.cleaned_data['name'],
                                                   address = user_form.cleaned_data['address'],
                                                   email = user_form.cleaned_data['email'],
                                                   zipcode = user_form.cleaned_data['zipcode'])[0]

            sign_in.save()
            return index(request)

    return render(request,'users/myform.html',context=op_data)
