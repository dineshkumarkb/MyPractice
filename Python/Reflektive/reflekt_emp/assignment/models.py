# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):

    #salary = models.ForeignKey('self',on_delete=models.CASCADE)
    emp_id = models.IntegerField(primary_key = True,default=1)





class Details(models.Model):


    eff_date = models.DateField()
    employee_id = models.ForeignKey(Employee,related_name="empl_id",default=1)
    salary = models.IntegerField()
    dept = models.CharField(max_length=50)




#from assignment.models import Employee,Details
# e=Employee(emp_id=4,salary=45000)
# d = Details(eff_date="2015-03-01",dept="Sales")