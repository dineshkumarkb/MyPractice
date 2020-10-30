# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Avg,Max

from django.http import HttpResponse
from models import Employee,Details


import json




# Create your views here.





def calc_average(request):


    if request.method == 'GET':

        all_sales = Details.objects.filter(dept="Sales").aggregate(Avg("salary")).values()[0]
        all_engg = Details.objects.filter(dept="Engineering").aggregate(Avg("salary")).values()[0]
        all_support = Details.objects.filter(dept="Support").aggregate(Avg("salary")).values()[0]

        all_depts = Details.objects.values_list('dept', flat=True).distinct()

        d = {}

        for depts in all_depts:

            if (depts == "Sales"):
                d[depts] = int(all_sales)

            elif (depts == "Engineering"):
                d[depts] = int(all_engg)

            elif (depts == "Support"):
                d[depts] = int(all_support)

        op = json.dumps(d, indent=4, sort_keys=True)


        my_dict = {'test_data':op}



        return render(request,"averages.html",context=my_dict)


def calc_headcount(request,myparams):


    if request.method == "GET":


        if myparams == "Sales":

            my_list = []

            sales_data = Details.objects.filter(dept="Sales").order_by("eff_date")


            for i,j in enumerate(sales_data,start=1):
                d = {}
                d["month"] = str(j.eff_date)
                d["headcount"] = i
                my_list.append(d)

            op = json.dumps(my_list, indent=4)
            my_dict = {'sales_data': op}
            return render(request,'headcount_sales.html',my_dict)




        elif myparams == "Engineering":

            my_list=[]

            engg_data = Details.objects.filter(dept="Engineering").order_by("eff_date")

            for i,j in enumerate(engg_data,start=1):
                d = {}
                d["month"] = str(j.eff_date)
                d["headcount"] = i
                my_list.append(d)

            op = json.dumps(my_list, indent=4)
            my_dict = {'engg_data': op}
            return render(request, 'headcount_engg.html', my_dict)

        elif myparams == "Support":

            my_list = []

            supp_data = Details.objects.filter(dept="Support")

            for i,j in enumerate(supp_data,start=1):
                d = {}
                d["month"] = str(j.eff_date)
                d["headcount"] = i
                my_list.append(d)

            op = json.dumps(my_list, indent=4)

            my_dict = {'support_data': op}

            return render(request, 'headcount_support.html', my_dict)










