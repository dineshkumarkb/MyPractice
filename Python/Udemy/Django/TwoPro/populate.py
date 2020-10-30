import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','TwoPro.settings')


import django
django.setup()


from TwoApp.models import User
from faker import Faker


fakegen = Faker()


def add_user():

    f = fakegen.name().split()
    fname = f[0]
    lname = f[1]
    femail = fakegen.email()

    for entry in range(10):
        users = User.objects.get_or_create(firstname=fname, lastname=lname, email=femail)[0]
        users.save()

    return users



if __name__ == "__main__":
    add_user()


