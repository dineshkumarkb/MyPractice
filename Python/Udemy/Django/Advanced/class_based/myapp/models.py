from django.db import models

# Create your models here.
class School(models.Model):

    name = models.CharField(max_length = 100)
    principal = models.CharField(max_length = 100)

    def __str__(self):
        return self.name



class Student(models.Model):

    name = models.CharField(max_length = 50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name="students")

    def __str__(self):
        return self.name