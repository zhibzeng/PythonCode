from django.template.loader import get_template
from django.template import Template,Context
from django.http import HttpResponse
import datetime
def timenow(request):
    now=datetime.datetime.now()
    na="Django"
    fa="±à³Ì!"
    t=get_template('template.html')
    html=t.render(Context({'nowdate':now,'name':na,'favourite':fa}))
    return HttpResponse(html)