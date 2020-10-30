from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    # This is kind of inheritance for model
    user =  models.OneToOneField(User)


    # Additional Fields
    url = models.URLField(blank = True)
    pic = models.ImageField(upload_to='profile_pics',blank = True)
