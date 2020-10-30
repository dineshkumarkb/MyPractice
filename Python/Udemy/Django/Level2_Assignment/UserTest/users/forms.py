from django import forms
from users.models import UserInformation


class SignIn(forms.ModelForm):

    # username = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=8,widget=forms.PasswordInput)
    # feedback = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = UserInformation
        fields = '__all__'
