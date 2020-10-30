from django import forms
from myapp.models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):

    url = forms.URLField(required=False)
    pic = forms.ImageField(required=False)

    class Meta():

        model = UserProfile
        fields = ('url','pic')


class UserForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:

        model = User
        fields = ('username','password','email')
