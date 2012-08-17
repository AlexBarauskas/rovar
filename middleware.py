from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from map.forms import AddTrackForm, AddPointForm

from account.decorators import login_required
from account.models import Account
from blog.models import Post

def index(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    posts = Post.objects.all().order_by('-created')
    if posts.count>2:
        posts = posts[:2]
    return render_to_response('html/main.html',
                              {'form': AddTrackForm(),
                               'form_point':AddPointForm(prefix="point"),
                               'user':user,
                               'posts':posts},
                              context_instance=RequestContext(request))
