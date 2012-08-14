# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

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
    return render_to_response('html/admin/admin.html',
                              {'user':user},
                              context_instance=RequestContext(request))

def list_tracks(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()
    
    tracks = Track.objects.all()
    return render_to_response('html/admin/list_tracks.html',
                              {'user':user,
                               'tracks': tracks},
                              context_instance=RequestContext(request))

def delete_tracks(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()

    ids = request.GET.get('ids',None)
    if ids:
        ids = simplejson.loads(ids)
        Track.objects.filter(id__in=ids).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
def list_points(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()
    
    points = Point.objects.all()
    return render_to_response('html/admin/list_points.html',
                              {'user':user,
                               'points': points},
                              context_instance=RequestContext(request))

def delete_points(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()

    ids = request.GET.get('ids',None)
    if ids:
        ids = simplejson.loads(ids)
        Point.objects.filter(id__in=ids).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def list_posts(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()
    
    posts = Post.objects.all()
    return render_to_response('html/admin/list_posts.html',
                              {'user':user,
                               'posts': posts},
                              context_instance=RequestContext(request))

def add_post(request):
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    if not user.is_admin:
        return HttpResponseNotFound()

    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddPost()
    return render_to_response('html/admin/add-post.html',
                              {'user':user,
                               'form': form},
                              context_instance=RequestContext(request))
