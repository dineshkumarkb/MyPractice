from django.http import HttpResponse,Http404
import datetime

from django.template import Template,Context


def hi(request):
    return HttpResponse("HelloPage")

def home(request):

    class Person(object):
        def __init__(self,fname,lname):
            self.fname = fname
            self.lname = lname

        def get_first(self):
            raise AssertionError,"dinesh"
    t = Template(' My Firstname : {{person.ffname}}, My Lastname {{person.lname}}')
    c = Context({'person':Person("Dinesh","Kumar")})
    s = t.render(c)
    return HttpResponse(s)

def curr_date(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"% now
    return HttpResponse(html)

def off_time(request,off):
    try:
         offset = int(off)
    except ValueError:
         raise Http404
    d = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>It will be %s in %s hours.</body></html>" % (d,offset)
    return HttpResponse(html)