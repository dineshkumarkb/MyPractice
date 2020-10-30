import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','UserTest.settings')


import django
django.setup()

from users.models import UserInformation
from faker import Faker


def populate(N=5):

    fake = Faker()




    for i in range(N):
        z = fake.zipcode()
        e = fake.email()
        add = fake.address()
        n = fake.name()


        user = UserInformation.objects.get_or_create(name=n,address=add,email=e,zipcode =z)[0]
        user.save()

    return user


if __name__ == "__main__":
    populate()

