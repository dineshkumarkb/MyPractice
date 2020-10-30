from django.db import models
from django.core.urlresolvers import reverse,reverse_lazy

# Create your models here.


class School(models.Model):

    name = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse("myapp:detail",kwargs={'pk':self.pk})



class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students')


    def __str__(self):
        return self.name