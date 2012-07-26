from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('html/main.html',
                              {},
                              context_instance=RequestContext(request))
