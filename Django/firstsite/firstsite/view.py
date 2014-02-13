from django.http import HttpResponse
def hello(request):
    return HttpResponse('Hello world')
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html="<html><body>It's now %s.<p><input name=\"name\"/></p></body></html>" %now
    return HttpResponse(html)

def hours_add(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>In %s hour(s),it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)
