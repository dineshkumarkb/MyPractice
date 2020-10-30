from django.shortcuts import render
from myapp.forms import UserProfileForm,UserForm


from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def index(request):

    return render(request,'myapp/userindex.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def logged_me(request):

    return HttpResponse("Successfull Login")


def user_page(request):


    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']

            profile.save()

        else:
            print (user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'myapp/user.html',{'user_form': user_form,'profile_form':profile_form})





def home_page(request):

    return render(request,'myapp/base.html')



def user_login(request):

    if request.method == 'POST':

        print (" The request.post is ",request.POST)
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        user = authenticate(username = username,password=password)

        if user:

            if user.is_active:
                login(request,user)
                #return HttpResponse("You are logged in")
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            return HttpResponse("INVALID LOGIN")

    else:
        return render(request,'myapp/login.html')

