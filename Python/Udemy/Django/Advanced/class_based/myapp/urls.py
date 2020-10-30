from django.conf.urls import url
from myapp.views import MyView,TempView,SchoolView,StudentView

app_name = 'myapp'

urlpatterns = [

    url(r'^$',MyView.as_view()),
    url(r'^temp/',TempView.as_view()),
    url(r'^list/',SchoolView.as_view()),
    url(r'^(?P<pk>[-\w]+)/',StudentView.as_view()),

]