# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.core.urlresolvers import reverse

from account.models import Account
from map.models import Track, Point
from map.methods import change_data_add_track
from blog.models import Post
from blog.forms import AddPost


def index(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if user and not user.is_admin:
        return HttpResponseNotFound()
    return render_to_response('admin.html',
                              {'user':user},
                              context_instance=RequestContext(request))

def list_tracks(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()
    
    tracks = Track.objects.all()
    return render_to_response('list_tracks.html',
                              {'user':user,
                               'tracks': tracks},
                              context_instance=RequestContext(request))

def list_points(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()
    
    points = Point.objects.all()
    return render_to_response('list_points.html',
                              {'user':user,
                               'points': points},
                              context_instance=RequestContext(request))
def list_posts(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()
    
    posts = Post.objects.all()
    return render_to_response('list_posts.html',
                              {'user':user,
                               'posts': posts},
                              context_instance=RequestContext(request))

def edit_add_post(request,post_id=None):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()

    page_name = 'add post'
    if not post_id is None:
        param = {'instance':get_object_or_404(Post,id=post_id)}
        page_name = 'edit post'
    else:
        param = {}
    if request.method == 'POST':
        form = AddPost(request.POST,**param)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_list_posts'))
    else:
        form = AddPost(**param)
    return render_to_response('add-post.html',
                              {'user':user,
                               'form': form,
                               'page_name' : page_name},
                              context_instance=RequestContext(request))


INSTANCE = {
    'post':Post,
    'track':Track,
    'point':Point
    }
def delete_objects(request,name):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()

    table = INSTANCE.get(name,None)
    if not table is None:
        ids = request.GET.get('ids',None)
        if ids:
            ids = simplejson.loads(ids)
            table.objects.filter(id__in=ids).delete()
        else:
            table.objects.all().delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
        
        
        
