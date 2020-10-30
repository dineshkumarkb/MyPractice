from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

from myapp.models import *

# Create your views here.


class Index(View):

    def get(self,request):

        return render(request,'base.html')


class AppIndex(View):

    def get(self,request):

        return render(request,'myapp/appbase.html')

class TempView(TemplateView):

    template_name = 'index.html'
    
    def get_context_data(self,**kwargs):
        
        context = super(TempView, self).get_context_data(**kwargs)
        context['sample'] = "This is a sample"

        return context

class SchoolList(ListView):

    context_object_name = 'schools_list'
    template_name = 'myapp/applist.html'
    model = School



class SchoolDetail(DetailView):

    context_object_name = 'schools_details'
    model = School
    template_name = 'myapp/appdetails.html'

class SchoolCreateView(CreateView):

    model = School
    fields = '__all__'
    template_name = 'myapp/appform.html'

class SchoolUpdateView(UpdateView):

    model = School
    fields = ('name','principal')


class SchoolDeleteView(DeleteView):

    model = School



