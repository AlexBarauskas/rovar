from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from map.forms import AddTrackForm

def index(request):
    return render_to_response('html/main.html',
                              {'form': AddTrackForm()},
                              context_instance=RequestContext(request))
