from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from models import User
import json


def index(request):

    return HttpResponse("<em>My Second App</em>")



def help(request):

    my_dict = {"my_data" : "This is a help page"}

    return render(request,'TwoApp/help.html',context=my_dict)


def statics(request):

    return render(request,'TwoApp/static.html')


def user_info(request):

    myuser = User.objects.all()

    my_dict = {'user_data':myuser}

    return render(request,'TwoApp/users.html',context=my_dict)
