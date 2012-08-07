# -*- coding: utf-8 -*-
from google.appengine.api import users
 
from django.conf import settings

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from account.models import Account
from account.decorators import login_required

@login_required
def main_page(request):
    return render_to_response('html/account/index.html',
                              {},
                              context_instance=RequestContext(request))

@login_required
def my_tracks(request):
    return render_to_response('html/account/my-tracks.html',
                              {},
                              context_instance=RequestContext(request))

@login_required
def my_points(request):
    return render_to_response('html/account/my-points.html',
                              {},
                              context_instance=RequestContext(request))


def login(request):
    return HttpResponseRedirect(users.create_login_url('/accounts/login_'))

def login_to_account(request):
    user = users.get_current_user()
    if user:
        request.session['user_email'] = user._User__email
        a = Account.objects.filter(email = user._User__email)
        if a.count()==0:
            a = Account(username = user.nickname(), email = user._User__email)
            a.save()
        else:
            a=a[0]
        request.session['user'] = a.id
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect(users.create_login_url('/accounts/login'))
    

def logout(request):
    request.user = None
    if request.session.has_key('user_email'):
        del request.session['user_email']
    if request.session.has_key('user'):
        del request.session['user']

    return HttpResponseRedirect(users.create_logout_url('/'))
