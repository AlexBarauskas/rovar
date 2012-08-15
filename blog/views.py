# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.core.urlresolvers import reverse

from account.models import Account
from blog.models import Post

def add_like(request,post_id):
    key = 'like-'+post_id
    errors = None
    post = get_object_or_404(Post,id=post_id)    
    if request.session.get(key,False):
        post.like+=1
        post.save()
        request.session[key]=True
    else:
        errors = u'Вы не можаце лайкануць другi раз :('
    return HttpResponse(simplejson.dumps({'errors':errors,
                                          'like':post.like}),mimetype='text/json')
    
