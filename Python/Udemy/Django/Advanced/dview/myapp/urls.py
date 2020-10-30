from django.conf.urls import url
from myapp.views import *


app_name = 'myapp'

urlpatterns = [

    url(r'^$',SchoolList.as_view(),name="mylist"),
    url(r'(?P<pk>\d+)/$',SchoolDetail.as_view(),name="detail"),
    url(r'^create/$',SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',SchoolDeleteView.as_view(),name='delete'),

]