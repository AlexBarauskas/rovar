from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from map.forms import AddTrackForm

from account.decorators import login_required
from account.models import Account

def index(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    return render_to_response('html/main.html',
                              {'form': AddTrackForm(),
                               'user':user},
                              context_instance=RequestContext(request))
