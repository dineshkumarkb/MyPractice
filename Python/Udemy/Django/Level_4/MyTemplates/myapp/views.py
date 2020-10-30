from django.shortcuts import render

# Create your views here.

def base(request):

    return render(request,'myapp/base.html')


def index(request):

    myindex_dict = {'mykey':'This is my key from index'}

    return render(request,'myapp/index.html',context=myindex_dict)


def child(request):

    mychild_dict = {'mykey':'This is my key from child'}

    return render(request,'myapp/child.html',context=mychild_dict)


def other(request):

    myother_dict = {'mykey':'This is my key from other'}

    return render(request,'myapp/other.html',context=myother_dict)
