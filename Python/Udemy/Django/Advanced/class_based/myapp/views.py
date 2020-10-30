from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from django.http import HttpResponse

from myapp.models import *

# Create your views here.


class MyView(View):

    def get(self,request):

        return HttpResponse("Class based views example")

def index(request):

    return render(request,'base.html')


class TempView(TemplateView):

    template_name = 'temp.html'

    def get_context_data(self,**kwargs):
        
        context = super(TempView, self).get_context_data(**kwargs)
        context['my_data'] = "Template data passed"

        return context


class SchoolView(ListView):

    context_object_name = 'schools_list'
    model =  School
    template_name = 'list.html'


class StudentView(DetailView):

    model = Student
    template_name = 'school_detail.html'
    context_object_name = 'std_details'
